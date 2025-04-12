# Generated from Simple.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SimpleParser import SimpleParser
else:
    from SimpleParser import SimpleParser

# This class defines a complete listener for a parse tree produced by SimpleParser.
class SimpleListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleParser#prog.
    def enterProg(self, ctx:SimpleParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleParser#prog.
    def exitProg(self, ctx:SimpleParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleParser#classDef.
    def enterClassDef(self, ctx:SimpleParser.ClassDefContext):
        pass

    # Exit a parse tree produced by SimpleParser#classDef.
    def exitClassDef(self, ctx:SimpleParser.ClassDefContext):
        pass


    # Enter a parse tree produced by SimpleParser#member.
    def enterMember(self, ctx:SimpleParser.MemberContext):
        pass

    # Exit a parse tree produced by SimpleParser#member.
    def exitMember(self, ctx:SimpleParser.MemberContext):
        pass


    # Enter a parse tree produced by SimpleParser#stat.
    def enterStat(self, ctx:SimpleParser.StatContext):
        pass

    # Exit a parse tree produced by SimpleParser#stat.
    def exitStat(self, ctx:SimpleParser.StatContext):
        pass


    # Enter a parse tree produced by SimpleParser#TermExpr.
    def enterTermExpr(self, ctx:SimpleParser.TermExprContext):
        pass

    # Exit a parse tree produced by SimpleParser#TermExpr.
    def exitTermExpr(self, ctx:SimpleParser.TermExprContext):
        pass


    # Enter a parse tree produced by SimpleParser#AddExpr.
    def enterAddExpr(self, ctx:SimpleParser.AddExprContext):
        pass

    # Exit a parse tree produced by SimpleParser#AddExpr.
    def exitAddExpr(self, ctx:SimpleParser.AddExprContext):
        pass


    # Enter a parse tree produced by SimpleParser#IntTerm.
    def enterIntTerm(self, ctx:SimpleParser.IntTermContext):
        pass

    # Exit a parse tree produced by SimpleParser#IntTerm.
    def exitIntTerm(self, ctx:SimpleParser.IntTermContext):
        pass


    # Enter a parse tree produced by SimpleParser#IdTerm.
    def enterIdTerm(self, ctx:SimpleParser.IdTermContext):
        pass

    # Exit a parse tree produced by SimpleParser#IdTerm.
    def exitIdTerm(self, ctx:SimpleParser.IdTermContext):
        pass



del SimpleParser