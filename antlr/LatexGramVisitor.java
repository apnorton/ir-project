// Generated from LatexGram.g4 by ANTLR 4.5.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link LatexGramParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface LatexGramVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link LatexGramParser#s}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitS(LatexGramParser.SContext ctx);
	/**
	 * Visit a parse tree produced by the {@code div}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDiv(LatexGramParser.DivContext ctx);
	/**
	 * Visit a parse tree produced by the {@code add}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdd(LatexGramParser.AddContext ctx);
	/**
	 * Visit a parse tree produced by the {@code sub}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSub(LatexGramParser.SubContext ctx);
	/**
	 * Visit a parse tree produced by the {@code mul}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMul(LatexGramParser.MulContext ctx);
	/**
	 * Visit a parse tree produced by the {@code atomic}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtomic(LatexGramParser.AtomicContext ctx);
	/**
	 * Visit a parse tree produced by the {@code pow}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPow(LatexGramParser.PowContext ctx);
	/**
	 * Visit a parse tree produced by the {@code iMul}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIMul(LatexGramParser.IMulContext ctx);
	/**
	 * Visit a parse tree produced by the {@code packed}
	 * labeled alternative in {@link LatexGramParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPacked(LatexGramParser.PackedContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexGramParser#pack}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPack(LatexGramParser.PackContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexGramParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(LatexGramParser.AtomContext ctx);
}