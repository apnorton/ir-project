# Generated from LatexGram.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\7\31\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\5\3\f\n\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3")
        buf.write(u"\3\2\3\4\4\2\4\2\2\31\2\6\3\2\2\2\4\13\3\2\2\2\6\7\5")
        buf.write(u"\4\3\2\7\3\3\2\2\2\b\t\b\3\1\2\t\f\7\5\2\2\n\f\7\7\2")
        buf.write(u"\2\13\b\3\2\2\2\13\n\3\2\2\2\f\25\3\2\2\2\r\16\f\6\2")
        buf.write(u"\2\16\17\7\3\2\2\17\24\5\4\3\7\20\21\f\5\2\2\21\22\7")
        buf.write(u"\4\2\2\22\24\5\4\3\6\23\r\3\2\2\2\23\20\3\2\2\2\24\27")
        buf.write(u"\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\5\3\2\2\2\27")
        buf.write(u"\25\3\2\2\2\5\13\23\25")
        return buf.getvalue()


class LatexGramParser ( Parser ):

    grammarFileName = "LatexGram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'*'", u"'+'" ]

    symbolicNames = [ u"<INVALID>", u"MULT", u"ADD", u"INT", u"WS", u"VAR" ]

    RULE_s = 0
    RULE_e = 1

    ruleNames =  [ u"s", u"e" ]

    EOF = Token.EOF
    MULT=1
    ADD=2
    INT=3
    WS=4
    VAR=5

    def __init__(self, input):
        super(LatexGramParser, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LatexGramParser.SContext, self).__init__(parent, invokingState)
            self.parser = parser

        def e(self):
            return self.getTypedRuleContext(LatexGramParser.EContext,0)


        def getRuleIndex(self):
            return LatexGramParser.RULE_s

        def enterRule(self, listener):
            if hasattr(listener, "enterS"):
                listener.enterS(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitS"):
                listener.exitS(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitS"):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = LatexGramParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.e(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LatexGramParser.EContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LatexGramParser.RULE_e

     
        def copyFrom(self, ctx):
            super(LatexGramParser.EContext, self).copyFrom(ctx)


    class AddContext(EContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.EContext)
            super(LatexGramParser.AddContext, self).__init__(parser)
            self.copyFrom(ctx)

        def e(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LatexGramParser.EContext)
            else:
                return self.getTypedRuleContext(LatexGramParser.EContext,i)

        def ADD(self):
            return self.getToken(LatexGramParser.ADD, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAdd"):
                listener.enterAdd(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAdd"):
                listener.exitAdd(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAdd"):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(EContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.EContext)
            super(LatexGramParser.MultContext, self).__init__(parser)
            self.copyFrom(ctx)

        def e(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LatexGramParser.EContext)
            else:
                return self.getTypedRuleContext(LatexGramParser.EContext,i)

        def MULT(self):
            return self.getToken(LatexGramParser.MULT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMult"):
                listener.enterMult(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMult"):
                listener.exitMult(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitMult"):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(EContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.EContext)
            super(LatexGramParser.VarContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(LatexGramParser.VAR, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVar"):
                listener.enterVar(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVar"):
                listener.exitVar(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitVar"):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(EContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.EContext)
            super(LatexGramParser.IntContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LatexGramParser.INT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterInt"):
                listener.enterInt(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInt"):
                listener.exitInt(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitInt"):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def e(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LatexGramParser.EContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_e, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            token = self._input.LA(1)
            if token in [LatexGramParser.INT]:
                localctx = LatexGramParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(LatexGramParser.INT)

            elif token in [LatexGramParser.VAR]:
                localctx = LatexGramParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(LatexGramParser.VAR)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 17
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = LatexGramParser.MultContext(self, LatexGramParser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 11
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 12
                        self.match(LatexGramParser.MULT)
                        self.state = 13
                        self.e(5)
                        pass

                    elif la_ == 2:
                        localctx = LatexGramParser.AddContext(self, LatexGramParser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 14
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 15
                        self.match(LatexGramParser.ADD)
                        self.state = 16
                        self.e(4)
                        pass

             
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.e_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def e_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




