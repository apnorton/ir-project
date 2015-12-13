# Generated from T by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\n/\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write(u"\5\3\5\3\6\3\6\3\7\3\7\3\b\6\b#\n\b\r\b\16\b$\3\b\3\b")
        buf.write(u"\3\t\6\t*\n\t\r\t\16\t+\3\n\3\n\2\2\13\3\3\5\4\7\5\t")
        buf.write(u"\6\13\7\r\b\17\t\21\n\23\2\3\2\4\5\2\13\f\17\17\"\"\3")
        buf.write(u"\2\62;/\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write(u"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write(u"\3\25\3\2\2\2\5\27\3\2\2\2\7\31\3\2\2\2\t\33\3\2\2\2")
        buf.write(u"\13\35\3\2\2\2\r\37\3\2\2\2\17\"\3\2\2\2\21)\3\2\2\2")
        buf.write(u"\23-\3\2\2\2\25\26\7*\2\2\26\4\3\2\2\2\27\30\7+\2\2\30")
        buf.write(u"\6\3\2\2\2\31\32\7,\2\2\32\b\3\2\2\2\33\34\7-\2\2\34")
        buf.write(u"\n\3\2\2\2\35\36\7\61\2\2\36\f\3\2\2\2\37 \7/\2\2 \16")
        buf.write(u"\3\2\2\2!#\t\2\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%")
        buf.write(u"\3\2\2\2%&\3\2\2\2&\'\b\b\2\2\'\20\3\2\2\2(*\5\23\n\2")
        buf.write(u")(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\22\3\2\2\2")
        buf.write(u"-.\t\3\2\2.\24\3\2\2\2\5\2$+\3\b\2\2")
        return buf.getvalue()


class TLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    MUL = 3
    ADD = 4
    DIV = 5
    SUB = 6
    WS = 7
    INT = 8

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'('", u"')'", u"'*'", u"'+'", u"'/'", u"'-'" ]

    symbolicNames = [ u"<INVALID>",
            u"MUL", u"ADD", u"DIV", u"SUB", u"WS", u"INT" ]

    ruleNames = [ u"T__0", u"T__1", u"MUL", u"ADD", u"DIV", u"SUB", u"WS", 
                  u"INT", u"DIGIT" ]

    grammarFileName = u"T"

    def __init__(self, input=None):
        super(TLexer, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


