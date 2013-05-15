#include "auth.h"

static const uint8_t encoding_table[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
static const uint8_t decoding_table[] = {
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //10 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //20 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //30 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //40 
  0,   0,   0,  62,   0,   0,   0,  63,  52,  53, //50 
 54,  55,  56,  57,  58,  59,  60,  61,   0,   0, //60 
  0,   0,   0,   0,   0,   0,   1,   2,   3,   4, //70 
  5,   6,   7,   8,   9,  10,  11,  12,  13,  14, //80 
 15,  16,  17,  18,  19,  20,  21,  22,  23,  24, //90 
 25,   0,   0,   0,   0,   0,   0,  26,  27,  28, //100 
 29,  30,  31,  32,  33,  34,  35,  36,  37,  38, //110 
 39,  40,  41,  42,  43,  44,  45,  46,  47,  48, //120 
 49,  50,  51,   0,   0,   0,   0,   0,   0,   0, //130 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //140 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //150 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //160 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //170 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //180 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //190 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //200 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //210 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //220 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //230 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //240 
  0,   0,   0,   0,   0,   0,   0,   0,   0,   0, //250 
  0,   0,   0,   0,   0,   0,
};

size_t base64_encode_len(size_t src_len)
{
	return 4 * ((src_len + 2) / 3);
}

uint8_t *base64_encode(const uint8_t *src, size_t src_len, uint8_t *dst, size_t *dst_len)
{
	uint8_t in[3];
	uint8_t *po = dst;
	uint32_t triple;
	size_t i;

	*dst_len = 4 * ((src_len + 2) / 3);
	fprintf(stderr, "dst_len is %d\n", *dst_len);
	for (i = 0; i + 2 < src_len; i += 3) {
		in[0] = src[i];
		in[1] = src[i + 1];
		in[2] = src[i + 2];
		triple = (in[0] << 0x10) + (in[1] << 0x08) + in[2];
		*po++ = encoding_table[(triple >> 3 * 6) & 0x3f];
		*po++ = encoding_table[(triple >> 2 * 6) & 0x3f];
		*po++ = encoding_table[(triple >> 1 * 6) & 0x3f];
		*po++ = encoding_table[(triple >> 0 * 6) & 0x3f];
	}
	if (src_len % 3 == 1) {
		*po++ = encoding_table[src[i] >> 0x02];
		*po++ = encoding_table[(src[i] & 0x03) << 4];
		*po++ = '=';
		*po++ = '=';
	} else if (src_len % 3 == 2) {
		triple = (src[i] << 0x10) + (src[i + 1] << 0x08);
		*po++ = encoding_table[(triple >> 3 * 6) & 0x3f];
		*po++ = encoding_table[(triple >> 2 * 6) & 0x3f];
		*po++ = encoding_table[(triple >> 1 * 6) & 0x3f];
		*po++ = '=';
	}
	// *(dst + *dst_len) = '\0';
	*po = '\0';
	return dst;
}

size_t base64_decode_len(const uint8_t *src, size_t src_len)
{
	int pad = 0;
	size_t dst_len;

	if (src[src_len - 1] == '=') {
		pad++;
		if (src[src_len - 2] == '=') {
			pad++;
		}
	}
	dst_len = src_len * 3 / 4 - pad;
	return dst_len;
}

uint8_t *base64_decode(const uint8_t *src, size_t src_len, uint8_t *dst, size_t *dst_len)
{
	uint8_t in[4];
	int pad = 0;
	uint8_t *psrc = (uint8_t *)src;
	int i;

	if (src[src_len - 1] == '=') {
		pad++;
		if (src[src_len - 2] == '=') {
			pad++;
		}
	}
	*dst_len = src_len * 3 / 4 - pad;
	int index = 0;
	for (i = 0; i <= src_len - 4 - pad; i += 4) {
		in[0] = decoding_table[psrc[i + 0]];
		in[1] = decoding_table[psrc[i + 1]];
		in[2] = decoding_table[psrc[i + 2]];
		in[3] = decoding_table[psrc[i + 3]];

		dst[index++] = (in[0] << 2) | (in[1] >> 4);
		dst[index++] = (in[1] << 4) | (in[2] >> 2);
		dst[index++] = (in[2] << 6) | (in[3]);
	}
	if (pad == 1) {
		in[0] = decoding_table[psrc[i + 0]];
		in[1] = decoding_table[psrc[i + 1]];
		in[2] = decoding_table[psrc[i + 2]];

		dst[index++] = (in[0] << 2) | (in[1] >> 4);
		dst[index++] = (in[1] << 4) | (in[2] >> 2);
	} else if (pad == 2) {
		in[0] = decoding_table[psrc[i + 0]];
		in[1] = decoding_table[psrc[i + 1]];

		dst[index++] = (in[0] << 2) | (in[1] >> 4);
	}
	dst[index] = '\0';
	return dst;
}

uint8_t *urlencode(const uint8_t *src, uint8_t *dst)
{
	uint8_t *psrc = (uint8_t *)src;
	uint8_t *pdst = dst;

	while (*psrc) {
		if ( isalnum(*psrc) || *psrc == '-'
		    || *psrc == '_' || *psrc == '.'
		    || *psrc == '~')
			*pdst++ = *psrc;
		else if (*psrc == ' ')
			*pdst++ = '+';
		else {
			*pdst++ = '%';
			*pdst++ = to_hex(*psrc >> 4);
			*pdst++ = to_hex(*psrc & 0xf);
		}
		psrc++;
	}
	pdst = '\0';
	return dst;
}

char *urldecode(const char *src, size_t src_len, char *dst, size_t *dst_len)
{
	uint8_t *psrc = (uint8_t *)src;
	uint8_t *pdst = dst;

	while (*psrc) {
		if (*psrc == '%') {
			if (psrc[1] && psrc[2]) {
				*pdst++ = from_hex(psrc[1] << 4 | from_hex(psrc[2]));
				psrc += 3;
			}
		} else if (*psrc == '+') {
			*pdst++ = ' ';
			psrc++;
		} else
			*pdst++ = *psrc++;
	}
	*pdst = '\0';
	return dst;
}
