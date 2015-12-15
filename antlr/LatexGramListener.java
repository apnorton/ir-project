// Generated from LatexGram.g4 by ANTLR 4.5.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LatexGramParser}.
 */
public interface LatexGramListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LatexGramParser#s}.
	 * @param ctx the parse tree
	 */
	void enterS(LatexGramParser.SContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexGramParser#s}.
	 * @param ctx the parse tree
	 */
	void exitS(LatexGramParser.SContext ctx);
	/**
	 * Enter a parse tree produced by the {@code div}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDiv(LatexGramParser.DivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code div}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDiv(LatexGramParser.DivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code add}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAdd(LatexGramParser.AddContext ctx);
	/**
	 * Exit a parse tree produced by the {@code add}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAdd(LatexGramParser.AddContext ctx);
	/**
	 * Enter a parse tree produced by the {@code sub}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterSub(LatexGramParser.SubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code sub}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitSub(LatexGramParser.SubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mul}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMul(LatexGramParser.MulContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mul}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMul(LatexGramParser.MulContext ctx);
	/**
	 * Enter a parse tree produced by the {@code atomic}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAtomic(LatexGramParser.AtomicContext ctx);
	/**
	 * Exit a parse tree produced by the {@code atomic}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAtomic(LatexGramParser.AtomicContext ctx);
	/**
	 * Enter a parse tree produced by the {@code pow}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterPow(LatexGramParser.PowContext ctx);
	/**
	 * Exit a parse tree produced by the {@code pow}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitPow(LatexGramParser.PowContext ctx);
	/**
	 * Enter a parse tree produced by the {@code iMul}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIMul(LatexGramParser.IMulContext ctx);
	/**
	 * Exit a parse tree produced by the {@code iMul}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIMul(LatexGramParser.IMulContext ctx);
	/**
	 * Enter a parse tree produced by the {@code packed}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterPacked(LatexGramParser.PackedContext ctx);
	/**
	 * Exit a parse tree produced by the {@code packed}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitPacked(LatexGramParser.PackedContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexGramParser#pack}.
	 * @param ctx the parse tree
	 */
	void enterPack(LatexGramParser.PackContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexGramParser#pack}.
	 * @param ctx the parse tree
	 */
	void exitPack(LatexGramParser.PackContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexGramParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(LatexGramParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexGramParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(LatexGramParser.AtomContext ctx);
}