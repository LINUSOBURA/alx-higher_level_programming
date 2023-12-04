#!/usr/bin/python3


def multiple_returns(sentence):
    if not sentence:
        sentence[0] = None
    len_sent = len(sentence)

    return (len_sent, sentence[0])
