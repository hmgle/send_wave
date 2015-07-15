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

install::
	mkdir -p ~/.send_wave
	cp -p config.cfg.example ~/.send_wave/config.cfg
	cp *.py /usr/local/bin/

uninstall::
	-rm -rf ~/.send_wave
	-rm -f /usr/local/bin/fanfou_config.py
	-rm -f /usr/local/bin/fanfouphoto.py
	-rm -f /usr/local/bin/fanfou.py
	-rm -f /usr/local/bin/fanfousender.py
	-rm -f /usr/local/bin/request_token.py
	-rm -f /usr/local/bin/tqq_msg.py
	-rm -f /usr/local/bin/tqq_pic.py
	-rm -f /usr/local/bin/tqq.py
	-rm -f /usr/local/bin/weibo_msg.py
	-rm -f /usr/local/bin/weibo_pic.py
	-rm -f /usr/local/bin/weibo.py

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
