CC = gcc
CFLAGS += -Wall -DDEBUG=1 -g

SRCDIR = src
SRC := $(wildcard $(SRCDIR)/*.c)
ODIR := obj
OBJ  := $(patsubst %.c,$(ODIR)/%.o,$(SRC))

.PHONY: all clean

TARGET =
TMPTARGET = test_base64

all: $(TARGET) $(TMPTARGET)

test_base64: $(ODIR)/auth.o $(ODIR)/test_base64.o

$(ODIR):
	@mkdir $@

$(ODIR)/%.o : %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	-rm -f *.o $(TARGET) $(TMPTARGET) obj/* src/*.d

sinclude $(SRC:.c=.d)

%.d: %.c
	@if !(test -d obj);then mkdir obj;fi
	@set -e; rm -f $@; \
		$(CC) -MM $(CPPFLAGS) $< > $@.$$$$; \
		sed 's,\(.*\)\.o[:]*,$(ODIR)/\1.o $@:,' < $@.$$$$ > $@; \
		rm -f $@.$$$$

vpath %.c src
vpath %.h src
vpath %.o obj
