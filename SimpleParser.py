# Generated from Simple.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,4,1,22,8,1,11,1,12,1,23,1,
        1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,38,8,2,11,2,12,
        2,39,1,2,1,2,3,2,44,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,54,8,
        3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,5,1,5,3,
        5,69,8,5,1,5,0,1,8,6,0,2,4,6,8,10,0,0,71,0,13,1,0,0,0,2,17,1,0,0,
        0,4,43,1,0,0,0,6,53,1,0,0,0,8,55,1,0,0,0,10,68,1,0,0,0,12,14,3,2,
        1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,
        1,0,0,0,17,18,5,1,0,0,18,19,5,11,0,0,19,21,5,2,0,0,20,22,3,4,2,0,
        21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,
        0,0,0,25,26,5,3,0,0,26,3,1,0,0,0,27,28,5,4,0,0,28,29,5,11,0,0,29,
        44,5,5,0,0,30,31,5,4,0,0,31,32,5,11,0,0,32,33,5,6,0,0,33,34,5,11,
        0,0,34,35,5,7,0,0,35,37,5,2,0,0,36,38,3,6,3,0,37,36,1,0,0,0,38,39,
        1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,3,0,0,
        42,44,1,0,0,0,43,27,1,0,0,0,43,30,1,0,0,0,44,5,1,0,0,0,45,46,3,8,
        4,0,46,47,5,5,0,0,47,54,1,0,0,0,48,49,5,11,0,0,49,50,5,8,0,0,50,
        51,3,8,4,0,51,52,5,5,0,0,52,54,1,0,0,0,53,45,1,0,0,0,53,48,1,0,0,
        0,54,7,1,0,0,0,55,56,6,4,-1,0,56,57,3,10,5,0,57,63,1,0,0,0,58,59,
        10,2,0,0,59,60,5,9,0,0,60,62,3,10,5,0,61,58,1,0,0,0,62,65,1,0,0,
        0,63,61,1,0,0,0,63,64,1,0,0,0,64,9,1,0,0,0,65,63,1,0,0,0,66,69,5,
        10,0,0,67,69,5,11,0,0,68,66,1,0,0,0,68,67,1,0,0,0,69,11,1,0,0,0,
        7,15,23,39,43,53,63,68
    ]

class SimpleParser ( Parser ):

    grammarFileName = "Simple.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'{'", "'}'", "'int'", "';'", 
                     "'('", "')'", "'='", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "ID", "WS" ]

    RULE_prog = 0
    RULE_classDef = 1
    RULE_member = 2
    RULE_stat = 3
    RULE_expr = 4
    RULE_term = 5

    ruleNames =  [ "prog", "classDef", "member", "stat", "expr", "term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    INT=10
    ID=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.ClassDefContext)
            else:
                return self.getTypedRuleContext(SimpleParser.ClassDefContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = SimpleParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.classDef()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.MemberContext)
            else:
                return self.getTypedRuleContext(SimpleParser.MemberContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_classDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDef" ):
                listener.enterClassDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDef" ):
                listener.exitClassDef(self)




    def classDef(self):

        localctx = SimpleParser.ClassDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(SimpleParser.T__0)
            self.state = 18
            self.match(SimpleParser.ID)
            self.state = 19
            self.match(SimpleParser.T__1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.member()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 25
            self.match(SimpleParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleParser.ID)
            else:
                return self.getToken(SimpleParser.ID, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.StatContext)
            else:
                return self.getTypedRuleContext(SimpleParser.StatContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember" ):
                listener.enterMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember" ):
                listener.exitMember(self)




    def member(self):

        localctx = SimpleParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member)
        self._la = 0 # Token type
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(SimpleParser.T__3)
                self.state = 28
                self.match(SimpleParser.ID)
                self.state = 29
                self.match(SimpleParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(SimpleParser.T__3)
                self.state = 31
                self.match(SimpleParser.ID)
                self.state = 32
                self.match(SimpleParser.T__5)
                self.state = 33
                self.match(SimpleParser.ID)
                self.state = 34
                self.match(SimpleParser.T__6)
                self.state = 35
                self.match(SimpleParser.T__1)
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 36
                    self.stat()
                    self.state = 39 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==10 or _la==11):
                        break

                self.state = 41
                self.match(SimpleParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleParser.ExprContext,0)


        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = SimpleParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(SimpleParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(SimpleParser.ID)
                self.state = 49
                self.match(SimpleParser.T__7)
                self.state = 50
                self.expr(0)
                self.state = 51
                self.match(SimpleParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TermExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(SimpleParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermExpr" ):
                listener.enterTermExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermExpr" ):
                listener.exitTermExpr(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SimpleParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(SimpleParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SimpleParser.TermExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 56
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleParser.AddExprContext(self, SimpleParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 58
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 59
                    self.match(SimpleParser.T__8)
                    self.state = 60
                    self.term() 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SimpleParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntTerm" ):
                listener.enterIntTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntTerm" ):
                listener.exitIntTerm(self)


    class IdTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdTerm" ):
                listener.enterIdTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdTerm" ):
                listener.exitIdTerm(self)



    def term(self):

        localctx = SimpleParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_term)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = SimpleParser.IntTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(SimpleParser.INT)
                pass
            elif token in [11]:
                localctx = SimpleParser.IdTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(SimpleParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




