#ifndef _DEBUG_LOG_H
#define _DEBUG_LOG_H

#include <stdio.h>
#include <string.h>

#if DEBUG
FILE *DEBUG_LOG_FILE;
char DEBUG_STRING[1024];
#else
FILE *DEBUG_LOG_FILE;
char *DEBUG_STRING;
#ifndef NDEBUG
#define NDEBUG
#endif /* #ifndef NDEBUG */
#endif /* #if DEBUG */
#include <assert.h>

#define debug_print(fmt, ...) \
    do { \
        if (DEBUG) \
            fprintf(stderr, "debug_print: %s: %d: %s():" \
                    fmt "\n", __FILE__, __LINE__, __func__, \
                    ##__VA_ARGS__); \
    } while (0)

#define open_debug_log(filename) do { \
    if (DEBUG) { \
        DEBUG_LOG_FILE = fopen(filename, "w"); \
    } \
} while (0)

#define debug_log(fmt, ...) do { \
    if (DEBUG) { \
        snprintf(DEBUG_STRING, 1023, "%s: %s(): %d: " fmt "\n", __FILE__, __func__, __LINE__, ##__VA_ARGS__); \
        fwrite(DEBUG_STRING, 1, strlen(DEBUG_STRING), DEBUG_LOG_FILE); \
        fflush(DEBUG_LOG_FILE); \
    } \
} while (0)

#define close_debug_log() do { \
    if (DEBUG) { \
        fclose(DEBUG_LOG_FILE); \
    } \
} while (0)

#endif
