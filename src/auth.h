#ifndef _AUTH_H
#define _AUTH_H

#include <stdio.h>
#include <stdint.h>

size_t base64_encode_len(size_t src_len);
uint8_t *base64_encode(const uint8_t *src, size_t src_len, uint8_t *dst, size_t *dst_len);
size_t base64_decode_len(const uint8_t *src, size_t src_len);
uint8_t *base64_decode(const uint8_t *src, size_t src_len, uint8_t *dst, size_t *dst_len);
char *urlencode(const char *src, int len, char *dst);
char *urldecode(const char *src, int len, char *dst);

#endif
