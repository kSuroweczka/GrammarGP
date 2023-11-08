// Generated from C:/Users/karol/PycharmProjects/GP-antlr\TinyGP.g4 by ANTLR 4.12.0
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link TinyGPParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface TinyGPVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(TinyGPParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(TinyGPParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#loopStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoopStatement(TinyGPParser.LoopStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#conditionalStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConditionalStatement(TinyGPParser.ConditionalStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#compoundStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCompoundStatement(TinyGPParser.CompoundStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#assignmentStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignmentStatement(TinyGPParser.AssignmentStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#inputStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInputStatement(TinyGPParser.InputStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#outputStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOutputStatement(TinyGPParser.OutputStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#condition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCondition(TinyGPParser.ConditionContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(TinyGPParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm(TinyGPParser.TermContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#factor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFactor(TinyGPParser.FactorContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#functionCall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionCall(TinyGPParser.FunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#argumentList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgumentList(TinyGPParser.ArgumentListContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable(TinyGPParser.VariableContext ctx);
	/**
	 * Visit a parse tree produced by {@link TinyGPParser#boolean}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBoolean(TinyGPParser.BooleanContext ctx);
}