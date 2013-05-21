#ifndef _AUTH_H
#define _AUTH_H

#include <stdio.h>
#include <stdint.h>

size_t base64_encode_len(size_t src_len);
uint8_t *base64_encode(const uint8_t *src, size_t src_len, uint8_t *dst);
size_t base64_decode_len(const uint8_t *src, size_t src_len);
uint8_t *base64_decode(const uint8_t *src, size_t src_len, uint8_t *dst);
uint8_t *urlencode(const uint8_t *src, uint8_t *dst);
uint8_t *urldecode(const uint8_t *src, uint8_t *dst);
uint8_t *oauth_nonce(uint8_t *str, size_t len);

#endif
