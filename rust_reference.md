## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

  * Auto
  * Light
  * Rust
  * Coal
  * Navy
  * Ayu

# The Rust Reference

[ ](print.html "Print this book") [ ](https://github.com/rust-lang/reference/
"Git repository")

# Introduction

This book is the primary reference for the Rust programming language.

> Note
>
> For known bugs and omissions in this book, see our [GitHub
> issues](https://github.com/rust-lang/reference/issues). If you see a case
> where the compiler behavior and the text here do not agree, file an issue so
> we can think about which is correct.

## Rust releases

Rust has a new language release every six weeks. The first stable release of
the language was Rust 1.0.0, followed by Rust 1.1.0 and so on. Tools (`rustc`,
`cargo`, etc.) and documentation ([Standard library](../std/index.html), this
book, etc.) are released with the language release.

The latest release of this book, matching the latest Rust version, can always
be found at <https://doc.rust-lang.org/reference/>. Prior versions can be
found by adding the Rust version before the “reference” directory. For
example, the Reference for Rust 1.49.0 is located at <https://doc.rust-
lang.org/1.49.0/reference/>.

## What _The Reference_ is not

This book does not serve as an introduction to the language. Background
familiarity with the language is assumed. A separate
[book](../book/index.html) is available to help acquire such background
familiarity.

This book also does not serve as a reference to the [standard
library](../std/index.html) included in the language distribution. Those
libraries are documented separately by extracting documentation attributes
from their source code. Many of the features that one might expect to be
language features are library features in Rust, so what you’re looking for may
be there, not here.

Similarly, this book does not usually document the specifics of `rustc` as a
tool or of Cargo. `rustc` has its own [book](../rustc/index.html). Cargo has a
[book](../cargo/index.html) that contains a
[reference](../cargo/reference/index.html). There are a few pages such as
linkage that still describe how `rustc` works.

This book also only serves as a reference to what is available in stable Rust.
For unstable features being worked on, see the [Unstable
Book](https://doc.rust-lang.org/nightly/unstable-book/).

Rust compilers, including `rustc`, will perform optimizations. The reference
does not specify what optimizations are allowed or disallowed. Instead, think
of the compiled program as a black box. You can only probe by running it,
feeding it input and observing its output. Everything that happens that way
must conform to what the reference says.

## How to use this book

This book does not assume you are reading this book sequentially. Each chapter
generally can be read standalone, but will cross-link to other chapters for
facets of the language they refer to, but do not discuss.

There are two main ways to read this document.

The first is to answer a specific question. If you know which chapter answers
that question, you can jump to that chapter in the table of contents.
Otherwise, you can press `s` or click the magnifying glass on the top bar to
search for keywords related to your question. For example, say you wanted to
know when a temporary value created in a let statement is dropped. If you
didn’t already know that the lifetime of temporaries is defined in the
expressions chapter, you could search “temporary let” and the first search
result will take you to that section.

The second is to generally improve your knowledge of a facet of the language.
In that case, just browse the table of contents until you see something you
want to know more about, and just start reading. If a link looks interesting,
click it, and read about that section.

That said, there is no wrong way to read this book. Read it however you feel
helps you best.

### Conventions

Like all technical books, this book has certain conventions in how it displays
information. These conventions are documented here.

  * Statements that define a term contain that term in _italics_. Whenever that term is used outside of that chapter, it is usually a link to the section that has this definition.

An _example term_ is an example of a term being defined.

  * The main text describes the latest stable edition. Differences to previous editions are separated in edition blocks:

> 2018 Edition differences
>
> Before the 2018 edition, the behavior was this. As of the 2018 edition, the
> behavior is that.

  * Notes that contain useful information about the state of the book or point out useful, but mostly out of scope, information are in note blocks.

> Note
>
> This is an example note.

  * Example blocks show an example that demonstrates some rule or points out some interesting aspect. Some examples may have hidden lines which can be viewed by clicking the eye icon that appears when hovering or tapping the example.

> Example
>
> This is a code example.
>  
>         #![allow(unused)]
>         fn main() {
>         println!("hello world");
>         }

  * Warnings that show unsound behavior in the language or possibly confusing interactions of language features are in a special warning box.

> Warning
>
> This is an example warning.

  * Code snippets inline in the text are inside `<code>` tags.

Longer code examples are in a syntax highlighted box that has controls for
copying, executing, and showing hidden lines in the top right corner.

        
        // This is a hidden line.
        fn main() {
            println!("This is a code example");
        }

All examples are written for the latest edition unless otherwise stated.

  * The grammar and lexical productions are described in the Notation chapter.

[example.rule.label]

  * Rule identifiers appear before each language rule enclosed in square brackets. These identifiers provide a way to refer to and link to a specific rule in the language (e.g.). The rule identifier uses periods to separate sections from most general to most specific (destructors.scope.nesting.function-body for example). On narrow screens, the rule name will collapse to display `[*]`.

The rule name can be clicked to link to that rule.

> Warning
>
> The organization of the rules is currently in flux. For the time being,
> these identifier names are not stable between releases, and links to these
> rules may fail if they are changed. We intend to stabilize these once the
> organization has settled so that links to the rule names will not break
> between releases.

  * Rules that have associated tests will include a `Tests` link below them (on narrow screens, the link is `[T]`). Clicking the link will pop up a list of tests, which can be clicked to view the test. For example, see input.encoding.utf8.

Linking rules to tests is an ongoing effort. See the Test summary chapter for
an overview.

## Contributing

We welcome contributions of all kinds.

You can contribute to this book by opening an issue or sending a pull request
to [the Rust Reference repository](https://github.com/rust-lang/reference/).
If this book does not answer your question, and you think its answer is in
scope of it, please do not hesitate to [file an
issue](https://github.com/rust-lang/reference/issues) or ask about it in the
`t-lang/doc` stream on [Zulip](https://rust-
lang.zulipchat.com/#narrow/stream/237824-t-lang.2Fdoc). Knowing what people
use this book for the most helps direct our attention to making those sections
the best that they can be. And of course, if you see anything that is wrong or
is non-normative but not specifically called out as such, please also [file an
issue](https://github.com/rust-lang/reference/issues).

[notation]

# Notation

[notation.grammar]

## Grammar

[notation.grammar.syntax]

The following notations are used by the _Lexer_ and _Syntax_ grammar snippets:

Notation| Examples| Meaning  
---|---|---  
CAPITAL| KW_IF, INTEGER_LITERAL| A token produced by the lexer  
_ItalicCamelCase_|  _LetStatement_ , _Item_|  A syntactical production  
`string`| `x`, `while`, `*`| The exact character(s)  
x?| `pub`?| An optional item  
x*| _OuterAttribute_ *| 0 or more of x  
x+| _MacroMatch_ +| 1 or more of x  
xa..b| HEX_DIGIT1..6| a to b repetitions of x  
Rule1 Rule2| `fn` _Name_ _Parameters_|  Sequence of rules in order  
|| `u8` | `u16`, Block | Item| Either one or another  
[ ]| [`b` `B`]| Any of the characters listed  
[ - ]| [`a`-`z`]| Any of the characters in the range  
~[ ]| ~[`b` `B`]| Any characters, except those listed  
~`string`| ~`\n`, ~`*/`| Any characters, except this sequence  
( )| (`,` _Parameter_)?| Groups items  
U+xxxx| U+0060| A single unicode character  
<text>| <any ASCII char except CR>| An English description of what should be
matched  
Rule suffix| IDENTIFIER_OR_KEYWORD _except`crate`_| A modification to the
previous rule  
// Comment.| // Single line comment.| A comment extending to the end of the
line.  
  
Sequences have a higher precedence than `|` alternation.

[notation.grammar.string-tables]

### String table productions

Some rules in the grammar — notably unary operators, binary operators, and
keywords — are given in a simplified form: as a listing of printable strings.
These cases form a subset of the rules regarding the token rule, and are
assumed to be the result of a lexical-analysis phase feeding the parser,
driven by a DFA, operating over the disjunction of all such string table
entries.

When such a string in `monospace` font occurs inside the grammar, it is an
implicit reference to a single member of such a string table production. See
tokens for more information.

[notation.grammar.visualizations]

### Grammar visualizations

Below each grammar block is a button to toggle the display of a [syntax
diagram](https://en.wikipedia.org/wiki/Syntax_diagram). A square element is a
non-terminal rule, and a rounded rectangle is a terminal.

# Lexical structure

[input]

# Input format

[input.syntax]

**Lexer**  
CHAR → <a Unicode scalar value>

NUL → U+0000

Show Railroad

CHAR a Unicode scalar value

NUL U+0000

[input.intro]

This chapter describes how a source file is interpreted as a sequence of
tokens.

See Crates and source files for a description of how programs are organised
into files.

[input.encoding]

## Source encoding

[input.encoding.utf8]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/macros/not-utf8.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/macros/not-utf8.rs)
  * [tests/ui/parser/utf16-be-without-bom.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/utf16-be-without-bom.rs)
  * [tests/ui/parser/utf16-le-without-bom.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/utf16-le-without-bom.rs)

Each source file is interpreted as a sequence of Unicode characters encoded in
UTF-8.

[input.encoding.invalid]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/macros/not-utf8.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/macros/not-utf8.rs)

It is an error if the file is not valid UTF-8.

[input.byte-order-mark]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/codemap_tests/utf8-bom.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/codemap_tests/utf8-bom.rs)
  * [tests/ui/json/json-bom-plus-crlf-multifile.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/json/json-bom-plus-crlf-multifile.rs)
  * [tests/ui/json/json-bom-plus-crlf.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/json/json-bom-plus-crlf.rs)

## Byte order mark removal

If the first character in the sequence is `U+FEFF` ([BYTE ORDER
MARK](https://en.wikipedia.org/wiki/Byte_order_mark#UTF-8)), it is removed.

[input.crlf]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/json/json-bom-plus-crlf-multifile.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/json/json-bom-plus-crlf-multifile.rs)
  * [tests/ui/json/json-bom-plus-crlf.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/json/json-bom-plus-crlf.rs)
  * [tests/ui/lexer/lexer-crlf-line-endings-string-literal-doc-comment.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/lexer/lexer-crlf-line-endings-string-literal-doc-comment.rs)

## CRLF normalization

Each pair of characters `U+000D` (CR) immediately followed by `U+000A` (LF) is
replaced by a single `U+000A` (LF). This happens once, not repeatedly, so
after the normalization, there can still exist `U+000D` (CR) immediately
followed by `U+000A` (LF) in the input (e.g. if the raw input contained “CR CR
LF LF”).

Other occurrences of the character `U+000D` (CR) are left in place (they are
treated as whitespace).

[input.shebang]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/parser/shebang/issue-71471-ignore-tidy.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/shebang/issue-71471-ignore-tidy.rs)
  * [tests/ui/parser/shebang/shebang-comment.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/shebang/shebang-comment.rs)
  * [tests/ui/parser/shebang/shebang-empty.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/shebang/shebang-empty.rs)
  * [tests/ui/parser/shebang/shebang-must-start-file.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/shebang/shebang-must-start-file.rs)
  * [tests/ui/parser/shebang/shebang-space.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/shebang/shebang-space.rs)
  * [tests/ui/parser/shebang/valid-shebang.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/shebang/valid-shebang.rs)

## Shebang removal

[input.shebang.intro]

If the remaining sequence begins with the characters `#!`, the characters up
to and including the first `U+000A` (LF) are removed from the sequence.

For example, the first line of the following file would be ignored:

    
    
    #!/usr/bin/env rustx
    
    fn main() {
        println!("Hello!");
    }

[input.shebang.inner-attribute]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/parser/shebang/multiline-attrib.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/shebang/multiline-attrib.rs)
  * [tests/ui/parser/shebang/regular-attrib.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/shebang/regular-attrib.rs)
  * [tests/ui/parser/shebang/shebang-and-attrib.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/shebang/shebang-and-attrib.rs)
  * [tests/ui/parser/shebang/shebang-doc-comment.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/shebang/shebang-doc-comment.rs)
  * [tests/ui/parser/shebang/sneaky-attrib.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/parser/shebang/sneaky-attrib.rs)

As an exception, if the `#!` characters are followed (ignoring intervening
comments or whitespace) by a `[` token, nothing is removed. This prevents an
inner attribute at the start of a source file being removed.

[input.tokenization]

## Tokenization

The resulting sequence of characters is then converted into tokens as
described in the remainder of this chapter.

> Note
>
> The standard library [`include!`](../core/macro.include.html) macro applies
> the following transformations to the file it reads:
>
>   * Byte order mark removal.
>   * CRLF normalization.
>   * Shebang removal when invoked in an item context (as opposed to
> expression or statement contexts).
>

>
> The [`include_str!`](../core/macro.include_str.html) and
> [`include_bytes!`](../core/macro.include_bytes.html) macros do not apply
> these transformations.

[lex.keywords]

# Keywords

Rust divides keywords into three categories:

  * strict
  * reserved
  * weak

[lex.keywords.strict]

## Strict keywords

[lex.keywords.strict.intro]

These keywords can only be used in their correct contexts. They cannot be used
as the names of:

  * Items
  * Variables and function parameters
  * Fields and variants
  * Type parameters
  * Lifetime parameters or loop labels
  * Macros or attributes
  * Macro placeholders
  * Crates

[lex.keywords.strict.list]

The following keywords are in all editions:

  * `_`
  * `as`
  * `async`
  * `await`
  * `break`
  * `const`
  * `continue`
  * `crate`
  * `dyn`
  * `else`
  * `enum`
  * `extern`
  * `false`
  * `fn`
  * `for`
  * `if`
  * `impl`
  * `in`
  * `let`
  * `loop`
  * `match`
  * `mod`
  * `move`
  * `mut`
  * `pub`
  * `ref`
  * `return`
  * `self`
  * `Self`
  * `static`
  * `struct`
  * `super`
  * `trait`
  * `true`
  * `type`
  * `unsafe`
  * `use`
  * `where`
  * `while`

[lex.keywords.strict.edition2018]

> 2018 Edition differences
>
> The following keywords were added in the 2018 edition:
>
>   * `async`
>   * `await`
>   * `dyn`
>

[lex.keywords.reserved]

## Reserved keywords

[lex.keywords.reserved.intro]

These keywords aren’t used yet, but they are reserved for future use. They
have the same restrictions as strict keywords. The reasoning behind this is to
make current programs forward compatible with future versions of Rust by
forbidding them to use these keywords.

[lex.keywords.reserved.list]

  * `abstract`
  * `become`
  * `box`
  * `do`
  * `final`
  * `gen`
  * `macro`
  * `override`
  * `priv`
  * `try`
  * `typeof`
  * `unsized`
  * `virtual`
  * `yield`

[lex.keywords.reserved.edition2018]

> 2018 Edition differences
>
> The `try` keyword was added as a reserved keyword in the 2018 edition.

[lex.keywords.reserved.edition2024]

> 2024 Edition differences
>
> The `gen` keyword was added as a reserved keyword in the 2024 edition.

[lex.keywords.weak]

## Weak keywords

[lex.keywords.weak.intro]

These keywords have special meaning only in certain contexts. For example, it
is possible to declare a variable or method with the name `union`.

  * `'static`
  * `macro_rules`
  * `raw`
  * `safe`
  * `union`

[lex.keywords.weak.macro_rules]

  * `macro_rules` is used to create custom macros.

[lex.keywords.weak.union]

  * `union` is used to declare a union and is only a keyword when used in a union declaration.

[lex.keywords.weak.lifetime-static]

  * `'static` is used for the static lifetime and cannot be used as a generic lifetime parameter or loop label
        
        // error[E0262]: invalid lifetime parameter name: `'static`
        fn invalid_lifetime_parameter<'static>(s: &'static str) -> &'static str { s }
        

[lex.keywords.weak.safe]

  * `safe` is used for functions and statics, which has meaning in external blocks.

[lex.keywords.weak.raw]

  * `raw` is used for raw borrow operators, and is only a keyword when matching a raw borrow operator form (such as `&raw const expr` or `&raw mut expr`).

[lex.keywords.weak.dyn.edition2018]

> 2018 Edition differences
>
> In the 2015 edition, `dyn` is a keyword when used in a type position
> followed by a path that does not start with `::` or `<`, a lifetime, a
> question mark, a `for` keyword or an opening parenthesis.
>
> Beginning in the 2018 edition, `dyn` has been promoted to a strict keyword.

[ident]

# Identifiers

[ident.syntax]

**Lexer**  
IDENTIFIER_OR_KEYWORD → ( XID_Start | _ ) XID_Continue*

XID_Start → <`XID_Start` defined by Unicode>

XID_Continue → <`XID_Continue` defined by Unicode>

RAW_IDENTIFIER → r# IDENTIFIER_OR_KEYWORD

NON_KEYWORD_IDENTIFIER → IDENTIFIER_OR_KEYWORDexcept a strict or reserved
keyword

IDENTIFIER → NON_KEYWORD_IDENTIFIER | RAW_IDENTIFIER

RESERVED_RAW_IDENTIFIER →  
r# ( _ | crate | self | Self | super )not immediately followed by XID_Continue

Show Railroad

IDENTIFIER_OR_KEYWORD XID_Start _ XID_Continue

XID_Start `XID_Start` defined by Unicode

XID_Continue `XID_Continue` defined by Unicode

RAW_IDENTIFIER r# IDENTIFIER_OR_KEYWORD

NON_KEYWORD_IDENTIFIER except a strict or reserved keyword
IDENTIFIER_OR_KEYWORD

IDENTIFIER NON_KEYWORD_IDENTIFIER RAW_IDENTIFIER

RESERVED_RAW_IDENTIFIER r# not immediately followed by XID_Continue _ crate
self Self super

[ident.unicode]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui-fulldeps/lexer/unicode-version.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui-fulldeps/lexer/unicode-version.rs)

Identifiers follow the specification in [Unicode Standard Annex
#31](https://www.unicode.org/reports/tr31/tr31-43.html) for Unicode version
17.0, with the additions described below. Some examples of identifiers:

  * `foo`
  * `_identifier`
  * `r#true`
  * `Москва`
  * `東京`

[ident.profile]

The profile used from UAX #31 is:

  * Start := [`XID_Start`](http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AXID_Start%3A%5D&abb=on&g=&i=), plus the underscore character (U+005F)
  * Continue := [`XID_Continue`](http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AXID_Continue%3A%5D&abb=on&g=&i=)
  * Medial := empty

> Note
>
> Identifiers starting with an underscore are typically used to indicate an
> identifier that is intentionally unused, and will silence the unused warning
> in `rustc`.

[ident.keyword]

Identifiers may not be a strict or reserved keyword without the `r#` prefix
described below in raw identifiers.

[ident.zero-width-chars]

Zero width non-joiner (ZWNJ U+200C) and zero width joiner (ZWJ U+200D)
characters are not allowed in identifiers.

[ident.ascii-limitations]

Identifiers are restricted to the ASCII subset of
[`XID_Start`](http://unicode.org/cldr/utility/list-
unicodeset.jsp?a=%5B%3AXID_Start%3A%5D&abb=on&g=&i=) and
[`XID_Continue`](http://unicode.org/cldr/utility/list-
unicodeset.jsp?a=%5B%3AXID_Continue%3A%5D&abb=on&g=&i=) in the following
situations:

  * `extern crate` declarations (except the AsClause identifier)
  * External crate names referenced in a path
  * Module names loaded from the filesystem without a `path` attribute
  * `no_mangle` attributed items
  * Item names in external blocks

[ident.normalization]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui-fulldeps/lexer/unicode-version.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui-fulldeps/lexer/unicode-version.rs)

## Normalization

Identifiers are normalized using Normalization Form C (NFC) as defined in
[Unicode Standard Annex
#15](https://www.unicode.org/reports/tr15/tr15-57.html). Two identifiers are
equal if their NFC forms are equal.

Procedural and declarative macros receive normalized identifiers in their
input.

[ident.raw]

## Raw identifiers

[ident.raw.intro]

A raw identifier is like a normal identifier, but prefixed by `r#`. (Note that
the `r#` prefix is not included as part of the actual identifier.)

[ident.raw.allowed]

Unlike a normal identifier, a raw identifier may be any strict or reserved
keyword except the ones listed above for `RAW_IDENTIFIER`.

[ident.raw.reserved]

It is an error to use the RESERVED_RAW_IDENTIFIER token.

[comments]

# Comments

[comments.syntax]

**Lexer**  
LINE_COMMENT →  
// ( ~[/ ! LF] | // ) ~LF*   
| //

BLOCK_COMMENT →  
/*  
( ~[* !] | ** | BLOCK_COMMENT_OR_DOC )   
( BLOCK_COMMENT_OR_DOC | ~*/ )*   
*/   
| /**/  
| /***/

INNER_LINE_DOC →  
//! ~[LF CR]*

INNER_BLOCK_DOC →  
/*! ( BLOCK_COMMENT_OR_DOC | ~[*/ CR] )* */

OUTER_LINE_DOC →  
/// ( ~/ ~[LF CR]* )?

OUTER_BLOCK_DOC →  
/**  
( ~* | BLOCK_COMMENT_OR_DOC )   
( BLOCK_COMMENT_OR_DOC | ~[*/ CR] )*   
*/

BLOCK_COMMENT_OR_DOC →  
BLOCK_COMMENT  
| OUTER_BLOCK_DOC  
| INNER_BLOCK_DOC

Show Railroad

LINE_COMMENT // ⚠️ with the exception of / ! LF CHAR // ⚠️ with the exception
of LF CHAR //

BLOCK_COMMENT /* ⚠️ with the exception of * ! CHAR ** BLOCK_COMMENT_OR_DOC
BLOCK_COMMENT_OR_DOC ⚠️ with the exception of */ CHAR */ /**/ /***/

INNER_LINE_DOC //! ⚠️ with the exception of LF CR CHAR

INNER_BLOCK_DOC /*! BLOCK_COMMENT_OR_DOC ⚠️ with the exception of */ CR CHAR
*/

OUTER_LINE_DOC /// ⚠️ with the exception of / CHAR ⚠️ with the exception of LF
CR CHAR

OUTER_BLOCK_DOC /** ⚠️ with the exception of * CHAR BLOCK_COMMENT_OR_DOC
BLOCK_COMMENT_OR_DOC ⚠️ with the exception of */ CR CHAR */

BLOCK_COMMENT_OR_DOC BLOCK_COMMENT OUTER_BLOCK_DOC INNER_BLOCK_DOC

[comments.normal]

## Non-doc comments

Comments follow the general C++ style of line (`//`) and block (`/* ... */`)
comment forms. Nested block comments are supported.

[comments.normal.tokenization]

Non-doc comments are interpreted as a form of whitespace.

[comments.doc]

## Doc comments

[comments.doc.syntax]

Line doc comments beginning with exactly _three_ slashes (`///`), and block
doc comments (`/** ... */`), both outer doc comments, are interpreted as a
special syntax for [`doc` attributes](../rustdoc/the-doc-attribute.html).

[comments.doc.attributes]

That is, they are equivalent to writing `#[doc="..."]` around the body of the
comment, i.e., `/// Foo` turns into `#[doc="Foo"]` and `/** Bar */` turns into
`#[doc="Bar"]`. They must therefore appear before something that accepts an
outer attribute.

[comments.doc.inner-syntax]

Line comments beginning with `//!` and block comments `/*! ... */` are doc
comments that apply to the parent of the comment, rather than the item that
follows.

[comments.doc.inner-attributes]

That is, they are equivalent to writing `#![doc="..."]` around the body of the
comment. `//!` comments are usually used to document modules that occupy a
source file.

[comments.doc.bare-crs]

The character `U+000D` (CR) is not allowed in doc comments.

> Note
>
> It is conventional for doc comments to contain Markdown, as expected by
> `rustdoc`. However, the comment syntax does not respect any internal
> Markdown. `/** `glob = "*/*.rs";` */` terminates the comment at the first
> `*/`, and the remaining code would cause a syntax error. This slightly
> limits the content of block doc comments compared to line doc comments.

> Note
>
> The sequence `U+000D` (CR) immediately followed by `U+000A` (LF) would have
> been previously transformed into a single `U+000A` (LF).

## Examples

    
    
    #![allow(unused)]
    fn main() {
    //! A doc comment that applies to the implicit anonymous module of this crate
    
    pub mod outer_module {
    
        //!  - Inner line doc
        //!! - Still an inner line doc (but with a bang at the beginning)
    
        /*!  - Inner block doc */
        /*!! - Still an inner block doc (but with a bang at the beginning) */
    
        //   - Only a comment
        ///  - Outer line doc (exactly 3 slashes)
        //// - Only a comment
    
        /*   - Only a comment */
        /**  - Outer block doc (exactly) 2 asterisks */
        /*** - Only a comment */
    
        pub mod inner_module {}
    
        pub mod nested_comments {
            /* In Rust /* we can /* nest comments */ */ */
    
            // All three types of block comments can contain or be nested inside
            // any other type:
    
            /*   /* */  /** */  /*! */  */
            /*!  /* */  /** */  /*! */  */
            /**  /* */  /** */  /*! */  */
            pub mod dummy_item {}
        }
    
        pub mod degenerate_cases {
            // empty inner line doc
            //!
    
            // empty inner block doc
            /*!*/
    
            // empty line comment
            //
    
            // empty outer line doc
            ///
    
            // empty block comment
            /**/
    
            pub mod dummy_item {}
    
            // empty 2-asterisk block isn't a doc block, it is a block comment
            /***/
    
        }
    
        /* The next one isn't allowed because outer doc comments
           require an item that will receive the doc */
    
        /// Where is my item?
      mod boo {}
    }
    }

[lex.whitespace]

# Whitespace

[whitespace.syntax]

**Lexer**  
WHITESPACE →  
U+0009 // Horizontal tab, `'\t'`  
| U+000A // Line feed, `'\n'`  
| U+000B // Vertical tab  
| U+000C // Form feed  
| U+000D // Carriage return, `'\r'`  
| U+0020 // Space, `' '`  
| U+0085 // Next line  
| U+200E // Left-to-right mark  
| U+200F // Right-to-left mark  
| U+2028 // Line separator  
| U+2029 // Paragraph separator

TAB → U+0009 // Horizontal tab, `'\t'`

LF → U+000A // Line feed, `'\n'`

CR → U+000D // Carriage return, `'\r'`

Show Railroad

WHITESPACE U+0009 U+000A U+000B U+000C U+000D U+0020 U+0085 U+200E U+200F
U+2028 U+2029

TAB U+0009

LF U+000A

CR U+000D

[lex.whitespace.intro]

Whitespace is any non-empty string containing only characters that have the
[`Pattern_White_Space`](https://www.unicode.org/reports/tr31/) Unicode
property.

[lex.whitespace.token-sep]

Rust is a “free-form” language, meaning that all forms of whitespace serve
only to separate _tokens_ in the grammar, and have no semantic significance.

[lex.whitespace.replacement]

A Rust program has identical meaning if each whitespace element is replaced
with any other legal whitespace element, such as a single space character.

[lex.token]

# Tokens

[lex.token.syntax]

**Lexer**  
Token →  
RESERVED_TOKEN  
| RAW_IDENTIFIER  
| CHAR_LITERAL  
| STRING_LITERAL  
| RAW_STRING_LITERAL  
| BYTE_LITERAL  
| BYTE_STRING_LITERAL  
| RAW_BYTE_STRING_LITERAL  
| C_STRING_LITERAL  
| RAW_C_STRING_LITERAL  
| FLOAT_LITERAL  
| INTEGER_LITERAL  
| LIFETIME_TOKEN  
| PUNCTUATION  
| IDENTIFIER_OR_KEYWORD

Show Railroad

Token RESERVED_TOKEN RAW_IDENTIFIER CHAR_LITERAL STRING_LITERAL
RAW_STRING_LITERAL BYTE_LITERAL BYTE_STRING_LITERAL RAW_BYTE_STRING_LITERAL
C_STRING_LITERAL RAW_C_STRING_LITERAL FLOAT_LITERAL INTEGER_LITERAL
LIFETIME_TOKEN PUNCTUATION IDENTIFIER_OR_KEYWORD

[lex.token.intro]

Tokens are primitive productions in the grammar defined by regular (non-
recursive) languages. Rust source input can be broken down into the following
kinds of tokens:

  * Keywords
  * Identifiers
  * Literals
  * Lifetimes
  * Punctuation
  * Delimiters

Within this documentation’s grammar, “simple” tokens are given in string table
production form, and appear in `monospace` font.

[lex.token.literal]

## Literals

Literals are tokens used in literal expressions.

### Examples

#### Characters and strings

| Example| `#` sets1| Characters| Escapes  
---|---|---|---|---  
Character| `'H'`| 0| All Unicode| Quote & ASCII & Unicode  
String| `"hello"`| 0| All Unicode| Quote & ASCII & Unicode  
Raw string| `r#"hello"#`| <256| All Unicode| `N/A`  
Byte| `b'H'`| 0| All ASCII| Quote & Byte  
Byte string| `b"hello"`| 0| All ASCII| Quote & Byte  
Raw byte string| `br#"hello"#`| <256| All ASCII| `N/A`  
C string| `c"hello"`| 0| All Unicode| Quote & Byte & Unicode  
Raw C string| `cr#"hello"#`| <256| All Unicode| `N/A`  
  
#### ASCII escapes

| Name  
---|---  
`\x41`| 7-bit character code (exactly 2 hex digits, up to 0x7F)  
`\n`| Newline  
`\r`| Carriage return  
`\t`| Tab  
`\\`| Backslash  
`\0`| Null  
  
#### Byte escapes

| Name  
---|---  
`\x7F`| 8-bit character code (exactly 2 hex digits)  
`\n`| Newline  
`\r`| Carriage return  
`\t`| Tab  
`\\`| Backslash  
`\0`| Null  
  
#### Unicode escapes

| Name  
---|---  
`\u{7FFF}`| 24-bit Unicode character code (up to 6 hex digits)  
  
#### Quote escapes

| Name  
---|---  
`\'`| Single quote  
`\"`| Double quote  
  
#### Numbers

Number literals2| Example| Exponentiation  
---|---|---  
Decimal integer| `98_222`| `N/A`  
Hex integer| `0xff`| `N/A`  
Octal integer| `0o77`| `N/A`  
Binary integer| `0b1111_0000`| `N/A`  
Floating-point| `123.0E+77`| `Optional`  
  
[lex.token.literal.suffix]

#### Suffixes

[lex.token.literal.literal.suffix.intro]

A suffix is a sequence of characters following the primary part of a literal
(without intervening whitespace), of the same form as a non-raw identifier or
keyword.

[lex.token.literal.suffix.syntax]

**Lexer**  
SUFFIX → IDENTIFIER_OR_KEYWORDexcept `_`

SUFFIX_NO_E → SUFFIXnot beginning with `e` or `E`

Show Railroad

SUFFIX except `_` IDENTIFIER_OR_KEYWORD

SUFFIX_NO_E not beginning with `e` or `E` SUFFIX

[lex.token.literal.suffix.validity]

Any kind of literal (string, integer, etc) with any suffix is valid as a
token.

A literal token with any suffix can be passed to a macro without producing an
error. The macro itself will decide how to interpret such a token and whether
to produce an error or not. In particular, the `literal` fragment specifier
for by-example macros matches literal tokens with arbitrary suffixes.

    
    
    #![allow(unused)]
    fn main() {
    macro_rules! blackhole { ($tt:tt) => () }
    macro_rules! blackhole_lit { ($l:literal) => () }
    
    blackhole!("string"suffix); // OK
    blackhole_lit!(1suffix); // OK
    }

[lex.token.literal.suffix.parse]

However, suffixes on literal tokens which are interpreted as literal
expressions or patterns are restricted. Any suffixes are rejected on non-
numeric literal tokens, and numeric literal tokens are accepted only with
suffixes from the list below.

Integer| Floating-point  
---|---  
`u8`, `i8`, `u16`, `i16`, `u32`, `i32`, `u64`, `i64`, `u128`, `i128`, `usize`,
`isize`| `f32`, `f64`  
  
### Character and string literals

[lex.token.literal.char]

#### Character literals

[lex.token.literal.char.syntax]

**Lexer**  
CHAR_LITERAL →  
'  
( ~[' \ LF CR TAB] | QUOTE_ESCAPE | ASCII_ESCAPE | UNICODE_ESCAPE )   
' SUFFIX?

QUOTE_ESCAPE → \' | \"

ASCII_ESCAPE →  
\x OCT_DIGIT HEX_DIGIT  
| \n | \r | \t | \\\ | \0

UNICODE_ESCAPE →  
\u{ ( HEX_DIGIT _* )1..6valid hex char value }​3

Show Railroad

CHAR_LITERAL ' ⚠️ with the exception of ' \ LF CR TAB CHAR QUOTE_ESCAPE
ASCII_ESCAPE UNICODE_ESCAPE ' SUFFIX

QUOTE_ESCAPE \' \"

ASCII_ESCAPE \x OCT_DIGIT HEX_DIGIT \n \r \t \\\ \0

UNICODE_ESCAPE \u{ valid hex char value at most 5 more times HEX_DIGIT _ }

[lex.token.literal.char.intro]

A _character literal_ is a single Unicode character enclosed within two
`U+0027` (single-quote) characters, with the exception of `U+0027` itself,
which must be _escaped_ by a preceding `U+005C` character (`\`).

[lex.token.literal.str]

#### String literals

[lex.token.literal.str.syntax]

**Lexer**  
STRING_LITERAL →  
" (  
~[" \ CR]  
| QUOTE_ESCAPE  
| ASCII_ESCAPE  
| UNICODE_ESCAPE  
| STRING_CONTINUE  
)* " SUFFIX?

STRING_CONTINUE → \ LF

Show Railroad

STRING_LITERAL " ⚠️ with the exception of " \ CR CHAR QUOTE_ESCAPE
ASCII_ESCAPE UNICODE_ESCAPE STRING_CONTINUE " SUFFIX

STRING_CONTINUE \ LF

[lex.token.literal.str.intro]

A _string literal_ is a sequence of any Unicode characters enclosed within two
`U+0022` (double-quote) characters, with the exception of `U+0022` itself,
which must be _escaped_ by a preceding `U+005C` character (`\`).

[lex.token.literal.str.linefeed]

Line-breaks, represented by the character `U+000A` (LF), are allowed in string
literals. The character `U+000D` (CR) may not appear in a string literal. When
an unescaped `U+005C` character (`\`) occurs immediately before a line break,
the line break does not appear in the string represented by the token. See
String continuation escapes for details.

[lex.token.literal.char-escape]

#### Character escapes

[lex.token.literal.char-escape.intro]

Some additional _escapes_ are available in either character or non-raw string
literals. An escape starts with a `U+005C` (`\`) and continues with one of the
following forms:

[lex.token.literal.char-escape.ascii]

  * A _7-bit code point escape_ starts with `U+0078` (`x`) and is followed by exactly two _hex digits_ with value up to `0x7F`. It denotes the ASCII character with value equal to the provided hex value. Higher values are not permitted because it is ambiguous whether they mean Unicode code points or byte values.

[lex.token.literal.char-escape.unicode]

  * A _24-bit code point escape_ starts with `U+0075` (`u`) and is followed by up to six _hex digits_ surrounded by braces `U+007B` (`{`) and `U+007D` (`}`). It denotes the Unicode code point equal to the provided hex value. The value must be a valid Unicode scalar value.

[lex.token.literal.char-escape.whitespace]

  * A _whitespace escape_ is one of the characters `U+006E` (`n`), `U+0072` (`r`), or `U+0074` (`t`), denoting the Unicode values `U+000A` (LF), `U+000D` (CR) or `U+0009` (HT) respectively.

[lex.token.literal.char-escape.null]

  * The _null escape_ is the character `U+0030` (`0`) and denotes the Unicode value `U+0000` (NUL).

[lex.token.literal.char-escape.slash]

  * The _backslash escape_ is the character `U+005C` (`\`) which must be escaped in order to denote itself.

[lex.token.literal.str-raw]

#### Raw string literals

[lex.token.literal.str-raw.syntax]

**Lexer**  
RAW_STRING_LITERAL → r RAW_STRING_CONTENT SUFFIX?

RAW_STRING_CONTENT →  
" ( ~CR )* (non-greedy) "  
| # RAW_STRING_CONTENT #

Show Railroad

RAW_STRING_LITERAL r RAW_STRING_CONTENT SUFFIX

RAW_STRING_CONTENT " non-greedy ⚠️ with the exception of CR CHAR " #
RAW_STRING_CONTENT #

[lex.token.literal.str-raw.intro]

Raw string literals do not process any escapes. They start with the character
`U+0072` (`r`), followed by fewer than 256 of the character `U+0023` (`#`) and
a `U+0022` (double-quote) character.

[lex.token.literal.str-raw.body]

The _raw string body_ can contain any sequence of Unicode characters other
than `U+000D` (CR). It is terminated only by another `U+0022` (double-quote)
character, followed by the same number of `U+0023` (`#`) characters that
preceded the opening `U+0022` (double-quote) character.

[lex.token.literal.str-raw.content]

All Unicode characters contained in the raw string body represent themselves,
the characters `U+0022` (double-quote) (except when followed by at least as
many `U+0023` (`#`) characters as were used to start the raw string literal)
or `U+005C` (`\`) do not have any special meaning.

Examples for string literals:

    
    
    #![allow(unused)]
    fn main() {
    "foo"; r"foo";                     // foo
    "\"foo\""; r#""foo""#;             // "foo"
    
    "foo #\"# bar";
    r##"foo #"# bar"##;                // foo #"# bar
    
    "\x52"; "R"; r"R";                 // R
    "\\x52"; r"\x52";                  // \x52
    }

### Byte and byte string literals

[lex.token.byte]

#### Byte literals

[lex.token.byte.syntax]

**Lexer**  
BYTE_LITERAL →  
b' ( ASCII_FOR_CHAR | BYTE_ESCAPE ) ' SUFFIX?

ASCII_FOR_CHAR →  
<any ASCII (i.e. 0x00 to 0x7F) except `'`, `\`, LF, CR, or TAB>

BYTE_ESCAPE →  
\x HEX_DIGIT HEX_DIGIT  
| \n | \r | \t | \\\ | \0 | \' | \"

Show Railroad

BYTE_LITERAL b' ASCII_FOR_CHAR BYTE_ESCAPE ' SUFFIX

ASCII_FOR_CHAR any ASCII (i.e. 0x00 to 0x7F) except `'`, `\\`, LF, CR, or TAB

BYTE_ESCAPE \x HEX_DIGIT HEX_DIGIT \n \r \t \\\ \0 \' \"

[lex.token.byte.intro]

A _byte literal_ is a single ASCII character (in the `U+0000` to `U+007F`
range) or a single _escape_ preceded by the characters `U+0062` (`b`) and
`U+0027` (single-quote), and followed by the character `U+0027`. If the
character `U+0027` is present within the literal, it must be _escaped_ by a
preceding `U+005C` (`\`) character. It is equivalent to a `u8` unsigned 8-bit
integer _number literal_.

[lex.token.str-byte]

#### Byte string literals

[lex.token.str-byte.syntax]

**Lexer**  
BYTE_STRING_LITERAL →  
b" ( ASCII_FOR_STRING | BYTE_ESCAPE | STRING_CONTINUE )* " SUFFIX?

ASCII_FOR_STRING →  
<any ASCII (i.e 0x00 to 0x7F) except `"`, `\`, or CR>

Show Railroad

BYTE_STRING_LITERAL b" ASCII_FOR_STRING BYTE_ESCAPE STRING_CONTINUE " SUFFIX

ASCII_FOR_STRING any ASCII (i.e 0x00 to 0x7F) except `"`, `\\`, or CR

[lex.token.str-byte.intro]

A non-raw _byte string literal_ is a sequence of ASCII characters and
_escapes_ , preceded by the characters `U+0062` (`b`) and `U+0022` (double-
quote), and followed by the character `U+0022`. If the character `U+0022` is
present within the literal, it must be _escaped_ by a preceding `U+005C` (`\`)
character. Alternatively, a byte string literal can be a _raw byte string
literal_ , defined below.

[lex.token.str-byte.linefeed]

Line-breaks, represented by the character `U+000A` (LF), are allowed in byte
string literals. The character `U+000D` (CR) may not appear in a byte string
literal. When an unescaped `U+005C` character (`\`) occurs immediately before
a line break, the line break does not appear in the string represented by the
token. See String continuation escapes for details.

[lex.token.str-byte.escape]

Some additional _escapes_ are available in either byte or non-raw byte string
literals. An escape starts with a `U+005C` (`\`) and continues with one of the
following forms:

[lex.token.str-byte.escape-byte]

  * A _byte escape_ escape starts with `U+0078` (`x`) and is followed by exactly two _hex digits_. It denotes the byte equal to the provided hex value.

[lex.token.str-byte.escape-whitespace]

  * A _whitespace escape_ is one of the characters `U+006E` (`n`), `U+0072` (`r`), or `U+0074` (`t`), denoting the bytes values `0x0A` (ASCII LF), `0x0D` (ASCII CR) or `0x09` (ASCII HT) respectively.

[lex.token.str-byte.escape-null]

  * The _null escape_ is the character `U+0030` (`0`) and denotes the byte value `0x00` (ASCII NUL).

[lex.token.str-byte.escape-slash]

  * The _backslash escape_ is the character `U+005C` (`\`) which must be escaped in order to denote its ASCII encoding `0x5C`.

[lex.token.str-byte-raw]

#### Raw byte string literals

[lex.token.str-byte-raw.syntax]

**Lexer**  
RAW_BYTE_STRING_LITERAL →  
br RAW_BYTE_STRING_CONTENT SUFFIX?

RAW_BYTE_STRING_CONTENT →  
" ASCII_FOR_RAW* (non-greedy) "  
| # RAW_BYTE_STRING_CONTENT #

ASCII_FOR_RAW →  
<any ASCII (i.e. 0x00 to 0x7F) except CR>

Show Railroad

RAW_BYTE_STRING_LITERAL br RAW_BYTE_STRING_CONTENT SUFFIX

RAW_BYTE_STRING_CONTENT " non-greedy ASCII_FOR_RAW " # RAW_BYTE_STRING_CONTENT
#

ASCII_FOR_RAW any ASCII (i.e. 0x00 to 0x7F) except CR

[lex.token.str-byte-raw.intro]

Raw byte string literals do not process any escapes. They start with the
character `U+0062` (`b`), followed by `U+0072` (`r`), followed by fewer than
256 of the character `U+0023` (`#`), and a `U+0022` (double-quote) character.

[lex.token.str-byte-raw.body]

The _raw string body_ can contain any sequence of ASCII characters other than
`U+000D` (CR). It is terminated only by another `U+0022` (double-quote)
character, followed by the same number of `U+0023` (`#`) characters that
preceded the opening `U+0022` (double-quote) character. A raw byte string
literal can not contain any non-ASCII byte.

[lex.token.literal.str-byte-raw.content]

All characters contained in the raw string body represent their ASCII
encoding, the characters `U+0022` (double-quote) (except when followed by at
least as many `U+0023` (`#`) characters as were used to start the raw string
literal) or `U+005C` (`\`) do not have any special meaning.

Examples for byte string literals:

    
    
    #![allow(unused)]
    fn main() {
    b"foo"; br"foo";                     // foo
    b"\"foo\""; br#""foo""#;             // "foo"
    
    b"foo #\"# bar";
    br##"foo #"# bar"##;                 // foo #"# bar
    
    b"\x52"; b"R"; br"R";                // R
    b"\\x52"; br"\x52";                  // \x52
    }

### C string and raw C string literals

[lex.token.str-c]

#### C string literals

[lex.token.str-c.syntax]

**Lexer**  
C_STRING_LITERAL →  
c" (  
~[" \ CR NUL]  
| BYTE_ESCAPEexcept `\0` or `\x00`  
| UNICODE_ESCAPEexcept `\u{0}`, `\u{00}`, …, `\u{000000}`  
| STRING_CONTINUE  
)* " SUFFIX?

Show Railroad

C_STRING_LITERAL c" ⚠️ with the exception of " \ CR NUL CHAR except `\0` or
`\x00` BYTE_ESCAPE except `\u{0}`, `\u{00}`, …, `\u{000000}` UNICODE_ESCAPE
STRING_CONTINUE " SUFFIX

[lex.token.str-c.intro]

A _C string literal_ is a sequence of Unicode characters and _escapes_ ,
preceded by the characters `U+0063` (`c`) and `U+0022` (double-quote), and
followed by the character `U+0022`. If the character `U+0022` is present
within the literal, it must be _escaped_ by a preceding `U+005C` (`\`)
character. Alternatively, a C string literal can be a _raw C string literal_ ,
defined below.

[lex.token.str-c.null]

C strings are implicitly terminated by byte `0x00`, so the C string literal
`c""` is equivalent to manually constructing a `&CStr` from the byte string
literal `b"\x00"`. Other than the implicit terminator, byte `0x00` is not
permitted within a C string.

[lex.token.str-c.linefeed]

Line-breaks, represented by the character `U+000A` (LF), are allowed in C
string literals. The character `U+000D` (CR) may not appear in a C string
literal. When an unescaped `U+005C` character (`\`) occurs immediately before
a line break, the line break does not appear in the string represented by the
token. See String continuation escapes for details.

[lex.token.str-c.escape]

Some additional _escapes_ are available in non-raw C string literals. An
escape starts with a `U+005C` (`\`) and continues with one of the following
forms:

[lex.token.str-c.escape-byte]

  * A _byte escape_ escape starts with `U+0078` (`x`) and is followed by exactly two _hex digits_. It denotes the byte equal to the provided hex value.

[lex.token.str-c.escape-unicode]

  * A _24-bit code point escape_ starts with `U+0075` (`u`) and is followed by up to six _hex digits_ surrounded by braces `U+007B` (`{`) and `U+007D` (`}`). It denotes the Unicode code point equal to the provided hex value, encoded as UTF-8.

[lex.token.str-c.escape-whitespace]

  * A _whitespace escape_ is one of the characters `U+006E` (`n`), `U+0072` (`r`), or `U+0074` (`t`), denoting the bytes values `0x0A` (ASCII LF), `0x0D` (ASCII CR) or `0x09` (ASCII HT) respectively.

[lex.token.str-c.escape-slash]

  * The _backslash escape_ is the character `U+005C` (`\`) which must be escaped in order to denote its ASCII encoding `0x5C`.

[lex.token.str-c.char-unicode]

A C string represents bytes with no defined encoding, but a C string literal
may contain Unicode characters above `U+007F`. Such characters will be
replaced with the bytes of that character’s UTF-8 representation.

The following C string literals are equivalent:

    
    
    #![allow(unused)]
    fn main() {
    c"æ";        // LATIN SMALL LETTER AE (U+00E6)
    c"\u{00E6}";
    c"\xC3\xA6";
    }

[lex.token.str-c.edition2021]

> 2021 Edition differences
>
> C string literals are accepted in the 2021 edition or later. In earlier
> editions the token `c""` is lexed as `c ""`.

[lex.token.str-c-raw]

#### Raw C string literals

[lex.token.str-c-raw.syntax]

**Lexer**  
RAW_C_STRING_LITERAL →  
cr RAW_C_STRING_CONTENT SUFFIX?

RAW_C_STRING_CONTENT →  
" ( ~[CR NUL] )* (non-greedy) "  
| # RAW_C_STRING_CONTENT #

Show Railroad

RAW_C_STRING_LITERAL cr RAW_C_STRING_CONTENT SUFFIX

RAW_C_STRING_CONTENT " non-greedy ⚠️ with the exception of CR NUL CHAR " #
RAW_C_STRING_CONTENT #

[lex.token.str-c-raw.intro]

Raw C string literals do not process any escapes. They start with the
character `U+0063` (`c`), followed by `U+0072` (`r`), followed by fewer than
256 of the character `U+0023` (`#`), and a `U+0022` (double-quote) character.

[lex.token.str-c-raw.body]

The _raw C string body_ can contain any sequence of Unicode characters other
than `U+0000` (NUL) and `U+000D` (CR). It is terminated only by another
`U+0022` (double-quote) character, followed by the same number of `U+0023`
(`#`) characters that preceded the opening `U+0022` (double-quote) character.

[lex.token.str-c-raw.content]

All characters contained in the raw C string body represent themselves in
UTF-8 encoding. The characters `U+0022` (double-quote) (except when followed
by at least as many `U+0023` (`#`) characters as were used to start the raw C
string literal) or `U+005C` (`\`) do not have any special meaning.

[lex.token.str-c-raw.edition2021]

> 2021 Edition differences
>
> Raw C string literals are accepted in the 2021 edition or later. In earlier
> editions the token `cr""` is lexed as `cr ""`, and `cr#""#` is lexed as `cr
> #""#` (which is non-grammatical).

#### Examples for C string and raw C string literals

    
    
    #![allow(unused)]
    fn main() {
    c"foo"; cr"foo";                     // foo
    c"\"foo\""; cr#""foo""#;             // "foo"
    
    c"foo #\"# bar";
    cr##"foo #"# bar"##;                 // foo #"# bar
    
    c"\x52"; c"R"; cr"R";                // R
    c"\\x52"; cr"\x52";                  // \x52
    }

[lex.token.literal.num]

### Number literals

A _number literal_ is either an _integer literal_ or a _floating-point
literal_. The grammar for recognizing the two kinds of literals is mixed.

[lex.token.literal.int]

#### Integer literals

[lex.token.literal.int.syntax]

**Lexer**  
INTEGER_LITERAL →  
( BIN_LITERAL | OCT_LITERAL | HEX_LITERAL | DEC_LITERAL ) SUFFIX_NO_E?

DEC_LITERAL → DEC_DIGIT ( DEC_DIGIT | _ )*

BIN_LITERAL → 0b _* BIN_DIGIT ( BIN_DIGIT | _ )*

OCT_LITERAL → 0o _* OCT_DIGIT ( OCT_DIGIT | _ )*

HEX_LITERAL → 0x _* HEX_DIGIT ( HEX_DIGIT | _ )*

BIN_DIGIT → [0-1]

OCT_DIGIT → [0-7]

DEC_DIGIT → [0-9]

HEX_DIGIT → [0-9 a-f A-F]

Show Railroad

INTEGER_LITERAL BIN_LITERAL OCT_LITERAL HEX_LITERAL DEC_LITERAL SUFFIX_NO_E

DEC_LITERAL DEC_DIGIT DEC_DIGIT _

BIN_LITERAL 0b _ BIN_DIGIT BIN_DIGIT _

OCT_LITERAL 0o _ OCT_DIGIT OCT_DIGIT _

HEX_LITERAL 0x _ HEX_DIGIT HEX_DIGIT _

BIN_DIGIT 0-1

OCT_DIGIT 0-7

DEC_DIGIT 0-9

HEX_DIGIT 0-9 a-f A-F

[lex.token.literal.int.kind]

An _integer literal_ has one of four forms:

[lex.token.literal.int.kind-dec]

  * A _decimal literal_ starts with a _decimal digit_ and continues with any mixture of _decimal digits_ and _underscores_.

[lex.token.literal.int.kind-hex]

  * A _hex literal_ starts with the character sequence `U+0030` `U+0078` (`0x`) and continues as any mixture (with at least one digit) of hex digits and underscores.

[lex.token.literal.int.kind-oct]

  * An _octal literal_ starts with the character sequence `U+0030` `U+006F` (`0o`) and continues as any mixture (with at least one digit) of octal digits and underscores.

[lex.token.literal.int.kind-bin]

  * A _binary literal_ starts with the character sequence `U+0030` `U+0062` (`0b`) and continues as any mixture (with at least one digit) of binary digits and underscores.

[lex.token.literal.int.restriction]

Like any literal, an integer literal may be followed (immediately, without any
spaces) by a suffix as described above. The suffix may not begin with `e` or
`E`, as that would be interpreted as the exponent of a floating-point literal.
See Integer literal expressions for the effect of these suffixes.

Examples of integer literals which are accepted as literal expressions:

    
    
    #![allow(unused)]
    fn main() {
    #![allow(overflowing_literals)]
    123;
    123i32;
    123u32;
    123_u32;
    
    0xff;
    0xff_u8;
    0x01_f32; // integer 7986, not floating-point 1.0
    0x01_e3;  // integer 483, not floating-point 1000.0
    
    0o70;
    0o70_i16;
    
    0b1111_1111_1001_0000;
    0b1111_1111_1001_0000i64;
    0b________1;
    
    0usize;
    
    // These are too big for their type, but are accepted as literal expressions.
    128_i8;
    256_u8;
    
    // This is an integer literal, accepted as a floating-point literal expression.
    5f32;
    }

Note that `-1i8`, for example, is analyzed as two tokens: `-` followed by
`1i8`.

Examples of integer literals which are not accepted as literal expressions:

    
    
    #![allow(unused)]
    fn main() {
    #[cfg(false)] {
    0invalidSuffix;
    123AFB43;
    0b010a;
    0xAB_CD_EF_GH;
    0b1111_f32;
    }
    }

[lex.token.literal.int.tuple-field]

#### Tuple index

[lex.token.literal.int.tuple-field.syntax]

**Lexer**  
TUPLE_INDEX → DEC_LITERAL | BIN_LITERAL | OCT_LITERAL | HEX_LITERAL

Show Railroad

TUPLE_INDEX DEC_LITERAL BIN_LITERAL OCT_LITERAL HEX_LITERAL

[lex.token.literal.int.tuple-field.intro]

A tuple index is used to refer to the fields of tuples, tuple structs, and
tuple enum variants.

[lex.token.literal.int.tuple-field.eq]

Tuple indices are compared with the literal token directly. Tuple indices
start with `0` and each successive index increments the value by `1` as a
decimal value. Thus, only decimal values will match, and the value must not
have any extra `0` prefix characters.

Tuple indices may not include any suffixes (such as `usize`).

    
    
    #![allow(unused)]
    fn main() {
    let example = ("dog", "cat", "horse");
    let dog = example.0;
    let cat = example.1;
    // The following examples are invalid.
    let cat = example.01;  // ERROR no field named `01`
    let horse = example.0b10;  // ERROR no field named `0b10`
    let unicorn = example.0usize; // ERROR suffixes on a tuple index are invalid
    let underscore = example.0_0; // ERROR no field `0_0` on type `(&str, &str, &str)`
    }

[lex.token.literal.float]

#### Floating-point literals

[lex.token.literal.float.syntax]

**Lexer**  
FLOAT_LITERAL →  
DEC_LITERAL ( . DEC_LITERAL )? FLOAT_EXPONENT SUFFIX?  
| DEC_LITERAL . DEC_LITERAL SUFFIX_NO_E?  
| DEC_LITERAL .not immediately followed by `.`, `_` or an XID_Start character

FLOAT_EXPONENT →  
( e | E ) ( + | - )? _* DEC_DIGIT ( DEC_DIGIT | _ )*

Show Railroad

FLOAT_LITERAL DEC_LITERAL . DEC_LITERAL FLOAT_EXPONENT SUFFIX DEC_LITERAL .
DEC_LITERAL SUFFIX_NO_E DEC_LITERAL not immediately followed by `.`, `_` or an
XID_Start character .

FLOAT_EXPONENT e E + - _ DEC_DIGIT DEC_DIGIT _

[lex.token.literal.float.form]

A _floating-point literal_ has one of two forms:

  * A _decimal literal_ followed by a period character `U+002E` (`.`). This is optionally followed by another decimal literal, with an optional _exponent_.
  * A single _decimal literal_ followed by an _exponent_.

[lex.token.literal.float.suffix]

Like integer literals, a floating-point literal may be followed by a suffix,
so long as the pre-suffix part does not end with `U+002E` (`.`). The suffix
may not begin with `e` or `E` if the literal does not include an exponent. See
Floating-point literal expressions for the effect of these suffixes.

Examples of floating-point literals which are accepted as literal expressions:

    
    
    #![allow(unused)]
    fn main() {
    123.0f64;
    0.1f64;
    0.1f32;
    12E+99_f64;
    let x: f64 = 2.;
    }

This last example is different because it is not possible to use the suffix
syntax with a floating point literal ending in a period. `2.f64` would attempt
to call a method named `f64` on `2`.

Note that `-1.0`, for example, is analyzed as two tokens: `-` followed by
`1.0`.

Examples of floating-point literals which are not accepted as literal
expressions:

    
    
    #![allow(unused)]
    fn main() {
    #[cfg(false)] {
    2.0f80;
    2e5f80;
    2e5e6;
    2.0e5e6;
    1.3e10u64;
    }
    }

[lex.token.literal.reserved]

#### Reserved forms similar to number literals

[lex.token.literal.reserved.syntax]

**Lexer**  
RESERVED_NUMBER →  
BIN_LITERAL [2-9]  
| OCT_LITERAL [8-9]  
| ( BIN_LITERAL | OCT_LITERAL | HEX_LITERAL ) .not immediately followed by `.`, `_` or an XID_Start character   
| ( BIN_LITERAL | OCT_LITERAL ) ( e | E )   
| 0b _* <end of input or not BIN_DIGIT>  
| 0o _* <end of input or not OCT_DIGIT>  
| 0x _* <end of input or not HEX_DIGIT>  
| DEC_LITERAL ( . DEC_LITERAL )? ( e | E ) ( + | - )? <end of input or not DEC_DIGIT>

Show Railroad

RESERVED_NUMBER BIN_LITERAL 2-9 OCT_LITERAL 8-9 BIN_LITERAL OCT_LITERAL
HEX_LITERAL not immediately followed by `.`, `_` or an XID_Start character .
BIN_LITERAL OCT_LITERAL e E 0b _ end of input or not BIN_DIGIT 0o _ end of
input or not OCT_DIGIT 0x _ end of input or not HEX_DIGIT DEC_LITERAL .
DEC_LITERAL e E + - end of input or not DEC_DIGIT

[lex.token.literal.reserved.intro]

The following lexical forms similar to number literals are _reserved forms_.
Due to the possible ambiguity these raise, they are rejected by the tokenizer
instead of being interpreted as separate tokens.

[lex.token.literal.reserved.out-of-range]

  * An unsuffixed binary or octal literal followed, without intervening whitespace, by a decimal digit out of the range for its radix.

[lex.token.literal.reserved.period]

  * An unsuffixed binary, octal, or hexadecimal literal followed, without intervening whitespace, by a period character (with the same restrictions on what follows the period as for floating-point literals).

[lex.token.literal.reserved.exp]

  * An unsuffixed binary or octal literal followed, without intervening whitespace, by the character `e` or `E`.

[lex.token.literal.reserved.empty-with-radix]

  * Input which begins with one of the radix prefixes but is not a valid binary, octal, or hexadecimal literal (because it contains no digits).

[lex.token.literal.reserved.empty-exp]

  * Input which has the form of a floating-point literal with no digits in the exponent.

Examples of reserved forms:

    
    
    #![allow(unused)]
    fn main() {
    0b0102;  // this is not `0b010` followed by `2`
    0o1279;  // this is not `0o127` followed by `9`
    0x80.0;  // this is not `0x80` followed by `.` and `0`
    0b101e;  // this is not a suffixed literal, or `0b101` followed by `e`
    0b;      // this is not an integer literal, or `0` followed by `b`
    0b_;     // this is not an integer literal, or `0` followed by `b_`
    2e;      // this is not a floating-point literal, or `2` followed by `e`
    2.0e;    // this is not a floating-point literal, or `2.0` followed by `e`
    2em;     // this is not a suffixed literal, or `2` followed by `em`
    2.0em;   // this is not a suffixed literal, or `2.0` followed by `em`
    }

[lex.token.life]

## Lifetimes and loop labels

[lex.token.life.syntax]

**Lexer**  
LIFETIME_TOKEN →  
RAW_LIFETIME  
| ' IDENTIFIER_OR_KEYWORDnot immediately followed by `'`

LIFETIME_OR_LABEL →  
RAW_LIFETIME  
| ' NON_KEYWORD_IDENTIFIERnot immediately followed by `'`

RAW_LIFETIME →  
'r# IDENTIFIER_OR_KEYWORDnot immediately followed by `'`

RESERVED_RAW_LIFETIME → 'r# ( _ | crate | self | Self | super )not immediately followed by `'`

Show Railroad

LIFETIME_TOKEN RAW_LIFETIME ' not immediately followed by `'`
IDENTIFIER_OR_KEYWORD

LIFETIME_OR_LABEL RAW_LIFETIME ' not immediately followed by `'`
NON_KEYWORD_IDENTIFIER

RAW_LIFETIME 'r# not immediately followed by `'` IDENTIFIER_OR_KEYWORD

RESERVED_RAW_LIFETIME 'r# not immediately followed by `'` _ crate self Self
super

[lex.token.life.intro]

Lifetime parameters and loop labels use LIFETIME_OR_LABEL tokens. Any
LIFETIME_TOKEN will be accepted by the lexer, and for example, can be used in
macros.

[lex.token.life.raw.intro]

A raw lifetime is like a normal lifetime, but its identifier is prefixed by
`r#`. (Note that the `r#` prefix is not included as part of the actual
lifetime.)

[lex.token.life.raw.allowed]

Unlike a normal lifetime, a raw lifetime may be any strict or reserved keyword
except the ones listed above for `RAW_LIFETIME`.

[lex.token.life.raw.reserved]

It is an error to use the RESERVED_RAW_LIFETIME token.

[lex.token.life.raw.edition2021]

> 2021 Edition differences
>
> Raw lifetimes are accepted in the 2021 edition or later. In earlier editions
> the token `'r#lt` is lexed as `'r # lt`.

[lex.token.punct]

## Punctuation

[lex.token.punct.intro]

Punctuation tokens are used as operators, separators, and other parts of the
grammar.

[lex.token.punct.syntax]

**Lexer**  
PUNCTUATION →  
...  
| ..=  
| <<=  
| >>=  
| !=  
| %=  
| &&  
| &=  
| *=  
| +=  
| -=  
| ->  
| ..  
| /=  
| ::  
| <-  
| <<  
| <=  
| ==  
| =>  
| >=  
| >>  
| >  
| ^=  
| |=  
| ||  
| !  
| #  
| $  
| %  
| &  
| (  
| )  
| *  
| +  
| ,  
| -  
| .  
| /  
| :  
| ;  
| <  
| =  
| ?  
| @  
| [  
| ]  
| ^  
| {  
| |   
| }  
| ~

Show Railroad

PUNCTUATION ... ..= <<= >>= != %= && &= *= += -= -> .. /= :: <- << <= == => >= >> > ^= |= || ! # $ % & ( ) * + , - . / : ; < = ? @ [ ] ^ { | } ~

> Note
>
> See the syntax index for links to how punctuation characters are used.

[lex.token.delim]

## Delimiters

Bracket punctuation is used in various parts of the grammar. An open bracket
must always be paired with a close bracket. Brackets and the tokens within
them are referred to as “token trees” in macros. The three types of brackets
are:

Bracket| Type  
---|---  
`{` `}`| Curly braces  
`[` `]`| Square brackets  
`(` `)`| Parentheses  
  
[lex.token.reserved]

## Reserved tokens

[lex.token.reserved.intro]

Several token forms are reserved for future use or to avoid confusion. It is
an error for the source input to match one of these forms.

[lex.token.reserved.syntax]

**Lexer**  
RESERVED_TOKEN →  
RESERVED_GUARDED_STRING_LITERAL  
| RESERVED_NUMBER  
| RESERVED_POUNDS  
| RESERVED_RAW_IDENTIFIER  
| RESERVED_RAW_LIFETIME  
| RESERVED_TOKEN_DOUBLE_QUOTE  
| RESERVED_TOKEN_LIFETIME  
| RESERVED_TOKEN_POUND  
| RESERVED_TOKEN_SINGLE_QUOTE

Show Railroad

RESERVED_TOKEN RESERVED_GUARDED_STRING_LITERAL RESERVED_NUMBER RESERVED_POUNDS
RESERVED_RAW_IDENTIFIER RESERVED_RAW_LIFETIME RESERVED_TOKEN_DOUBLE_QUOTE
RESERVED_TOKEN_LIFETIME RESERVED_TOKEN_POUND RESERVED_TOKEN_SINGLE_QUOTE

[lex.token.reserved-prefix]

## Reserved prefixes

[lex.token.reserved-prefix.syntax]

**Lexer**  
RESERVED_TOKEN_DOUBLE_QUOTE →  
IDENTIFIER_OR_KEYWORDexcept `b` or `c` or `r` or `br` or `cr` "

RESERVED_TOKEN_SINGLE_QUOTE →  
IDENTIFIER_OR_KEYWORDexcept `b` '

RESERVED_TOKEN_POUND →  
IDENTIFIER_OR_KEYWORDexcept `r` or `br` or `cr` #

RESERVED_TOKEN_LIFETIME →  
' IDENTIFIER_OR_KEYWORDexcept `r` #

Show Railroad

RESERVED_TOKEN_DOUBLE_QUOTE except `b` or `c` or `r` or `br` or `cr`
IDENTIFIER_OR_KEYWORD "

RESERVED_TOKEN_SINGLE_QUOTE except `b` IDENTIFIER_OR_KEYWORD '

RESERVED_TOKEN_POUND except `r` or `br` or `cr` IDENTIFIER_OR_KEYWORD #

RESERVED_TOKEN_LIFETIME ' except `r` IDENTIFIER_OR_KEYWORD #

[lex.token.reserved-prefix.intro]

Some lexical forms known as _reserved prefixes_ are reserved for future use.

[lex.token.reserved-prefix.id]

Source input which would otherwise be lexically interpreted as a non-raw
identifier (or a keyword) which is immediately followed by a `#`, `'`, or `"`
character (without intervening whitespace) is identified as a reserved prefix.

[lex.token.reserved-prefix.raw-token]

Note that raw identifiers, raw string literals, and raw byte string literals
may contain a `#` character but are not interpreted as containing a reserved
prefix.

[lex.token.reserved-prefix.strings]

Similarly the `r`, `b`, `br`, `c`, and `cr` prefixes used in raw string
literals, byte literals, byte string literals, raw byte string literals, C
string literals, and raw C string literals are not interpreted as reserved
prefixes.

[lex.token.reserved-prefix.life]

Source input which would otherwise be lexically interpreted as a non-raw
lifetime (or a keyword) which is immediately followed by a `#` character
(without intervening whitespace) is identified as a reserved lifetime prefix.

[lex.token.reserved-prefix.edition2021]

> 2021 Edition differences
>
> Starting with the 2021 edition, reserved prefixes are reported as an error
> by the lexer (in particular, they cannot be passed to macros).
>
> Before the 2021 edition, reserved prefixes are accepted by the lexer and
> interpreted as multiple tokens (for example, one token for the identifier or
> keyword, followed by a `#` token).
>
> Examples accepted in all editions:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     macro_rules! lexes {($($_:tt)*) => {}}
>     lexes!{a #foo}
>     lexes!{continue 'foo}
>     lexes!{match "..." {}}
>     lexes!{r#let#foo}         // three tokens: r#let # foo
>     lexes!{'prefix #lt}
>     }
>
> Examples accepted before the 2021 edition but rejected later:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     macro_rules! lexes {($($_:tt)*) => {}}
>     lexes!{a#foo}
>     lexes!{continue'foo}
>     lexes!{match"..." {}}
>     lexes!{'prefix#lt}
>     }

[lex.token.reserved-guards]

## Reserved guards

[lex.token.reserved-guards.syntax]

**Lexer**  
RESERVED_GUARDED_STRING_LITERAL → #+ STRING_LITERAL

RESERVED_POUNDS → #2..

Show Railroad

RESERVED_GUARDED_STRING_LITERAL # STRING_LITERAL

RESERVED_POUNDS # #

[lex.token.reserved-guards.intro]

The reserved guards are syntax reserved for future use, and will generate a
compile error if used.

[lex.token.reserved-guards.string-literal]

The _reserved guarded string literal_ is a token of one or more `U+0023` (`#`)
immediately followed by a STRING_LITERAL.

[lex.token.reserved-guards.pounds]

The _reserved pounds_ is a token of two or more `U+0023` (`#`).

[lex.token.reserved-guards.edition2024]

> 2024 Edition differences
>
> Before the 2024 edition, reserved guards are accepted by the lexer and
> interpreted as multiple tokens. For example, the `#"foo"#` form is
> interpreted as three tokens. `##` is interpreted as two tokens.

* * *

  1. The number of `#`s on each side of the same literal must be equivalent. ↩

  2. All number literals allow `_` as a visual separator: `1_234.0E+18f64` ↩

  3. See lex.token.literal.char-escape.unicode. ↩

[macro]

# Macros

[macro.intro]

The functionality and syntax of Rust can be extended with custom definitions
called macros. They are given names, and invoked through a consistent syntax:
`some_extension!(...)`.

There are two ways to define new macros:

  * Macros by Example define new syntax in a higher-level, declarative way.
  * Procedural Macros define function-like macros, custom derives, and custom attributes using functions that operate on input tokens.

[macro.invocation]

## Macro invocation

[macro.invocation.syntax]

**Syntax**  
MacroInvocation →  
SimplePath ! DelimTokenTree

DelimTokenTree →  
( TokenTree* )  
| [ TokenTree* ]  
| { TokenTree* }

TokenTree →  
Tokenexcept delimiters | DelimTokenTree

MacroInvocationSemi →  
SimplePath ! ( TokenTree* ) ;  
| SimplePath ! [ TokenTree* ] ;  
| SimplePath ! { TokenTree* }

Show Railroad

MacroInvocation SimplePath ! DelimTokenTree

DelimTokenTree ( TokenTree ) [ TokenTree ] { TokenTree }

TokenTree except delimiters Token DelimTokenTree

MacroInvocationSemi SimplePath ! ( TokenTree ) ; SimplePath ! [ TokenTree ] ;
SimplePath ! { TokenTree }

[macro.invocation.intro]

A macro invocation expands a macro at compile time and replaces the invocation
with the result of the macro. Macros may be invoked in the following
situations:

[macro.invocation.expr]

  * Expressions and statements

[macro.invocation.pattern]

  * Patterns

[macro.invocation.type]

  * Types

[macro.invocation.item]

  * Items including associated items

[macro.invocation.nested]

  * `macro_rules` transcribers

[macro.invocation.extern]

  * External blocks

[macro.invocation.item-statement]

When used as an item or a statement, the MacroInvocationSemi form is used
where a semicolon is required at the end when not using curly braces.
Visibility qualifiers are never allowed before a macro invocation or
`macro_rules` definition.

    
    
    #![allow(unused)]
    fn main() {
    // Used as an expression.
    let x = vec![1,2,3];
    
    // Used as a statement.
    println!("Hello!");
    
    // Used in a pattern.
    macro_rules! pat {
        ($i:ident) => (Some($i))
    }
    
    if let pat!(x) = Some(1) {
        assert_eq!(x, 1);
    }
    
    // Used in a type.
    macro_rules! Tuple {
        { $A:ty, $B:ty } => { ($A, $B) };
    }
    
    type N2 = Tuple!(i32, i32);
    
    // Used as an item.
    use std::cell::RefCell;
    thread_local!(static FOO: RefCell<u32> = RefCell::new(1));
    
    // Used as an associated item.
    macro_rules! const_maker {
        ($t:ty, $v:tt) => { const CONST: $t = $v; };
    }
    trait T {
        const_maker!{i32, 7}
    }
    
    // Macro calls within macros.
    macro_rules! example {
        () => { println!("Macro call in a macro!") };
    }
    // Outer macro `example` is expanded, then inner macro `println` is expanded.
    example!();
    }

[macro.invocation.name-resolution]

Macros invocations can be resolved via two kinds of scopes:

  * Textual Scope 
    * Textual scope `macro_rules`
  * Path-based scope 
    * Path-based scope `macro_rules`
    * Procedural macros

[macro.decl]

# Macros by example

[macro.decl.syntax]

**Syntax**  
MacroRulesDefinition →  
macro_rules ! IDENTIFIER MacroRulesDef

MacroRulesDef →  
( MacroRules ) ;  
| [ MacroRules ] ;  
| { MacroRules }

MacroRules →  
MacroRule ( ; MacroRule )* ;?

MacroRule →  
MacroMatcher => MacroTranscriber

MacroMatcher →  
( MacroMatch* )  
| [ MacroMatch* ]  
| { MacroMatch* }

MacroMatch →  
Tokenexcept `$` and delimiters  
| MacroMatcher  
| $ ( IDENTIFIER_OR_KEYWORDexcept `crate` | RAW_IDENTIFIER ) : MacroFragSpec   
| $ ( MacroMatch+ ) MacroRepSep? MacroRepOp

MacroFragSpec →  
block | expr | expr_2021 | ident | item | lifetime | literal   
| meta | pat | pat_param | path | stmt | tt | ty | vis

MacroRepSep → Tokenexcept delimiters and MacroRepOp

MacroRepOp → * | + | ?

MacroTranscriber → DelimTokenTree

Show Railroad

MacroRulesDefinition macro_rules ! IDENTIFIER MacroRulesDef

MacroRulesDef ( MacroRules ) ; [ MacroRules ] ; { MacroRules }

MacroRules MacroRule ; MacroRule ;

MacroRule MacroMatcher => MacroTranscriber

MacroMatcher ( MacroMatch ) [ MacroMatch ] { MacroMatch }

MacroMatch except `$` and delimiters Token MacroMatcher $ except `crate`
IDENTIFIER_OR_KEYWORD RAW_IDENTIFIER : MacroFragSpec $ ( MacroMatch )
MacroRepSep MacroRepOp

MacroFragSpec block expr expr_2021 ident item lifetime literal meta pat
pat_param path stmt tt ty vis

MacroRepSep except delimiters and MacroRepOp Token

MacroRepOp * + ?

MacroTranscriber DelimTokenTree

[macro.decl.intro]

`macro_rules` allows users to define syntax extension in a declarative way. We
call such extensions “macros by example” or simply “macros”.

Each macro by example has a name, and one or more _rules_. Each rule has two
parts: a _matcher_ , describing the syntax that it matches, and a
_transcriber_ , describing the syntax that will replace a successfully matched
invocation. Both the matcher and the transcriber must be surrounded by
delimiters. Macros can expand to expressions, statements, items (including
traits, impls, and foreign items), types, or patterns.

[macro.decl.transcription]

## Transcribing

[macro.decl.transcription.intro]

When a macro is invoked, the macro expander looks up macro invocations by
name, and tries each macro rule in turn. It transcribes the first successful
match; if this results in an error, then future matches are not tried.

[macro.decl.transcription.lookahead]

When matching, no lookahead is performed; if the compiler cannot unambiguously
determine how to parse the macro invocation one token at a time, then it is an
error. In the following example, the compiler does not look ahead past the
identifier to see if the following token is a `)`, even though that would
allow it to parse the invocation unambiguously:

    
    
    #![allow(unused)]
    fn main() {
    macro_rules! ambiguity {
        ($($i:ident)* $j:ident) => { };
    }
    
    ambiguity!(error); // Error: local ambiguity
    }

[macro.decl.transcription.syntax]

In both the matcher and the transcriber, the `$` token is used to invoke
special behaviours from the macro engine (described below in Metavariables and
Repetitions). Tokens that aren’t part of such an invocation are matched and
transcribed literally, with one exception. The exception is that the outer
delimiters for the matcher will match any pair of delimiters. Thus, for
instance, the matcher `(())` will match `{()}` but not `{{}}`. The character
`$` cannot be matched or transcribed literally.

[macro.decl.transcription.fragment]

### Forwarding a matched fragment

When forwarding a matched fragment to another macro-by-example, matchers in
the second macro will see an opaque AST of the fragment type. The second macro
can’t use literal tokens to match the fragments in the matcher, only a
fragment specifier of the same type. The `ident`, `lifetime`, and `tt`
fragment types are an exception, and _can_ be matched by literal tokens. The
following illustrates this restriction:

    
    
    #![allow(unused)]
    fn main() {
    macro_rules! foo {
        ($l:expr) => { bar!($l); }
    // ERROR:               ^^ no rules expected this token in macro call
    }
    
    macro_rules! bar {
        (3) => {}
    }
    
    foo!(3);
    }

The following illustrates how tokens can be directly matched after matching a
`tt` fragment:

    
    
    #![allow(unused)]
    fn main() {
    // compiles OK
    macro_rules! foo {
        ($l:tt) => { bar!($l); }
    }
    
    macro_rules! bar {
        (3) => {}
    }
    
    foo!(3);
    }

[macro.decl.meta]

## Metavariables

[macro.decl.meta.intro]

In the matcher, `$` _name_ `:` _fragment-specifier_ matches a Rust syntax
fragment of the kind specified and binds it to the metavariable `$`_name_.

[macro.decl.meta.specifier]

Valid fragment specifiers are:

  * `block`: a BlockExpression
  * `expr`: an Expression
  * `expr_2021`: an Expression except UnderscoreExpression and ConstBlockExpression (see macro.decl.meta.edition2024)
  * `ident`: an IDENTIFIER_OR_KEYWORD except `_`, RAW_IDENTIFIER, or `$crate`
  * `item`: an Item
  * `lifetime`: a LIFETIME_TOKEN
  * `literal`: matches `-`?LiteralExpression
  * `meta`: an Attr, the contents of an attribute
  * `pat`: a Pattern (see macro.decl.meta.edition2021)
  * `pat_param`: a PatternNoTopAlt
  * `path`: a TypePath style path
  * `stmt`: a Statement without the trailing semicolon (except for item statements that require semicolons)
  * `tt`: a TokenTree (a single token or tokens in matching delimiters `()`, `[]`, or `{}`)
  * `ty`: a Type
  * `vis`: a possibly empty Visibility qualifier

[macro.decl.meta.transcription]

In the transcriber, metavariables are referred to simply by `$`_name_ , since
the fragment kind is specified in the matcher. Metavariables are replaced with
the syntax element that matched them. Metavariables can be transcribed more
than once or not at all.

[macro.decl.meta.dollar-crate]

The keyword metavariable `$crate` can be used to refer to the current crate.

[macro.decl.meta.edition2021]

> 2021 Edition differences
>
> Starting with the 2021 edition, `pat` fragment-specifiers match top-level
> or-patterns (that is, they accept Pattern).
>
> Before the 2021 edition, they match exactly the same fragments as
> `pat_param` (that is, they accept PatternNoTopAlt).
>
> The relevant edition is the one in effect for the `macro_rules!` definition.

[macro.decl.meta.edition2024]

> 2024 Edition differences
>
> Before the 2024 edition, `expr` fragment specifiers do not match
> UnderscoreExpression or ConstBlockExpression at the top level. They are
> allowed within subexpressions.
>
> The `expr_2021` fragment specifier exists to maintain backwards
> compatibility with editions before 2024.

[macro.decl.repetition]

## Repetitions

[macro.decl.repetition.intro]

In both the matcher and transcriber, repetitions are indicated by placing the
tokens to be repeated inside `$(`…`)`, followed by a repetition operator,
optionally with a separator token between.

[macro.decl.repetition.separator]

The separator token can be any token other than a delimiter or one of the
repetition operators, but `;` and `,` are the most common. For instance, `$(
$i:ident ),*` represents any number of identifiers separated by commas. Nested
repetitions are permitted.

[macro.decl.repetition.operators]

The repetition operators are:

  * `*` — indicates any number of repetitions.
  * `+` — indicates any number but at least one.
  * `?` — indicates an optional fragment with zero or one occurrence.

[macro.decl.repetition.optional-restriction]

Since `?` represents at most one occurrence, it cannot be used with a
separator.

[macro.decl.repetition.fragment]

The repeated fragment both matches and transcribes to the specified number of
the fragment, separated by the separator token. Metavariables are matched to
every repetition of their corresponding fragment. For instance, the `$(
$i:ident ),*` example above matches `$i` to all of the identifiers in the
list.

During transcription, additional restrictions apply to repetitions so that the
compiler knows how to expand them properly:

  1. A metavariable must appear in exactly the same number, kind, and nesting order of repetitions in the transcriber as it did in the matcher. So for the matcher `$( $i:ident ),*`, the transcribers `=> { $i }`, `=> { $( $( $i )* )* }`, and `=> { $( $i )+ }` are all illegal, but `=> { $( $i );* }` is correct and replaces a comma-separated list of identifiers with a semicolon-separated list.
  2. Each repetition in the transcriber must contain at least one metavariable to decide how many times to expand it. If multiple metavariables appear in the same repetition, they must be bound to the same number of fragments. For instance, `( $( $i:ident ),* ; $( $j:ident ),* ) => (( $( ($i,$j) ),* ))` must bind the same number of `$i` fragments as `$j` fragments. This means that invoking the macro with `(a, b, c; d, e, f)` is legal and expands to `((a,d), (b,e), (c,f))`, but `(a, b, c; d, e)` is illegal because it does not have the same number. This requirement applies to every layer of nested repetitions.

[macro.decl.scope]

## Scoping, exporting, and importing

[macro.decl.scope.intro]

For historical reasons, the scoping of macros by example does not work
entirely like items. Macros have two forms of scope: textual scope, and path-
based scope. Textual scope is based on the order that things appear in source
files, or even across multiple files, and is the default scoping. It is
explained further below. Path-based scope works exactly the same way that item
scoping does. The scoping, exporting, and importing of macros is controlled
largely by attributes.

[macro.decl.scope.unqualified]

When a macro is invoked by an unqualified identifier (not part of a multi-part
path), it is first looked up in textual scoping. If this does not yield any
results, then it is looked up in path-based scoping. If the macro’s name is
qualified with a path, then it is only looked up in path-based scoping.

    
    
    use lazy_static::lazy_static; // Path-based import.
    
    macro_rules! lazy_static { // Textual definition.
        (lazy) => {};
    }
    
    lazy_static!{lazy} // Textual lookup finds our macro first.
    self::lazy_static!{} // Path-based lookup ignores our macro, finds imported one.

[macro.decl.scope.textual]

### Textual scope

[macro.decl.scope.textual.intro]

Textual scope is based largely on the order that things appear in source
files, and works similarly to the scope of local variables declared with `let`
except it also applies at the module level. When `macro_rules!` is used to
define a macro, the macro enters the scope after the definition (note that it
can still be used recursively, since names are looked up from the invocation
site), up until its surrounding scope, typically a module, is closed. This can
enter child modules and even span across multiple files:

    
    
    //// src/lib.rs
    mod has_macro {
        // m!{} // Error: m is not in scope.
    
        macro_rules! m {
            () => {};
        }
        m!{} // OK: appears after declaration of m.
    
        mod uses_macro;
    }
    
    // m!{} // Error: m is not in scope.
    
    //// src/has_macro/uses_macro.rs
    
    m!{} // OK: appears after declaration of m in src/lib.rs

[macro.decl.scope.textual.shadow]

It is not an error to define a macro multiple times; the most recent
declaration will shadow the previous one unless it has gone out of scope.

    
    
    #![allow(unused)]
    fn main() {
    macro_rules! m {
        (1) => {};
    }
    
    m!(1);
    
    mod inner {
        m!(1);
    
        macro_rules! m {
            (2) => {};
        }
        // m!(1); // Error: no rule matches '1'
        m!(2);
    
        macro_rules! m {
            (3) => {};
        }
        m!(3);
    }
    
    m!(1);
    }

Macros can be declared and used locally inside functions as well, and work
similarly:

    
    
    #![allow(unused)]
    fn main() {
    fn foo() {
        // m!(); // Error: m is not in scope.
        macro_rules! m {
            () => {};
        }
        m!();
    }
    
    // m!(); // Error: m is not in scope.
    }

[macro.decl.scope.textual.shadow.path-based]

Textual scope name bindings for macros shadow path-based scope bindings to
macros.

    
    
    #![allow(unused)]
    fn main() {
    macro_rules! m2 {
        () => {
            println!("m2");
        };
    }
    
    // Resolves to path-based candidate from use declaration below.
    m!(); // prints "m2\n"
    
    // Introduce second candidate for `m` with textual scope.
    //
    // This shadows path-based candidate from below for the rest of this
    // example.
    macro_rules! m {
        () => {
            println!("m");
        };
    }
    
    // Introduce `m2` macro as path-based candidate.
    //
    // This item is in scope for this entire example, not just below the
    // use declaration.
    use m2 as m;
    
    // Resolves to the textual macro candidate from above the use
    // declaration.
    m!(); // prints "m\n"
    }

> Note
>
> For areas where shadowing is not allowed, see name resolution ambiguities.

[macro.decl.scope.path-based]

### Path-based scope

[macro.decl.scope.path-based.intro]

By default, a macro has no path-based scope. Macros can gain path-based scope
in two ways:

  * Use declaration re-export
  * `macro_export`

[macro.decl.scope.path.reexport]

Macros can be re-exported to give them path-based scope from a module other
than the crate root.

    
    
    #![allow(unused)]
    fn main() {
    mac::m!(); // OK: Path-based lookup finds `m` in the mac module.
    
    mod mac {
        // Introduce macro `m` with textual scope.
        macro_rules! m {
            () => {};
        }
    
        // Reexport with path-based scope from within `m`'s textual scope.
        pub(crate) use m;
    }
    }

[macro.decl.scope.path-based.visibility]

Macros have an implicit visibility of `pub(crate)`. `#[macro_export]` changes
the implicit visibility to `pub`.

    
    
    #![allow(unused)]
    fn main() {
    // Implicit visibility is `pub(crate)`.
    macro_rules! private_m {
        () => {};
    }
    
    // Implicit visibility is `pub`.
    #[macro_export]
    macro_rules! pub_m {
        () => {};
    }
    
    pub(crate) use private_m as private_macro; // OK.
    pub use pub_m as pub_macro; // OK.
    }
    
    
    #![allow(unused)]
    fn main() {
    // Implicit visibility is `pub(crate)`.
    macro_rules! private_m {
        () => {};
    }
    
    // Implicit visibility is `pub`.
    #[macro_export]
    macro_rules! pub_m {
        () => {};
    }
    
    pub(crate) use private_m as private_macro; // OK.
    pub use pub_m as pub_macro; // OK.
    
    pub use private_m; // ERROR: `private_m` is only public within
                       // the crate and cannot be re-exported outside.
    }

[macro.decl.scope.macro_use]

### The `macro_use` attribute

[macro.decl.scope.macro_use.intro]

The _`macro_use` attribute_ has two purposes: it may be used on modules to
extend the scope of macros defined within them, and it may be used on `extern
crate` to import macros from another crate into the `macro_use` prelude.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[macro_use]
>     mod inner {
>         macro_rules! m {
>             () => {};
>         }
>     }
>     m!();
>     }
>  
>  
>     #[macro_use]
>     extern crate log;

[macro.decl.scope.macro_use.syntax]

When used on modules, the `macro_use` attribute uses the MetaWord syntax.

When used on `extern crate`, it uses the MetaWord and MetaListIdents syntaxes.
For more on how these syntaxes may be used, see
macro.decl.scope.macro_use.prelude.

[macro.decl.scope.macro_use.allowed-positions]

The `macro_use` attribute may be applied to modules or `extern crate`.

> Note
>
> `rustc` ignores use in other positions but lints against it. This may become
> an error in the future.

[macro.decl.scope.macro_use.extern-crate-self]

The `macro_use` attribute may not be used on `extern crate self`.

[macro.decl.scope.macro_use.duplicates]

The `macro_use` attribute may be used any number of times on a form.

Multiple instances of `macro_use` in the MetaListIdents syntax may be
specified. The union of all specified macros will be imported.

> Note
>
> On modules, `rustc` lints against any MetaWord `macro_use` attributes
> following the first.
>
> On `extern crate`, `rustc` lints against any `macro_use` attributes that
> have no effect due to not importing any macros not already imported by
> another `macro_use` attribute. If two or more MetaListIdents `macro_use`
> attributes import the same macro, the first is linted against. If any
> MetaWord `macro_use` attributes are present, all MetaListIdents `macro_use`
> attributes are linted against. If two or more MetaWord `macro_use`
> attributes are present, the ones following the first are linted against.

[macro.decl.scope.macro_use.mod-decl]

When `macro_use` is used on a module, the module’s macro scope extends beyond
the module’s lexical scope.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[macro_use]
>     mod inner {
>         macro_rules! m {
>             () => {};
>         }
>     }
>     m!(); // OK
>     }

[macro.decl.scope.macro_use.prelude]

Specifying `macro_use` on an `extern crate` declaration in the crate root
imports exported macros from that crate.

Macros imported this way are imported into the `macro_use` prelude, not
textually, which means that they can be shadowed by any other name. Macros
imported by `macro_use` can be used before the import statement.

> Note
>
> `rustc` currently prefers the last macro imported in case of conflict. Don’t
> rely on this. This behavior is unusual, as imports in Rust are generally
> order-independent. This behavior of `macro_use` may change in the future.
>
> For details, see [Rust issue #148025](https://github.com/rust-
> lang/rust/issues/148025).

When using the MetaWord syntax, all exported macros are imported. When using
the MetaListIdents syntax, only the specified macros are imported.

> Example
>  
>  
>     #[macro_use(lazy_static)] // Or `#[macro_use]` to import all macros.
>     extern crate lazy_static;
>  
>     lazy_static!{}
>     // self::lazy_static!{} // ERROR: lazy_static is not defined in `self`.

[macro.decl.scope.macro_use.export]

Macros to be imported with `macro_use` must be exported with `macro_export`.

[macro.decl.scope.macro_export]

### The `macro_export` attribute

[macro.decl.scope.macro_export.intro]

The _`macro_export` attribute_ exports the macro from the crate and makes it
available in the root of the crate for path-based resolution.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     self::m!();
>     //  ^^^^ OK: Path-based lookup finds `m` in the current module.
>     m!(); // As above.
>  
>     mod inner {
>         super::m!();
>         crate::m!();
>     }
>  
>     mod mac {
>         #[macro_export]
>         macro_rules! m {
>             () => {};
>         }
>     }
>     }

[macro.decl.scope.macro_export.syntax]

The `macro_export` attribute uses the MetaWord and MetaListIdents syntaxes.
With the MetaListIdents syntax, it accepts a single `local_inner_macros`
value.

[macro.decl.scope.macro_export.allowed-positions]

The `macro_export` attribute may be applied to `macro_rules` definitions.

> Note
>
> `rustc` ignores use in other positions but lints against it. This may become
> an error in the future.

[macro.decl.scope.macro_export.duplicates]

Only the first use of `macro_export` on a macro has effect.

> Note
>
> `rustc` lints against any use following the first.

[macro.decl.scope.macro_export.path-based]

By default, macros only have textual scope and cannot be resolved by path.
When the `macro_export` attribute is used, the macro is made available in the
crate root and can be referred to by its path.

> Example
>
> Without `macro_export`, macros only have textual scope, so path-based
> resolution of the macro fails.
>  
>  
>     macro_rules! m {
>         () => {};
>     }
>     self::m!(); // ERROR
>     crate::m!(); // ERROR
>     fn main() {}
>
> With `macro_export`, path-based resolution works.
>  
>  
>     #[macro_export]
>     macro_rules! m {
>         () => {};
>     }
>     self::m!(); // OK
>     crate::m!(); // OK
>     fn main() {}

[macro.decl.scope.macro_export.export]

The `macro_export` attribute causes a macro to be exported from the crate root
so that it can be referred to in other crates by path.

> Example
>
> Given the following in a `log` crate:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[macro_export]
>     macro_rules! warn {
>         ($message:expr) => { eprintln!("WARN: {}", $message) };
>     }
>     }
>
> From another crate, you can refer to the macro by path:
>  
>  
>     fn main() {
>         log::warn!("example warning");
>     }

[macro.decl.scope.macro_export.macro_use]

`macro_export` allows the use of `macro_use` on an `extern crate` to import
the macro into the `macro_use` prelude.

> Example
>
> Given the following in a `log` crate:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[macro_export]
>     macro_rules! warn {
>         ($message:expr) => { eprintln!("WARN: {}", $message) };
>     }
>     }
>
> Using `macro_use` in a dependent crate allows you to use the macro from the
> prelude:
>  
>  
>     #[macro_use]
>     extern crate log;
>  
>     pub mod util {
>         pub fn do_thing() {
>             // Resolved via macro prelude.
>             warn!("example warning");
>         }
>     }

[macro.decl.scope.macro_export.local_inner_macros]

Adding `local_inner_macros` to the `macro_export` attribute causes all single-
segment macro invocations in the macro definition to have an implicit
`$crate::` prefix.

> Note
>
> This is intended primarily as a tool to migrate code written before `$crate`
> was added to the language to work with Rust 2018’s path-based imports of
> macros. Its use is discouraged in new code.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[macro_export(local_inner_macros)]
>     macro_rules! helped {
>         () => { helper!() } // Automatically converted to $crate::helper!().
>     }
>  
>     #[macro_export]
>     macro_rules! helper {
>         () => { () }
>     }
>     }

[macro.decl.hygiene]

## Hygiene

[macro.decl.hygiene.intro]

Macros by example have _mixed-site hygiene_. This means that loop labels,
block labels, and local variables are looked up at the macro definition site
while other symbols are looked up at the macro invocation site. For example:

    
    
    #![allow(unused)]
    fn main() {
    let x = 1;
    fn func() {
        unreachable!("this is never called")
    }
    
    macro_rules! check {
        () => {
            assert_eq!(x, 1); // Uses `x` from the definition site.
            func();           // Uses `func` from the invocation site.
        };
    }
    
    {
        let x = 2;
        fn func() { /* does not panic */ }
        check!();
    }
    }

Labels and local variables defined in macro expansion are not shared between
invocations, so this code doesn’t compile:

    
    
    #![allow(unused)]
    fn main() {
    macro_rules! m {
        (define) => {
            let x = 1;
        };
        (refer) => {
            dbg!(x);
        };
    }
    
    m!(define);
    m!(refer);
    }

[macro.decl.hygiene.crate]

A special case is the `$crate` metavariable. It refers to the crate defining
the macro, and can be used at the start of the path to look up items or macros
which are not in scope at the invocation site.

    
    
    //// Definitions in the `helper_macro` crate.
    #[macro_export]
    macro_rules! helped {
        // () => { helper!() } // This might lead to an error due to 'helper' not being in scope.
        () => { $crate::helper!() }
    }
    
    #[macro_export]
    macro_rules! helper {
        () => { () }
    }
    
    //// Usage in another crate.
    // Note that `helper_macro::helper` is not imported!
    use helper_macro::helped;
    
    fn unit() {
        helped!();
    }

Note that, because `$crate` refers to the current crate, it must be used with
a fully qualified module path when referring to non-macro items:

    
    
    #![allow(unused)]
    fn main() {
    pub mod inner {
        #[macro_export]
        macro_rules! call_foo {
            () => { $crate::inner::foo() };
        }
    
        pub fn foo() {}
    }
    }

[macro.decl.hygiene.vis]

Additionally, even though `$crate` allows a macro to refer to items within its
own crate when expanding, its use has no effect on visibility. An item or
macro referred to must still be visible from the invocation site. In the
following example, any attempt to invoke `call_foo!()` from outside its crate
will fail because `foo()` is not public.

    
    
    #![allow(unused)]
    fn main() {
    #[macro_export]
    macro_rules! call_foo {
        () => { $crate::foo() };
    }
    
    fn foo() {}
    }

> Note
>
> Prior to Rust 1.30, `$crate` and `local_inner_macros` were unsupported. They
> were added alongside path-based imports of macros, to ensure that helper
> macros did not need to be manually imported by users of a macro-exporting
> crate. Crates written for earlier versions of Rust that use helper macros
> need to be modified to use `$crate` or `local_inner_macros` to work well
> with path-based imports.

[macro.decl.follow-set]

## Follow-set ambiguity restrictions

[macro.decl.follow-set.intro]

The parser used by the macro system is reasonably powerful, but it is limited
in order to prevent ambiguity in current or future versions of the language.

[macro.decl.follow-set.token-restriction]

In particular, in addition to the rule about ambiguous expansions, a
nonterminal matched by a metavariable must be followed by a token which has
been decided can be safely used after that kind of match.

As an example, a macro matcher like `$i:expr [ , ]` could in theory be
accepted in Rust today, since `[,]` cannot be part of a legal expression and
therefore the parse would always be unambiguous. However, because `[` can
start trailing expressions, `[` is not a character which can safely be ruled
out as coming after an expression. If `[,]` were accepted in a later version
of Rust, this matcher would become ambiguous or would misparse, breaking
working code. Matchers like `$i:expr,` or `$i:expr;` would be legal, however,
because `,` and `;` are legal expression separators. The specific rules are:

[macro.decl.follow-set.token-expr-stmt]

  * `expr` and `stmt` may only be followed by one of: `=>`, `,`, or `;`.

[macro.decl.follow-set.token-pat_param]

  * `pat_param` may only be followed by one of: `=>`, `,`, `=`, `|`, `if`, or `in`.

[macro.decl.follow-set.token-pat]

  * `pat` may only be followed by one of: `=>`, `,`, `=`, `if`, or `in`.

[macro.decl.follow-set.token-path-ty]

  * `path` and `ty` may only be followed by one of: `=>`, `,`, `=`, `|`, `;`, `:`, `>`, `>>`, `[`, `{`, `as`, `where`, or a macro variable of `block` fragment specifier.

[macro.decl.follow-set.token-vis]

  * `vis` may only be followed by one of: `,`, an identifier other than a non-raw `priv`, any token that can begin a type, or a metavariable with a `ident`, `ty`, or `path` fragment specifier.

[macro.decl.follow-set.token-other]

  * All other fragment specifiers have no restrictions.

[macro.decl.follow-set.edition2021]

> 2021 Edition differences
>
> Before the 2021 edition, `pat` may also be followed by `|`.

[macro.decl.follow-set.repetition]

When repetitions are involved, then the rules apply to every possible number
of expansions, taking separators into account. This means:

  * If the repetition includes a separator, that separator must be able to follow the contents of the repetition.
  * If the repetition can repeat multiple times (`*` or `+`), then the contents must be able to follow themselves.
  * The contents of the repetition must be able to follow whatever comes before, and whatever comes after must be able to follow the contents of the repetition.
  * If the repetition can match zero times (`*` or `?`), then whatever comes after must be able to follow whatever comes before.

For more detail, see the formal specification.

[macro.proc]

# Procedural macros

[macro.proc.intro]

_Procedural macros_ allow creating syntax extensions as execution of a
function. Procedural macros come in one of three flavors:

  * Function-like macros \- `custom!(...)`
  * Derive macros \- `#[derive(CustomDerive)]`
  * Attribute macros \- `#[CustomAttribute]`

Procedural macros allow you to run code at compile time that operates over
Rust syntax, both consuming and producing Rust syntax. You can sort of think
of procedural macros as functions from an AST to another AST.

[macro.proc.def]

Procedural macros must be defined in the root of a crate with the crate type
of `proc-macro`. The macros may not be used from the crate where they are
defined, and can only be used when imported in another crate.

> Note
>
> When using Cargo, Procedural macro crates are defined with the `proc-macro`
> key in your manifest:
>  
>  
>     [lib]
>     proc-macro = true
>  

[macro.proc.result]

As functions, they must either return syntax, panic, or loop endlessly.
Returned syntax either replaces or adds the syntax depending on the kind of
procedural macro. Panics are caught by the compiler and are turned into a
compiler error. Endless loops are not caught by the compiler which hangs the
compiler.

Procedural macros run during compilation, and thus have the same resources
that the compiler has. For example, standard input, error, and output are the
same that the compiler has access to. Similarly, file access is the same.
Because of this, procedural macros have the same security concerns that
[Cargo’s build scripts](../cargo/reference/build-scripts.html) have.

[macro.proc.error]

Procedural macros have two ways of reporting errors. The first is to panic.
The second is to emit a [`compile_error`](../core/macro.compile_error.html)
macro invocation.

[macro.proc.proc_macro-crate]

## The `proc_macro` crate

[macro.proc.proc_macro-crate.intro]

Procedural macro crates almost always will link to the compiler-provided
[`proc_macro` crate](../proc_macro/index.html). The `proc_macro` crate
provides types required for writing procedural macros and facilities to make
it easier.

[macro.proc.proc_macro-crate.token-stream]

This crate primarily contains a
[`TokenStream`](../proc_macro/struct.TokenStream.html) type. Procedural macros
operate over _token streams_ instead of AST nodes, which is a far more stable
interface over time for both the compiler and for procedural macros to target.
A _token stream_ is roughly equivalent to `Vec<TokenTree>` where a `TokenTree`
can roughly be thought of as lexical token. For example `foo` is an `Ident`
token, `.` is a `Punct` token, and `1.2` is a `Literal` token. The
`TokenStream` type, unlike `Vec<TokenTree>`, is cheap to clone.

[macro.proc.proc_macro-crate.span]

All tokens have an associated `Span`. A `Span` is an opaque value that cannot
be modified but can be manufactured. `Span`s represent an extent of source
code within a program and are primarily used for error reporting. While you
cannot modify a `Span` itself, you can always change the `Span` _associated_
with any token, such as through getting a `Span` from another token.

[macro.proc.hygiene]

## Procedural macro hygiene

Procedural macros are _unhygienic_. This means they behave as if the output
token stream was simply written inline to the code it’s next to. This means
that it’s affected by external items and also affects external imports.

Macro authors need to be careful to ensure their macros work in as many
contexts as possible given this limitation. This often includes using absolute
paths to items in libraries (for example, `::std::option::Option` instead of
`Option`) or by ensuring that generated functions have names that are unlikely
to clash with other functions (like `__internal_foo` instead of `foo`).

[macro.proc.proc_macro]

## The `proc_macro` attribute

[macro.proc.proc_macro.intro]

The _`proc_macro` attribute_ defines a function-like procedural macro.

> Example
>
> This macro definition ignores its input and emits a function `answer` into
> its scope.
>  
>  
>     #![crate_type = "proc-macro"]
>     extern crate proc_macro;
>     use proc_macro::TokenStream;
>  
>     #[proc_macro]
>     pub fn make_answer(_item: TokenStream) -> TokenStream {
>         "fn answer() -> u32 { 42 }".parse().unwrap()
>     }
>
> We can use it in a binary crate to print “42” to standard output.
>  
>  
>     extern crate proc_macro_examples;
>     use proc_macro_examples::make_answer;
>  
>     make_answer!();
>  
>     fn main() {
>         println!("{}", answer());
>     }

[macro.proc.proc_macro.syntax]

The `proc_macro` attribute uses the MetaWord syntax.

[macro.proc.proc_macro.allowed-positions]

The `proc_macro` attribute may only be applied to a `pub` function of type
`fn(TokenStream) -> TokenStream` where
[`TokenStream`](../proc_macro/struct.TokenStream.html) comes from the
[`proc_macro` crate](../proc_macro/index.html). It must have the “Rust” ABI.
No other function qualifiers are allowed. It must be located in the root of
the crate.

[macro.proc.proc_macro.duplicates]

The `proc_macro` attribute may only be specified once on a function.

[macro.proc.proc_macro.namespace]

The `proc_macro` attribute publicly defines the macro in the macro namespace
in the root of the crate with the same name as the function.

[macro.proc.proc_macro.behavior]

A function-like macro invocation of a function-like procedural macro will pass
what is inside the delimiters of the macro invocation as the input
[`TokenStream`](../proc_macro/struct.TokenStream.html) argument and replace
the entire macro invocation with the output
[`TokenStream`](../proc_macro/struct.TokenStream.html) of the function.

[macro.proc.proc_macro.invocation]

Function-like procedural macros may be invoked in any macro invocation
position, which includes:

  * Statements
  * Expressions
  * Patterns
  * Type expressions
  * Item positions, including items in `extern` blocks
  * Inherent and trait implementations
  * Trait definitions

[macro.proc.derive]

## The `proc_macro_derive` attribute

[macro.proc.derive.intro]

Applying the _`proc_macro_derive` attribute_ to a function defines a _derive
macro_ that can be invoked by the `derive` attribute. These macros are given
the token stream of a struct, enum, or union definition and can emit new items
after it. They can also declare and use derive macro helper attributes.

> Example
>
> This derive macro ignores its input and appends tokens that define a
> function.
>  
>  
>     #![crate_type = "proc-macro"]
>     extern crate proc_macro;
>     use proc_macro::TokenStream;
>  
>     #[proc_macro_derive(AnswerFn)]
>     pub fn derive_answer_fn(_item: TokenStream) -> TokenStream {
>         "fn answer() -> u32 { 42 }".parse().unwrap()
>     }
>
> To use it, we might write:
>  
>  
>     extern crate proc_macro_examples;
>     use proc_macro_examples::AnswerFn;
>  
>     #[derive(AnswerFn)]
>     struct Struct;
>  
>     fn main() {
>         assert_eq!(42, answer());
>     }

[macro.proc.derive.syntax]

The syntax for the `proc_macro_derive` attribute is:

**Syntax**  
ProcMacroDeriveAttribute →  
proc_macro_derive ( DeriveMacroName ( , DeriveMacroAttributes )? ,? )

DeriveMacroName → IDENTIFIER

DeriveMacroAttributes →  
attributes ( ( IDENTIFIER ( , IDENTIFIER )* ,? )? )

Show Railroad

ProcMacroDeriveAttribute proc_macro_derive ( DeriveMacroName ,
DeriveMacroAttributes , )

DeriveMacroName IDENTIFIER

DeriveMacroAttributes attributes ( IDENTIFIER , IDENTIFIER , )

The name of the derive macro is given by DeriveMacroName. The optional
`attributes` argument is described in macro.proc.derive.attributes.

[macro.proc.derive.allowed-positions]

The `proc_macro_derive` attribute may only be applied to a `pub` function with
the Rust ABI defined in the root of the crate with a type of `fn(TokenStream)
-> TokenStream` where [`TokenStream`](../proc_macro/struct.TokenStream.html)
comes from the [`proc_macro` crate](../proc_macro/index.html). The function
may be `const` and may use `extern` to explicitly specify the Rust ABI, but it
may not use any other qualifiers (e.g. it may not be `async` or `unsafe`).

[macro.proc.derive.duplicates]

The `proc_macro_derive` attribute may be used only once on a function.

[macro.proc.derive.namespace]

The `proc_macro_derive` attribute publicly defines the derive macro in the
macro namespace in the root of the crate.

[macro.proc.derive.output]

The input [`TokenStream`](../proc_macro/struct.TokenStream.html) is the token
stream of the item to which the `derive` attribute is applied. The output
[`TokenStream`](../proc_macro/struct.TokenStream.html) must be a (possibly
empty) set of items. These items are appended following the input item within
the same module or block.

[macro.proc.derive.attributes]

### Derive macro helper attributes

[macro.proc.derive.attributes.intro]

Derive macros can declare _derive macro helper attributes_ to be used within
the scope of the item to which the derive macro is applied. These attributes
are inert. While their purpose is to be used by the macro that declared them,
they can be seen by any macro.

[macro.proc.derive.attributes.decl]

A helper attribute for a derive macro is declared by adding its identifier to
the `attributes` list in the `proc_macro_derive` attribute.

> Example
>
> This declares a helper attribute and then ignores it.
>  
>  
>     #![crate_type="proc-macro"]
>     extern crate proc_macro;
>     use proc_macro::TokenStream;
>  
>     #[proc_macro_derive(WithHelperAttr, attributes(helper))]
>     pub fn derive_with_helper_attr(_item: TokenStream) -> TokenStream {
>         TokenStream::new()
>     }
>
> To use it, we might write:
>  
>  
>     #[derive(WithHelperAttr)]
>     struct Struct {
>         #[helper] field: (),
>     }

[macro.proc.derive.attributes.scope]

When a derive macro invocation is applied to an item, the helper attributes
introduced by that derive macro become in scope 1) for attributes that are
applied to that item and are applied lexically after the derive macro
invocation and 2) for attributes that are applied to fields and variants
inside of the item.

> Note
>
> rustc currently allows derive helpers to be used before the macro that
> introduces them. Such derive helpers used out of order may not shadow other
> attribute macros. This behavior is deprecated and slated for removal.
>  
>  
>     #[helper] // Deprecated, hard error in the future.
>     #[derive(WithHelperAttr)]
>     struct Struct {
>         field: (),
>     }
>
> For more details, see [Rust issue #79202](https://github.com/rust-
> lang/rust/issues/79202).

[macro.proc.attribute]

## The `proc_macro_attribute` attribute

[macro.proc.attribute.intro]

The _`proc_macro_attribute` attribute_ defines an _attribute macro_ which can
be used as an outer attribute.

> Example
>
> This attribute macro takes the input stream and emits it as-is, effectively
> being a no-op attribute.
>  
>  
>     #![crate_type = "proc-macro"]
>     extern crate proc_macro;
>     use proc_macro::TokenStream;
>  
>     #[proc_macro_attribute]
>     pub fn return_as_is(_attr: TokenStream, item: TokenStream) ->
> TokenStream {
>         item
>     }

> Example
>
> This shows, in the output of the compiler, the stringified
> [`TokenStream`s](../proc_macro/struct.TokenStream.html) that attribute
> macros see.
>  
>  
>     // my-macro/src/lib.rs
>     extern crate proc_macro;
>     use proc_macro::TokenStream;
>     #[proc_macro_attribute]
>     pub fn show_streams(attr: TokenStream, item: TokenStream) -> TokenStream
> {
>         println!("attr: \"{attr}\"");
>         println!("item: \"{item}\"");
>         item
>     }
>  
>  
>     // src/lib.rs
>     extern crate my_macro;
>  
>     use my_macro::show_streams;
>  
>     // Example: Basic function.
>     #[show_streams]
>     fn invoke1() {}
>     // out: attr: ""
>     // out: item: "fn invoke1() {}"
>  
>     // Example: Attribute with input.
>     #[show_streams(bar)]
>     fn invoke2() {}
>     // out: attr: "bar"
>     // out: item: "fn invoke2() {}"
>  
>     // Example: Multiple tokens in the input.
>     #[show_streams(multiple => tokens)]
>     fn invoke3() {}
>     // out: attr: "multiple => tokens"
>     // out: item: "fn invoke3() {}"
>  
>     // Example: Delimiters in the input.
>     #[show_streams { delimiters }]
>     fn invoke4() {}
>     // out: attr: "delimiters"
>     // out: item: "fn invoke4() {}"

[macro.proc.attribute.syntax]

The `proc_macro_attribute` attribute uses the MetaWord syntax.

[macro.proc.attribute.allowed-positions]

The `proc_macro_attribute` attribute may only be applied to a `pub` function
of type `fn(TokenStream, TokenStream) -> TokenStream` where
[`TokenStream`](../proc_macro/struct.TokenStream.html) comes from the
[`proc_macro` crate](../proc_macro/index.html). It must have the “Rust” ABI.
No other function qualifiers are allowed. It must be located in the root of
the crate.

[macro.proc.attribute.duplicates]

The `proc_macro_attribute` attribute may only be specified once on a function.

[macro.proc.attribute.namespace]

The `proc_macro_attribute` attribute defines the attribute in the macro
namespace in the root of the crate with the same name as the function.

[macro.proc.attribute.use-positions]

Attribute macros can only be used on:

  * Items
  * Items in `extern` blocks
  * Inherent and trait implementations
  * Trait definitions

[macro.proc.attribute.behavior]

The first [`TokenStream`](../proc_macro/struct.TokenStream.html) parameter is
the delimited token tree following the attribute’s name but not including the
outer delimiters. If the applied attribute contains only the attribute name or
the attribute name followed by empty delimiters, the
[`TokenStream`](../proc_macro/struct.TokenStream.html) is empty.

The second [`TokenStream`](../proc_macro/struct.TokenStream.html) is the rest
of the item, including other attributes on the item.

The item to which the attribute is applied is replaced by the zero or more
items in the returned [`TokenStream`](../proc_macro/struct.TokenStream.html).

[macro.proc.token]

## Declarative macro tokens and procedural macro tokens

[macro.proc.token.intro]

Declarative `macro_rules` macros and procedural macros use similar, but
different definitions for tokens (or rather
[`TokenTree`s](../proc_macro/enum.TokenTree.html).)

[macro.proc.token.macro_rules]

Token trees in `macro_rules` (corresponding to `tt` matchers) are defined as

  * Delimited groups (`(...)`, `{...}`, etc)
  * All operators supported by the language, both single-character and multi-character ones (`+`, `+=`). 
    * Note that this set doesn’t include the single quote `'`.
  * Literals (`"string"`, `1`, etc) 
    * Note that negation (e.g. `-1`) is never a part of such literal tokens, but a separate operator token.
  * Identifiers, including keywords (`ident`, `r#ident`, `fn`)
  * Lifetimes (`'ident`)
  * Metavariable substitutions in `macro_rules` (e.g. `$my_expr` in `macro_rules! mac { ($my_expr: expr) => { $my_expr } }` after the `mac`’s expansion, which will be considered a single token tree regardless of the passed expression)

[macro.proc.token.tree]

Token trees in procedural macros are defined as

  * Delimited groups (`(...)`, `{...}`, etc)
  * All punctuation characters used in operators supported by the language (`+`, but not `+=`), and also the single quote `'` character (typically used in lifetimes, see below for lifetime splitting and joining behavior)
  * Literals (`"string"`, `1`, etc) 
    * Negation (e.g. `-1`) is supported as a part of integer and floating point literals.
  * Identifiers, including keywords (`ident`, `r#ident`, `fn`)

[macro.proc.token.conversion.intro]

Mismatches between these two definitions are accounted for when token streams
are passed to and from procedural macros.  
Note that the conversions below may happen lazily, so they might not happen if
the tokens are not actually inspected.

[macro.proc.token.conversion.to-proc_macro]

When passed to a proc-macro

  * All multi-character operators are broken into single characters.
  * Lifetimes are broken into a `'` character and an identifier.
  * The keyword metavariable `$crate` is passed as a single identifier.
  * All other metavariable substitutions are represented as their underlying token streams. 
    * Such token streams may be wrapped into delimited groups ([`Group`](../proc_macro/struct.Group.html)) with implicit delimiters ([`Delimiter::None`](../proc_macro/enum.Delimiter.html#variant.None)) when it’s necessary for preserving parsing priorities.
    * `tt` and `ident` substitutions are never wrapped into such groups and always represented as their underlying token trees.

[macro.proc.token.conversion.from-proc_macro]

When emitted from a proc macro

  * Punctuation characters are glued into multi-character operators when applicable.
  * Single quotes `'` joined with identifiers are glued into lifetimes.
  * Negative literals are converted into two tokens (the `-` and the literal) possibly wrapped into a delimited group ([`Group`](../proc_macro/struct.Group.html)) with implicit delimiters ([`Delimiter::None`](../proc_macro/enum.Delimiter.html#variant.None)) when it’s necessary for preserving parsing priorities.

[macro.proc.token.doc-comment]

Note that neither declarative nor procedural macros support doc comment tokens
(e.g. `/// Doc`), so they are always converted to token streams representing
their equivalent `#[doc = r"str"]` attributes when passed to macros.

[crate]

# Crates and source files

[crate.syntax]

**Syntax**  
Crate →  
InnerAttribute*  
Item*

Show Railroad

Crate InnerAttribute Item

> Note
>
> Although Rust, like any other language, can be implemented by an interpreter
> as well as a compiler, the only existing implementation is a compiler, and
> the language has always been designed to be compiled. For these reasons,
> this section assumes a compiler.

[crate.compile-time]

Rust’s semantics obey a _phase distinction_ between compile-time and run-
time.1 Semantic rules that have a _static interpretation_ govern the success
or failure of compilation, while semantic rules that have a _dynamic
interpretation_ govern the behavior of the program at run-time.

[crate.unit]

The compilation model centers on artifacts called _crates_. Each compilation
processes a single crate in source form, and if successful, produces a single
crate in binary form: either an executable or some sort of library.2

[crate.module]

A _crate_ is a unit of compilation and linking, as well as versioning,
distribution, and runtime loading. A crate contains a _tree_ of nested module
scopes. The top level of this tree is a module that is anonymous (from the
point of view of paths within the module) and any item within a crate has a
canonical module path denoting its location within the crate’s module tree.

[crate.input-source]

The Rust compiler is always invoked with a single source file as input, and
always produces a single output crate. The processing of that source file may
result in other source files being loaded as modules. Source files have the
extension `.rs`.

[crate.module-def]

A Rust source file describes a module, the name and location of which — in the
module tree of the current crate — are defined from outside the source file:
either by an explicit Module item in a referencing source file, or by the name
of the crate itself.

[crate.inline-module]

Every source file is a module, but not every module needs its own source file:
module definitions can be nested within one file.

[crate.items]

Each source file contains a sequence of zero or more Item definitions, and may
optionally begin with any number of attributes that apply to the containing
module, most of which influence the behavior of the compiler.

[crate.attributes]

The anonymous crate module can have additional attributes that apply to the
crate as a whole.

> Note
>
> The file’s contents may be preceded by a shebang.
    
    
    #![allow(unused)]
    fn main() {
    // Specify the crate name.
    #![crate_name = "projx"]
    
    // Specify the type of output artifact.
    #![crate_type = "lib"]
    
    // Turn on a warning.
    // This can be done in any module, not just the anonymous crate module.
    #![warn(non_camel_case_types)]
    }

[crate.main]

## Main functions

[crate.main.general]

A crate that contains a `main` function can be compiled to an executable.

[crate.main.restriction]

If a `main` function is present, it must take no arguments, must not declare
any trait or lifetime bounds, must not have any where clauses, and its return
type must implement the [`Termination`](../std/process/trait.Termination.html)
trait.

    
    
    fn main() {}
    
    
    fn main() -> ! {
        std::process::exit(0);
    }
    
    
    fn main() -> impl std::process::Termination {
        std::process::ExitCode::SUCCESS
    }

[crate.main.import]

The `main` function may be an import, e.g. from an external crate or from the
current one.

    
    
    #![allow(unused)]
    fn main() {
    mod foo {
        pub fn bar() {
            println!("Hello, world!");
        }
    }
    use foo::bar as main;
    }

> Note
>
> Types with implementations of
> [`Termination`](../std/process/trait.Termination.html) in the standard
> library include:
>
>   * `()`
>   * `!`
>   * [`Infallible`](../core/convert/enum.Infallible.html)
>   * [`ExitCode`](../std/process/struct.ExitCode.html)
>   * `Result<T, E> where T: Termination, E: Debug`
>

[crate.uncaught-foreign-unwinding]

### Uncaught foreign unwinding

When a “foreign” unwind (e.g. an exception thrown from C++ code, or a `panic!`
in Rust code using a different panic handler) propagates beyond the `main`
function, the process will be safely terminated. This may take the form of an
abort, in which case it is not guaranteed that any `Drop` calls will be
executed, and the error output may be less informative than if the runtime had
been terminated by a “native” Rust `panic`.

For more information, see the panic documentation.

[crate.no_main]

### The `no_main` attribute

The _`no_main` attribute_ may be applied at the crate level to disable
emitting the `main` symbol for an executable binary. This is useful when some
other object being linked to defines `main`.

[crate.crate_name]

## The `crate_name` attribute

[crate.crate_name.general]

The _`crate_name` attribute_ may be applied at the crate level to specify the
name of the crate with the MetaNameValueStr syntax.

    
    
    #![allow(unused)]
    #![crate_name = "mycrate"]
    fn main() {
    }

[crate.crate_name.restriction]

The crate name must not be empty, and must only contain [Unicode
alphanumeric](../std/primitive.char.html#method.is_alphanumeric) or `_`
(U+005F) characters.

* * *

  1. This distinction would also exist in an interpreter. Static checks like syntactic analysis, type checking, and lints should happen before the program is executed regardless of when it is executed. ↩

  2. A crate is somewhat analogous to an _assembly_ in the ECMA-335 CLI model, a _library_ in the SML/NJ Compilation Manager, a _unit_ in the Owens and Flatt module system, or a _configuration_ in Mesa. ↩

[cfg]

# Conditional compilation

[cfg.syntax]

**Syntax**  
ConfigurationPredicate →  
ConfigurationOption  
| ConfigurationAll  
| ConfigurationAny  
| ConfigurationNot  
| true  
| false

ConfigurationOption →  
IDENTIFIER ( = ( STRING_LITERAL | RAW_STRING_LITERAL ) )?

ConfigurationAll →  
all ( ConfigurationPredicateList? )

ConfigurationAny →  
any ( ConfigurationPredicateList? )

ConfigurationNot →  
not ( ConfigurationPredicate )

ConfigurationPredicateList →  
ConfigurationPredicate ( , ConfigurationPredicate )* ,?

Show Railroad

ConfigurationPredicate ConfigurationOption ConfigurationAll ConfigurationAny
ConfigurationNot true false

ConfigurationOption IDENTIFIER = STRING_LITERAL RAW_STRING_LITERAL

ConfigurationAll all ( ConfigurationPredicateList )

ConfigurationAny any ( ConfigurationPredicateList )

ConfigurationNot not ( ConfigurationPredicate )

ConfigurationPredicateList ConfigurationPredicate , ConfigurationPredicate ,

[cfg.general]

_Conditionally compiled source code_ is source code that is compiled only
under certain conditions.

[cfg.attributes-macro]

Source code can be made conditionally compiled using the `cfg` and `cfg_attr`
attributes and the built-in `cfg` macro.

[cfg.conditional]

Whether to compile can depend on the target architecture of the compiled
crate, arbitrary values passed to the compiler, and other things further
described below.

[cfg.predicate]

Each form of conditional compilation takes a _configuration predicate_ that
evaluates to true or false. The predicate is one of the following:

[cfg.predicate.option]

  * A configuration option. The predicate is true if the option is set, and false if it is unset.

[cfg.predicate.all]

  * `all()` with a comma-separated list of configuration predicates. It is true if all of the given predicates are true, or if the list is empty.

[cfg.predicate.any]

  * `any()` with a comma-separated list of configuration predicates. It is true if at least one of the given predicates is true. If there are no predicates, it is false.

[cfg.predicate.not]

  * `not()` with a configuration predicate. It is true if its predicate is false and false if its predicate is true.

[cfg.predicate.literal]

  * `true` or `false` literals, which are always true or false respectively.

[cfg.option-spec]

_Configuration options_ are either names or key-value pairs, and are either
set or unset.

[cfg.option-name]

Names are written as a single identifier, such as `unix`.

[cfg.option-key-value]

Key-value pairs are written as an identifier, `=`, and then a string, such as
`target_arch = "x86_64"`.

> Note
>
> Whitespace around the `=` is ignored, so `foo="bar"` and `foo = "bar"` are
> equivalent.

[cfg.option-key-uniqueness]

Keys do not need to be unique. For example, both `feature = "std"` and
`feature = "serde"` can be set at the same time.

[cfg.options.set]

## Set configuration options

[cfg.options.general]

Which configuration options are set is determined statically during the
compilation of the crate.

[cfg.options.target]

Some options are _compiler-set_ based on data about the compilation.

[cfg.options.other]

Other options are _arbitrarily-set_ based on input passed to the compiler
outside of the code.

[cfg.options.crate]

It is not possible to set a configuration option from within the source code
of the crate being compiled.

> Note
>
> For `rustc`, arbitrary-set configuration options are set using the
> [`--cfg`](../rustc/command-line-arguments.html#--cfg-configure-the-
> compilation-environment) flag. Configuration values for a specified target
> can be displayed with `rustc --print cfg --target $TARGET`.

> Note
>
> Configuration options with the key `feature` are a convention used by
> [Cargo](../cargo/reference/features.html) for specifying compile-time
> options and optional dependencies.

[cfg.target_arch]

### `target_arch`

[cfg.target_arch.gen]

Key-value option set once with the target’s CPU architecture. The value is
similar to the first element of the platform’s target triple, but not
identical.

[cfg.target_arch.values]

Example values:

  * `"x86"`
  * `"x86_64"`
  * `"mips"`
  * `"powerpc"`
  * `"powerpc64"`
  * `"arm"`
  * `"aarch64"`

[cfg.target_feature]

### `target_feature`

[cfg.target_feature.general]

Key-value option set for each platform feature available for the current
compilation target.

[cfg.target_feature.values]

Example values:

  * `"avx"`
  * `"avx2"`
  * `"crt-static"`
  * `"rdrand"`
  * `"sse"`
  * `"sse2"`
  * `"sse4.1"`

See the `target_feature` attribute for more details on the available features.

[cfg.target_feature.crt_static]

An additional feature of `crt-static` is available to the `target_feature`
option to indicate that a static C runtime is available.

[cfg.target_os]

### `target_os`

[cfg.target_os.general]

Key-value option set once with the target’s operating system. This value is
similar to the second and third element of the platform’s target triple.

[cfg.target_os.values]

Example values:

  * `"windows"`
  * `"macos"`
  * `"ios"`
  * `"linux"`
  * `"android"`
  * `"freebsd"`
  * `"dragonfly"`
  * `"openbsd"`
  * `"netbsd"`
  * `"none"` (typical for embedded targets)

[cfg.target_family]

### `target_family`

[cfg.target_family.general]

Key-value option providing a more generic description of a target, such as the
family of the operating systems or architectures that the target generally
falls into. Any number of `target_family` key-value pairs can be set.

[cfg.target_family.values]

Example values:

  * `"unix"`
  * `"windows"`
  * `"wasm"`
  * Both `"unix"` and `"wasm"`

[cfg.target_family.unix]

### `unix` and `windows`

`unix` is set if `target_family = "unix"` is set.

[cfg.target_family.windows]

`windows` is set if `target_family = "windows"` is set.

[cfg.target_env]

### `target_env`

[cfg.target_env.general]

Key-value option set with further disambiguating information about the target
platform with information about the ABI or `libc` used. For historical
reasons, this value is only defined as not the empty-string when actually
needed for disambiguation. Thus, for example, on many GNU platforms, this
value will be empty. This value is similar to the fourth element of the
platform’s target triple. One difference is that embedded ABIs such as
`gnueabihf` will simply define `target_env` as `"gnu"`.

[cfg.target_env.values]

Example values:

  * `""`
  * `"gnu"`
  * `"msvc"`
  * `"musl"`
  * `"sgx"`
  * `"sim"`
  * `"macabi"`

[cfg.target_abi]

### `target_abi`

[cfg.target_abi.general]

Key-value option set to further disambiguate the target with information about
the target ABI.

[cfg.target_abi.disambiguation]

For historical reasons, this value is only defined as not the empty-string
when actually needed for disambiguation. Thus, for example, on many GNU
platforms, this value will be empty.

[cfg.target_abi.values]

Example values:

  * `""`
  * `"llvm"`
  * `"eabihf"`
  * `"abi64"`

[cfg.target_endian]

### `target_endian`

Key-value option set once with either a value of “little” or “big” depending
on the endianness of the target’s CPU.

[cfg.target_pointer_width]

### `target_pointer_width`

[cfg.target_pointer_width.general]

Key-value option set once with the target’s pointer width in bits.

[cfg.target_pointer_width.values]

Example values:

  * `"16"`
  * `"32"`
  * `"64"`

[cfg.target_vendor]

### `target_vendor`

[cfg.target_vendor.general]

Key-value option set once with the vendor of the target.

[cfg.target_vendor.values]

Example values:

  * `"apple"`
  * `"fortanix"`
  * `"pc"`
  * `"unknown"`

[cfg.target_has_atomic]

### `target_has_atomic`

[cfg.target_has_atomic.general]

Key-value option set for each bit width that the target supports atomic loads,
stores, and compare-and-swap operations.

[cfg.target_has_atomic.stdlib]

When this cfg is present, all of the stable
[`core::sync::atomic`](../core/sync/atomic/index.html) APIs are available for
the relevant atomic width.

[cfg.target_has_atomic.values]

Possible values:

  * `"8"`
  * `"16"`
  * `"32"`
  * `"64"`
  * `"128"`
  * `"ptr"`

[cfg.test]

### `test`

Enabled when compiling the test harness. Done with `rustc` by using the
[`--test`](../rustc/command-line-arguments.html#--test-build-a-test-harness)
flag. See Testing for more on testing support.

[cfg.debug_assertions]

### `debug_assertions`

Enabled by default when compiling without optimizations. This can be used to
enable extra debugging code in development but not in production. For example,
it controls the behavior of the standard library’s
[`debug_assert!`](../core/macro.debug_assert.html) macro.

[cfg.proc_macro]

### `proc_macro`

Set when the crate being compiled is being compiled with the `proc_macro`
crate type.

[cfg.panic]

### `panic`

[cfg.panic.general]

Key-value option set depending on the panic strategy. Note that more values
may be added in the future.

[cfg.panic.values]

Example values:

  * `"abort"`
  * `"unwind"`

## Forms of conditional compilation

[cfg.attr]

### The `cfg` attribute

[cfg.attr.intro]

The _`cfg` attribute_ conditionally includes the form to which it is attached
based on a configuration predicate.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     // The function is only included in the build when compiling for macOS
>     #[cfg(target_os = "macos")]
>     fn macos_only() {
>       // ...
>     }
>  
>     // This function is only included when either foo or bar is defined
>     #[cfg(any(foo, bar))]
>     fn needs_foo_or_bar() {
>       // ...
>     }
>  
>     // This function is only included when compiling for a unixish OS with a
> 32-bit
>     // architecture
>     #[cfg(all(unix, target_pointer_width = "32"))]
>     fn on_32bit_unix() {
>       // ...
>     }
>  
>     // This function is only included when foo is not defined
>     #[cfg(not(foo))]
>     fn needs_not_foo() {
>       // ...
>     }
>  
>     // This function is only included when the panic strategy is set to
> unwind
>     #[cfg(panic = "unwind")]
>     fn when_unwinding() {
>       // ...
>     }
>     }

[cfg.attr.syntax]

The syntax for the `cfg` attribute is:

**Syntax**  
CfgAttribute → cfg ( ConfigurationPredicate )

Show Railroad

CfgAttribute cfg ( ConfigurationPredicate )

[cfg.attr.allowed-positions]

The `cfg` attribute may be used anywhere attributes are allowed.

[cfg.attr.duplicates]

The `cfg` attribute may be used any number of times on a form. The form to
which the attributes are attached will not be included if any of the `cfg`
predicates are false except as described in cfg.attr.crate-level-attrs.

[cfg.attr.effect]

If the predicates are true, the form is rewritten to not have the `cfg`
attributes on it. If any predicate is false, the form is removed from the
source code.

[cfg.attr.crate-level-attrs]

When a crate-level `cfg` has a false predicate, the crate itself still exists.
Any crate attributes preceding the `cfg` are kept, and any crate attributes
following the `cfg` are removed as well as removing all of the following crate
contents.

> Example
>
> The behavior of not removing the preceding attributes allows you to do
> things such as include `#![no_std]` to avoid linking `std` even if a
> `#![cfg(...)]` has otherwise removed the contents of the crate. For example:
>  
>  
>     // This `no_std` attribute is kept even though the crate-level `cfg`
>     // attribute is false.
>     #![no_std]
>     #![cfg(false)]
>  
>     // This function is not included.
>     pub fn example() {}

[cfg.cfg_attr]

### The `cfg_attr` attribute

[cfg.cfg_attr.intro]

The _`cfg_attr` attribute_ conditionally includes attributes based on a
configuration predicate.

> Example
>
> The following module will either be found at `linux.rs` or `windows.rs`
> based on the target.
>  
>  
>     #[cfg_attr(target_os = "linux", path = "linux.rs")]
>     #[cfg_attr(windows, path = "windows.rs")]
>     mod os;

[cfg.cfg_attr.syntax]

The syntax for the `cfg_attr` attribute is:

**Syntax**  
CfgAttrAttribute → cfg_attr ( ConfigurationPredicate , CfgAttrs? )

CfgAttrs → Attr ( , Attr )* ,?

Show Railroad

CfgAttrAttribute cfg_attr ( ConfigurationPredicate , CfgAttrs )

CfgAttrs Attr , Attr ,

[cfg.cfg_attr.allowed-positions]

The `cfg_attr` attribute may be used anywhere attributes are allowed.

[cfg.cfg_attr.duplicates]

The `cfg_attr` attribute may be used any number of times on a form.

[cfg.cfg_attr.attr-restriction]

The `crate_type` and `crate_name` attributes cannot be used with `cfg_attr`.

[cfg.cfg_attr.behavior]

When the configuration predicate is true, `cfg_attr` expands out to the
attributes listed after the predicate.

[cfg.cfg_attr.attribute-list]

Zero, one, or more attributes may be listed. Multiple attributes will each be
expanded into separate attributes.

> Example
>  
>  
>     #[cfg_attr(feature = "magic", sparkles, crackles)]
>     fn bewitched() {}
>  
>     // When the `magic` feature flag is enabled, the above will expand to:
>     #[sparkles]
>     #[crackles]
>     fn bewitched() {}

> Note
>
> The `cfg_attr` can expand to another `cfg_attr`. For example,
> `#[cfg_attr(target_os = "linux", cfg_attr(feature = "multithreaded",
> some_other_attribute))]` is valid. This example would be equivalent to
> `#[cfg_attr(all(target_os = "linux", feature = "multithreaded"),
> some_other_attribute)]`.

[cfg.macro]

### The `cfg` macro

The built-in `cfg` macro takes in a single configuration predicate and
evaluates to the `true` literal when the predicate is true and the `false`
literal when it is false.

For example:

    
    
    #![allow(unused)]
    fn main() {
    let machine_kind = if cfg!(unix) {
      "unix"
    } else if cfg!(windows) {
      "windows"
    } else {
      "unknown"
    };
    
    println!("I'm running on a {} machine!", machine_kind);
    }

[items]

# Items

[items.syntax]

**Syntax**  
Item →  
OuterAttribute* ( VisItem | MacroItem )

VisItem →  
Visibility?  
(  
Module  
| ExternCrate  
| UseDeclaration  
| Function  
| TypeAlias  
| Struct  
| Enumeration  
| Union  
| ConstantItem  
| StaticItem  
| Trait  
| Implementation  
| ExternBlock  
)

MacroItem →  
MacroInvocationSemi  
| MacroRulesDefinition

Show Railroad

Item OuterAttribute VisItem MacroItem

VisItem Visibility Module ExternCrate UseDeclaration Function TypeAlias Struct
Enumeration Union ConstantItem StaticItem Trait Implementation ExternBlock

MacroItem MacroInvocationSemi MacroRulesDefinition

[items.intro]

An _item_ is a component of a crate. Items are organized within a crate by a
nested set of modules. Every crate has a single “outermost” anonymous module;
all further items within the crate have paths within the module tree of the
crate.

[items.static-def]

Items are entirely determined at compile-time, generally remain fixed during
execution, and may reside in read-only memory.

[items.kinds]

There are several kinds of items:

  * modules
  * `extern crate` declarations
  * `use` declarations
  * function definitions
  * type alias definitions
  * struct definitions
  * enumeration definitions
  * union definitions
  * constant items
  * static items
  * trait definitions
  * implementations
  * `extern` blocks

[items.locations]

Items may be declared in the root of the crate, a module, or a block
expression.

[items.associated-locations]

A subset of items, called associated items, may be declared in traits and
implementations.

[items.extern-locations]

A subset of items, called external items, may be declared in `extern` blocks.

[items.decl-order]

Items may be defined in any order, with the exception of `macro_rules` which
has its own scoping behavior.

[items.name-resolution]

Name resolution of item names allows items to be defined before or after where
the item is referred to in the module or block.

See item scopes for information on the scoping rules of items.

[items.mod]

# Modules

[items.mod.syntax]

**Syntax**  
Module →  
unsafe? mod IDENTIFIER ;  
| unsafe? mod IDENTIFIER {  
InnerAttribute*  
Item*  
}

Show Railroad

Module unsafe mod IDENTIFIER ; unsafe mod IDENTIFIER { InnerAttribute Item }

[items.mod.intro]

A module is a container for zero or more items.

[items.mod.def]

A _module item_ is a module, surrounded in braces, named, and prefixed with
the keyword `mod`. A module item introduces a new, named module into the tree
of modules making up a crate.

[items.mod.nesting]

Modules can nest arbitrarily.

An example of a module:

    
    
    #![allow(unused)]
    fn main() {
    mod math {
        type Complex = (f64, f64);
        fn sin(f: f64) -> f64 {
            /* ... */
          unimplemented!();
        }
        fn cos(f: f64) -> f64 {
            /* ... */
          unimplemented!();
        }
        fn tan(f: f64) -> f64 {
            /* ... */
          unimplemented!();
        }
    }
    }

[items.mod.namespace]

Modules are defined in the type namespace of the module or block where they
are located.

[items.mod.multiple-items]

It is an error to define multiple items with the same name in the same
namespace within a module. See the scopes chapter for more details on
restrictions and shadowing behavior.

[items.mod.unsafe]

The `unsafe` keyword is syntactically allowed to appear before the `mod`
keyword, but it is rejected at a semantic level. This allows macros to consume
the syntax and make use of the `unsafe` keyword, before removing it from the
token stream.

[items.mod.outlined]

## Module source filenames

[items.mod.outlined.intro]

A module without a body is loaded from an external file. When the module does
not have a `path` attribute, the path to the file mirrors the logical module
path.

[items.mod.outlined.search]

Ancestor module path components are directories, and the module’s contents are
in a file with the name of the module plus the `.rs` extension. For example,
the following module structure can have this corresponding filesystem
structure:

Module Path| Filesystem Path| File Contents  
---|---|---  
`crate`| `lib.rs`| `mod util;`  
`crate::util`| `util.rs`| `mod config;`  
`crate::util::config`| `util/config.rs`|  
  
[items.mod.outlined.search-mod]

Module filenames may also be the name of the module as a directory with the
contents in a file named `mod.rs` within that directory. The above example can
alternately be expressed with `crate::util`’s contents in a file named
`util/mod.rs`. It is not allowed to have both `util.rs` and `util/mod.rs`.

> Note
>
> Prior to `rustc` 1.30, using `mod.rs` files was the way to load a module
> with nested children. It is encouraged to use the new naming convention as
> it is more consistent, and avoids having many files named `mod.rs` within a
> project.

[items.mod.outlined.path]

### The `path` attribute

[items.mod.outlined.path.intro]

The directories and files used for loading external file modules can be
influenced with the `path` attribute.

[items.mod.outlined.path.search]

For `path` attributes on modules not inside inline module blocks, the file
path is relative to the directory the source file is located. For example, the
following code snippet would use the paths shown based on where it is located:

    
    
    #[path = "foo.rs"]
    mod c;

Source File| `c`’s File Location| `c`’s Module Path  
---|---|---  
`src/a/b.rs`| `src/a/foo.rs`| `crate::a::b::c`  
`src/a/mod.rs`| `src/a/foo.rs`| `crate::a::c`  
  
[items.mod.outlined.path.search-nested]

For `path` attributes inside inline module blocks, the relative location of
the file path depends on the kind of source file the `path` attribute is
located in. “mod-rs” source files are root modules (such as `lib.rs` or
`main.rs`) and modules with files named `mod.rs`. “non-mod-rs” source files
are all other module files. Paths for `path` attributes inside inline module
blocks in a mod-rs file are relative to the directory of the mod-rs file
including the inline module components as directories. For non-mod-rs files,
it is the same except the path starts with a directory with the name of the
non-mod-rs module. For example, the following code snippet would use the paths
shown based on where it is located:

    
    
    mod inline {
        #[path = "other.rs"]
        mod inner;
    }

Source File| `inner`’s File Location| `inner`’s Module Path  
---|---|---  
`src/a/b.rs`| `src/a/b/inline/other.rs`| `crate::a::b::inline::inner`  
`src/a/mod.rs`| `src/a/inline/other.rs`| `crate::a::inline::inner`  
  
An example of combining the above rules of `path` attributes on inline modules
and nested modules within (applies to both mod-rs and non-mod-rs files):

    
    
    #[path = "thread_files"]
    mod thread {
        // Load the `local_data` module from `thread_files/tls.rs` relative to
        // this source file's directory.
        #[path = "tls.rs"]
        mod local_data;
    }

[items.mod.attributes]

## Attributes on modules

[items.mod.attributes.intro]

Modules, like all items, accept outer attributes. They also accept inner
attributes: either after `{` for a module with a body, or at the beginning of
the source file, after the optional BOM and shebang.

[items.mod.attributes.supported]

The built-in attributes that have meaning on a module are `cfg`, `deprecated`,
[`doc`](../rustdoc/the-doc-attribute.html), the lint check attributes, `path`,
and `no_implicit_prelude`. Modules also accept macro attributes.

[items.extern-crate]

# Extern crate declarations

[items.extern-crate.syntax]

**Syntax**  
ExternCrate → extern crate CrateRef AsClause? ;

CrateRef → IDENTIFIER | self

AsClause → as ( IDENTIFIER | _ )

Show Railroad

ExternCrate extern crate CrateRef AsClause ;

CrateRef IDENTIFIER self

AsClause as IDENTIFIER _

[items.extern-crate.intro]

An _`extern crate` declaration_ specifies a dependency on an external crate.

[items.extern-crate.namespace]

The external crate is then bound into the declaring scope as the given
identifier in the type namespace.

[items.extern-crate.extern-prelude]

Additionally, if the `extern crate` appears in the crate root, then the crate
name is also added to the extern prelude, making it automatically in scope in
all modules.

[items.extern-crate.as]

The `as` clause can be used to bind the imported crate to a different name.

[items.extern-crate.lookup]

The external crate is resolved to a specific `soname` at compile time, and a
runtime linkage requirement to that `soname` is passed to the linker for
loading at runtime. The `soname` is resolved at compile time by scanning the
compiler’s library path and matching the optional `crate_name` provided
against the `crate_name` attributes that were declared on the external crate
when it was compiled. If no `crate_name` is provided, a default `name`
attribute is assumed, equal to the identifier given in the `extern crate`
declaration.

[items.extern-crate.self]

The `self` crate may be imported which creates a binding to the current crate.
In this case the `as` clause must be used to specify the name to bind it to.

Three examples of `extern crate` declarations:

    
    
    extern crate pcre;
    
    extern crate std; // equivalent to: extern crate std as std;
    
    extern crate std as ruststd; // linking to 'std' under another name

[items.extern-crate.name-restrictions]

When naming Rust crates, hyphens are disallowed. However, Cargo packages may
make use of them. In such case, when `Cargo.toml` doesn’t specify a crate
name, Cargo will transparently replace `-` with `_` (Refer to [RFC
940](https://github.com/rust-lang/rfcs/blob/master/text/0940-hyphens-
considered-harmful.md) for more details).

Here is an example:

    
    
    // Importing the Cargo package hello-world
    extern crate hello_world; // hyphen replaced with an underscore

[items.extern-crate.underscore]

## Underscore imports

[items.extern-crate.underscore.intro]

An external crate dependency can be declared without binding its name in scope
by using an underscore with the form `extern crate foo as _`. This may be
useful for crates that only need to be linked, but are never referenced, and
will avoid being reported as unused.

[items.extern-crate.underscore.macro_use]

The `macro_use` attribute works as usual and imports the macro names into the
`macro_use` prelude.

[items.extern-crate.no_link]

## The `no_link` attribute

[items.extern-crate.no_link.intro]

The _`no_link` attribute_ may be applied to an `extern crate` item to prevent
linking the crate.

> Note
>
> This is helpful, e.g., when only the macros of a crate are needed.

> Example
>  
>  
>     #[no_link]
>     extern crate other_crate;
>  
>     other_crate::some_macro!();

[items.extern-crate.no_link.syntax]

The `no_link` attribute uses the MetaWord syntax.

[items.extern-crate.no_link.allowed-positions]

The `no_link` attribute may only be applied to an `extern crate` declaration.

> Note
>
> `rustc` ignores use in other positions but lints against it. This may become
> an error in the future.

[items.extern-crate.no_link.duplicates]

Only the first use of `no_link` on an `extern crate` declaration has effect.

> Note
>
> `rustc` lints against any use following the first. This may become an error
> in the future.

[items.use]

# Use declarations

[items.use.syntax]

**Syntax**  
UseDeclaration → use UseTree ;

UseTree →  
( SimplePath? :: )? *  
| ( SimplePath? :: )? { ( UseTree ( , UseTree )* ,? )? }  
| SimplePath ( as ( IDENTIFIER | _ ) )?

Show Railroad

UseDeclaration use UseTree ;

UseTree SimplePath :: * SimplePath :: { UseTree , UseTree , } SimplePath as
IDENTIFIER _

[items.use.intro]

A _use declaration_ creates one or more local name bindings synonymous with
some other path. Usually a `use` declaration is used to shorten the path
required to refer to a module item. These declarations may appear in modules
and blocks, usually at the top. A `use` declaration is also sometimes called
an _import_ , or, if it is public, a _re-export_.

[items.use.forms]

Use declarations support a number of convenient shortcuts:

[items.use.forms.multiple]

  * Simultaneously binding a list of paths with a common prefix, using the brace syntax `use a::b::{c, d, e::f, g::h::i};`

[items.use.forms.self]

  * Simultaneously binding a list of paths with a common prefix and their common parent module, using the `self` keyword, such as `use a::b::{self, c, d::e};`

[items.use.forms.as]

  * Rebinding the target name as a new local name, using the syntax `use p::q::r as x;`. This can also be used with the last two features: `use a::b::{self as ab, c as abc}`.

[items.use.forms.glob]

  * Binding all paths matching a given prefix, using the asterisk wildcard syntax `use a::b::*;`.

[items.use.forms.nesting]

  * Nesting groups of the previous features multiple times, such as `use a::b::{self as ab, c, d::{*, e::f}};`

An example of `use` declarations:

    
    
    use std::collections::hash_map::{self, HashMap};
    
    fn foo<T>(_: T){}
    fn bar(map1: HashMap<String, usize>, map2: hash_map::HashMap<String, usize>){}
    
    fn main() {
        // use declarations can also exist inside of functions
        use std::option::Option::{Some, None};
    
        // Equivalent to 'foo(vec![std::option::Option::Some(1.0f64),
        // std::option::Option::None]);'
        foo(vec![Some(1.0f64), None]);
    
        // Both `hash_map` and `HashMap` are in scope.
        let map1 = HashMap::new();
        let map2 = hash_map::HashMap::new();
        bar(map1, map2);
    }

[items.use.visibility]

## `use` Visibility

[items.use.visibility.intro]

Like items, `use` declarations are private to the containing module, by
default. Also like items, a `use` declaration can be public, if qualified by
the `pub` keyword. Such a `use` declaration serves to _re-export_ a name. A
public `use` declaration can therefore _redirect_ some public name to a
different target definition: even a definition with a private canonical path,
inside a different module.

[items.use.visibility.unambiguous]

If a sequence of such redirections form a cycle or cannot be resolved
unambiguously, they represent a compile-time error.

An example of re-exporting:

    
    
    mod quux {
        pub use self::foo::{bar, baz};
        pub mod foo {
            pub fn bar() {}
            pub fn baz() {}
        }
    }
    
    fn main() {
        quux::bar();
        quux::baz();
    }

In this example, the module `quux` re-exports two public names defined in
`foo`.

[items.use.path]

## `use` Paths

[items.use.path.intro]

The paths that are allowed in a `use` item follow the SimplePath grammar and
are similar to the paths that may be used in an expression. They may create
bindings for:

  * Nameable items
  * Enum variants
  * Built-in types
  * Attributes
  * Derive macros
  * `macro_rules`

[items.use.path.disallowed]

They cannot import associated items, generic parameters, local variables,
paths with `Self`, or tool attributes. More restrictions are described below.

[items.use.path.namespace]

`use` will create bindings for all namespaces from the imported entities, with
the exception that a `self` import will only import from the type namespace
(as described below). For example, the following illustrates creating bindings
for the same name in two namespaces:

    
    
    #![allow(unused)]
    fn main() {
    mod stuff {
        pub struct Foo(pub i32);
    }
    
    // Imports the `Foo` type and the `Foo` constructor.
    use stuff::Foo;
    
    fn example() {
        let ctor = Foo; // Uses `Foo` from the value namespace.
        let x: Foo = ctor(123); // Uses `Foo` From the type namespace.
    }
    }

[items.use.path.edition2018]

> 2018 Edition differences
>
> In the 2015 edition, `use` paths are relative to the crate root. For
> example:
>  
>  
>     mod foo {
>         pub mod example { pub mod iter {} }
>         pub mod baz { pub fn foobaz() {} }
>     }
>     mod bar {
>         // Resolves `foo` from the crate root.
>         use foo::example::iter;
>         // The `::` prefix explicitly resolves `foo`
>         // from the crate root.
>         use ::foo::baz::foobaz;
>     }
>  
>     fn main() {}
>
> The 2015 edition does not allow use declarations to reference the extern
> prelude. Thus, `extern crate` declarations are still required in 2015 to
> reference an external crate in a `use` declaration. Beginning with the 2018
> edition, `use` declarations can specify an external crate dependency the
> same way `extern crate` can.

[items.use.as]

## `as` renames

The `as` keyword can be used to change the name of an imported entity. For
example:

    
    
    #![allow(unused)]
    fn main() {
    // Creates a non-public alias `bar` for the function `foo`.
    use inner::foo as bar;
    
    mod inner {
        pub fn foo() {}
    }
    }

[items.use.multiple-syntax]

## Brace syntax

[items.use.multiple-syntax.intro]

Braces can be used in the last segment of the path to import multiple entities
from the previous segment, or, if there are no previous segments, from the
current scope. Braces can be nested, creating a tree of paths, where each
grouping of segments is logically combined with its parent to create a full
path.

    
    
    #![allow(unused)]
    fn main() {
    // Creates bindings to:
    // - `std::collections::BTreeSet`
    // - `std::collections::hash_map`
    // - `std::collections::hash_map::HashMap`
    use std::collections::{BTreeSet, hash_map::{self, HashMap}};
    }

[items.use.multiple-syntax.empty]

An empty brace does not import anything, though the leading path is validated
that it is accessible.

[items.use.multiple-syntax.edition2018]

> 2018 Edition differences
>
> In the 2015 edition, paths are relative to the crate root, so an import such
> as `use {foo, bar};` will import the names `foo` and `bar` from the crate
> root, whereas starting in 2018, those names are relative to the current
> scope.

[items.use.self]

## `self` imports

[items.use.self.intro]

The keyword `self` may be used within brace syntax to create a binding of the
parent entity under its own name.

    
    
    mod stuff {
        pub fn foo() {}
        pub fn bar() {}
    }
    mod example {
        // Creates a binding for `stuff` and `foo`.
        use crate::stuff::{self, foo};
        pub fn baz() {
            foo();
            stuff::bar();
        }
    }
    fn main() {}

[items.use.self.namespace]

`self` only creates a binding from the type namespace of the parent entity.
For example, in the following, only the `foo` mod is imported:

    
    
    mod bar {
        pub mod foo {}
        pub fn foo() {}
    }
    
    // This only imports the module `foo`. The function `foo` lives in
    // the value namespace and is not imported.
    use bar::foo::{self};
    
    fn main() {
        foo(); //~ ERROR `foo` is a module
    }

> Note
>
> `self` may also be used as the first segment of a path. The usage of `self`
> as the first segment and inside a `use` brace is logically the same; it
> means the current module of the parent segment, or the current module if
> there is no parent segment. See `self` in the paths chapter for more
> information on the meaning of a leading `self`.

[items.use.glob]

## Glob imports

[items.use.glob.intro]

The `*` character may be used as the last segment of a `use` path to import
all importable entities from the entity of the preceding segment. For example:

    
    
    #![allow(unused)]
    fn main() {
    // Creates a non-public alias to `bar`.
    use foo::*;
    
    mod foo {
        fn i_am_private() {}
        enum Example {
            V1,
            V2,
        }
        pub fn bar() {
            // Creates local aliases to `V1` and `V2`
            // of the `Example` enum.
            use Example::*;
            let x = V1;
        }
    }
    }

[items.use.glob.shadowing]

Items and named imports are allowed to shadow names from glob imports in the
same namespace. That is, if there is a name already defined by another item in
the same namespace, the glob import will be shadowed. For example:

    
    
    #![allow(unused)]
    fn main() {
    // This creates a binding to the `clashing::Foo` tuple struct
    // constructor, but does not import its type because that would
    // conflict with the `Foo` struct defined here.
    //
    // Note that the order of definition here is unimportant.
    use clashing::*;
    struct Foo {
        field: f32,
    }
    
    fn do_stuff() {
        // Uses the constructor from `clashing::Foo`.
        let f1 = Foo(123);
        // The struct expression uses the type from
        // the `Foo` struct defined above.
        let f2 = Foo { field: 1.0 };
        // `Bar` is also in scope due to the glob import.
        let z = Bar {};
    }
    
    mod clashing {
        pub struct Foo(pub i32);
        pub struct Bar {}
    }
    }

> Note
>
> For areas where shadowing is not allowed, see name resolution ambiguities.

[items.use.glob.last-segment-only]

`*` cannot be used as the first or intermediate segments.

[items.use.glob.self-import]

`*` cannot be used to import a module’s contents into itself (such as `use
self::*;`).

[items.use.glob.edition2018]

> 2018 Edition differences
>
> In the 2015 edition, paths are relative to the crate root, so an import such
> as `use *;` is valid, and it means to import everything from the crate root.
> This cannot be used in the crate root itself.

[items.use.as-underscore]

## Underscore imports

[items.use.as-underscore.intro]

Items can be imported without binding to a name by using an underscore with
the form `use path as _`. This is particularly useful to import a trait so
that its methods may be used without importing the trait’s symbol, for example
if the trait’s symbol may conflict with another symbol. Another example is to
link an external crate without importing its name.

[items.use.as-underscore.glob]

Asterisk glob imports will import items imported with `_` in their unnameable
form.

    
    
    mod foo {
        pub trait Zoo {
            fn zoo(&self) {}
        }
    
        impl<T> Zoo for T {}
    }
    
    use self::foo::Zoo as _;
    struct Zoo;  // Underscore import avoids name conflict with this item.
    
    fn main() {
        let z = Zoo;
        z.zoo();
    }

[items.use.as-underscore.macro]

The unique, unnameable symbols are created after macro expansion so that
macros may safely emit multiple references to `_` imports. For example, the
following should not produce an error:

    
    
    #![allow(unused)]
    fn main() {
    macro_rules! m {
        ($item: item) => { $item $item }
    }
    
    m!(use std as _;);
    // This expands to:
    // use std as _;
    // use std as _;
    }

[items.use.restrictions]

## Restrictions

The following are restrictions for valid `use` declarations:

[items.use.restrictions.crate]

  * `use crate;` must use `as` to define the name to which to bind the crate root.

[items.use.restrictions.self]

  * `use {self};` is an error; there must be a leading segment when using `self`.

[items.use.restrictions.duplicate-name]

  * As with any item definition, `use` imports cannot create duplicate bindings of the same name in the same namespace in a module or block.

[items.use.restrictions.macro-crate]

  * `use` paths with `$crate` are not allowed in a `macro_rules` expansion.

[items.use.restrictions.variant]

  * `use` paths cannot refer to enum variants through a type alias. For example: 
        
        #![allow(unused)]
        fn main() {
        enum MyEnum {
            MyVariant
        }
        type TypeAlias = MyEnum;
        
        use MyEnum::MyVariant; //~ OK
        use TypeAlias::MyVariant; //~ ERROR
        }

[items.fn]

# Functions

[items.fn.syntax]

**Syntax**  
Function →  
FunctionQualifiers fn IDENTIFIER GenericParams?  
( FunctionParameters? )  
FunctionReturnType? WhereClause?  
( BlockExpression | ; )

FunctionQualifiers → const? async?​1 ItemSafety?​2 ( extern Abi? )?

ItemSafety → safe​3 | unsafe

Abi → STRING_LITERAL | RAW_STRING_LITERAL

FunctionParameters →  
SelfParam ,?  
| ( SelfParam , )? FunctionParam ( , FunctionParam )* ,?

SelfParam → OuterAttribute* ( ShorthandSelf | TypedSelf )

ShorthandSelf → ( & | & Lifetime )? mut? self

TypedSelf → mut? self : Type

FunctionParam → OuterAttribute* ( FunctionParamPattern | ... | Type​4 )

FunctionParamPattern → PatternNoTopAlt : ( Type | ... )

FunctionReturnType → -> Type

Show Railroad

Function FunctionQualifiers fn IDENTIFIER GenericParams ( FunctionParameters )
FunctionReturnType WhereClause BlockExpression ;

FunctionQualifiers const async ItemSafety extern Abi

ItemSafety safe unsafe

Abi STRING_LITERAL RAW_STRING_LITERAL

FunctionParameters SelfParam , SelfParam , FunctionParam , FunctionParam ,

SelfParam OuterAttribute ShorthandSelf TypedSelf

ShorthandSelf & & Lifetime mut self

TypedSelf mut self : Type

FunctionParam OuterAttribute FunctionParamPattern ... Type

FunctionParamPattern PatternNoTopAlt : Type ...

FunctionReturnType -> Type

[items.fn.intro]

A _function_ consists of a block (that’s the _body_ of the function), along
with a name, a set of parameters, and an output type. Other than a name, all
these are optional.

[items.fn.namespace]

Functions are declared with the keyword `fn` which defines the given name in
the value namespace of the module or block where it is located.

[items.fn.signature]

Functions may declare a set of _input_ _variables_ as parameters, through
which the caller passes arguments into the function, and the _output_ _type_
of the value the function will return to its caller on completion.

[items.fn.implicit-return]

If the output type is not explicitly stated, it is the unit type.

[items.fn.fn-item-type]

When referred to, a _function_ yields a first-class _value_ of the
corresponding zero-sized _function item type_, which when called evaluates to
a direct call to the function.

For example, this is a simple function:

    
    
    #![allow(unused)]
    fn main() {
    fn answer_to_life_the_universe_and_everything() -> i32 {
        return 42;
    }
    }

[items.fn.safety-qualifiers]

The `safe` function is semantically only allowed when used in an `extern`
block.

[items.fn.params]

## Function parameters

[items.fn.params.intro]

Function parameters are irrefutable patterns, so any pattern that is valid in
an else-less `let` binding is also valid as a parameter:

    
    
    #![allow(unused)]
    fn main() {
    fn first((value, _): (i32, i32)) -> i32 { value }
    }

[items.fn.params.self-pat]

If the first parameter is a SelfParam, this indicates that the function is a
method.

[items.fn.params.self-restriction]

Functions with a self parameter may only appear as an associated function in a
trait or implementation.

[items.fn.params.varargs]

A parameter with the `...` token indicates a variadic function, and may only
be used as the last parameter of an external block function. The variadic
parameter may have an optional identifier, such as `args: ...`.

[items.fn.body]

## Function body

[items.fn.body.intro]

The body block of a function is conceptually wrapped in another block that
first binds the argument patterns and then `return`s the value of the
function’s body. This means that the tail expression of the block, if
evaluated, ends up being returned to the caller. As usual, an explicit return
expression within the body of the function will short-cut that implicit
return, if reached.

For example, the function above behaves as if it was written as:

    
    
    // argument_0 is the actual first argument passed from the caller
    let (value, _) = argument_0;
    return {
        value
    };

[items.fn.body.bodyless]

Functions without a body block are terminated with a semicolon. This form may
only appear in a trait or external block.

[items.fn.generics]

## Generic functions

[items.fn.generics.intro]

A _generic function_ allows one or more _parameterized types_ to appear in its
signature. Each type parameter must be explicitly declared in an angle-
bracket-enclosed and comma-separated list, following the function name.

    
    
    #![allow(unused)]
    fn main() {
    // foo is generic over A and B
    
    fn foo<A, B>(x: A, y: B) {
    }
    }

[items.fn.generics.param-names]

Inside the function signature and body, the name of the type parameter can be
used as a type name.

[items.fn.generics.param-bounds]

Trait bounds can be specified for type parameters to allow methods with that
trait to be called on values of that type. This is specified using the `where`
syntax:

    
    
    #![allow(unused)]
    fn main() {
    use std::fmt::Debug;
    fn foo<T>(x: T) where T: Debug {
    }
    }

[items.fn.generics.mono]

When a generic function is referenced, its type is instantiated based on the
context of the reference. For example, calling the `foo` function here:

    
    
    #![allow(unused)]
    fn main() {
    use std::fmt::Debug;
    
    fn foo<T>(x: &[T]) where T: Debug {
        // details elided
    }
    
    foo(&[1, 2]);
    }

will instantiate type parameter `T` with `i32`.

[items.fn.generics.explicit-arguments]

The type parameters can also be explicitly supplied in a trailing path
component after the function name. This might be necessary if there is not
sufficient context to determine the type parameters. For example,
`mem::size_of::<u32>() == 4`.

[items.fn.extern]

## Extern function qualifier

[items.fn.extern.intro]

The `extern` function qualifier allows providing function _definitions_ that
can be called with a particular ABI:

    
    
    extern "ABI" fn foo() { /* ... */ }

[items.fn.extern.def]

These are often used in combination with external block items which provide
function _declarations_ that can be used to call functions without providing
their _definition_ :

    
    
    unsafe extern "ABI" {
      unsafe fn foo(); /* no body */
      safe fn bar(); /* no body */
    }
    unsafe { foo() };
    bar();

[items.fn.extern.default-abi]

When `"extern" Abi?*` is omitted from `FunctionQualifiers` in function items,
the ABI `"Rust"` is assigned. For example:

    
    
    #![allow(unused)]
    fn main() {
    fn foo() {}
    }

is equivalent to:

    
    
    #![allow(unused)]
    fn main() {
    extern "Rust" fn foo() {}
    }

[items.fn.extern.foreign-call]

Functions can be called by foreign code, and using an ABI that differs from
Rust allows, for example, to provide functions that can be called from other
programming languages like C:

    
    
    #![allow(unused)]
    fn main() {
    // Declares a function with the "C" ABI
    extern "C" fn new_i32() -> i32 { 0 }
    
    // Declares a function with the "stdcall" ABI
    #[cfg(any(windows, target_arch = "x86"))]
    extern "stdcall" fn new_i32_stdcall() -> i32 { 0 }
    }

[items.fn.extern.default-extern]

Just as with external block, when the `extern` keyword is used and the `"ABI"`
is omitted, the ABI used defaults to `"C"`. That is, this:

    
    
    #![allow(unused)]
    fn main() {
    extern fn new_i32() -> i32 { 0 }
    let fptr: extern fn() -> i32 = new_i32;
    }

is equivalent to:

    
    
    #![allow(unused)]
    fn main() {
    extern "C" fn new_i32() -> i32 { 0 }
    let fptr: extern "C" fn() -> i32 = new_i32;
    }

[items.fn.extern.unwind]

### Unwinding

[items.fn.extern.unwind.intro]

Most ABI strings come in two variants, one with an `-unwind` suffix and one
without. The `Rust` ABI always permits unwinding, so there is no `Rust-unwind`
ABI. The choice of ABI, together with the runtime panic handler, determines
the behavior when unwinding out of a function.

[items.fn.extern.unwind.behavior]

The table below indicates the behavior of an unwinding operation reaching each
type of ABI boundary (function declaration or definition using the
corresponding ABI string). Note that the Rust runtime is not affected by, and
cannot have an effect on, any unwinding that occurs entirely within another
language’s runtime, that is, unwinds that are thrown and caught without
reaching a Rust ABI boundary.

The `panic`-unwind column refers to panicking via the `panic!` macro and
similar standard library mechanisms, as well as to any other Rust operations
that cause a panic, such as out-of-bounds array indexing or integer overflow.

The “unwinding” ABI category refers to `"Rust"` (the implicit ABI of Rust
functions not marked `extern`), `"C-unwind"`, and any other ABI with `-unwind`
in its name. The “non-unwinding” ABI category refers to all other ABI strings,
including `"C"` and `"stdcall"`.

Native unwinding is defined per-target. On targets that support throwing and
catching C++ exceptions, it refers to the mechanism used to implement this
feature. Some platforms implement a form of unwinding referred to as [“forced
unwinding”](https://rust-lang.github.io/rfcs/2945-c-unwind-abi.html#forced-
unwinding); `longjmp` on Windows and `pthread_exit` in `glibc` are implemented
this way. Forced unwinding is explicitly excluded from the “Native unwind”
column in the table.

panic runtime| ABI| `panic`-unwind| Native unwind (unforced)  
---|---|---|---  
`panic=unwind`| unwinding| unwind| unwind  
`panic=unwind`| non-unwinding| abort (see notes below)| undefined behavior  
`panic=abort`| unwinding| `panic` aborts without unwinding| abort  
`panic=abort`| non-unwinding| `panic` aborts without unwinding| undefined
behavior  
  
[items.fn.extern.abort]

With `panic=unwind`, when a `panic` is turned into an abort by a non-unwinding
ABI boundary, either no destructors (`Drop` calls) will run, or all
destructors up until the ABI boundary will run. It is unspecified which of
those two behaviors will happen.

For other considerations and limitations regarding unwinding across FFI
boundaries, see the relevant section in the Panic documentation.

[items.fn.const]

## Const functions

See const functions for the definition of const functions.

[items.fn.async]

## Async functions

[items.fn.async.intro]

Functions may be qualified as async, and this can also be combined with the
`unsafe` qualifier:

    
    
    #![allow(unused)]
    fn main() {
    async fn regular_example() { }
    async unsafe fn unsafe_example() { }
    }

[items.fn.async.future]

Async functions do no work when called: instead, they capture their arguments
into a future. When polled, that future will execute the function’s body.

[items.fn.async.desugar-brief]

An async function is roughly equivalent to a function that returns `impl
Future` and with an `async move` block as its body:

    
    
    #![allow(unused)]
    fn main() {
    // Source
    async fn example(x: &str) -> usize {
        x.len()
    }
    }

is roughly equivalent to:

    
    
    #![allow(unused)]
    fn main() {
    use std::future::Future;
    // Desugared
    fn example<'a>(x: &'a str) -> impl Future<Output = usize> + 'a {
        async move { x.len() }
    }
    }

[items.fn.async.desugar]

The actual desugaring is more complex:

[items.fn.async.lifetime-capture]

  * The return type in the desugaring is assumed to capture all lifetime parameters from the `async fn` declaration. This can be seen in the desugared example above, which explicitly outlives, and hence captures, `'a`.

[items.fn.async.param-capture]

  * The `async move` block in the body captures all function parameters, including those that are unused or bound to a `_` pattern. This ensures that function parameters are dropped in the same order as they would be if the function were not async, except that the drop occurs when the returned future has been fully awaited.

For more information on the effect of async, see `async` blocks.

[items.fn.async.edition2018]

> 2018 Edition differences
>
> Async functions are only available beginning with Rust 2018.

[items.fn.async.safety]

### Combining `async` and `unsafe`

[items.fn.async.safety.intro]

It is legal to declare a function that is both async and unsafe. The resulting
function is unsafe to call and (like any async function) returns a future.
This future is just an ordinary future and thus an `unsafe` context is not
required to “await” it:

    
    
    #![allow(unused)]
    fn main() {
    // Returns a future that, when awaited, dereferences `x`.
    //
    // Soundness condition: `x` must be safe to dereference until
    // the resulting future is complete.
    async unsafe fn unsafe_example(x: *const i32) -> i32 {
      *x
    }
    
    async fn safe_example() {
        // An `unsafe` block is required to invoke the function initially:
        let p = 22;
        let future = unsafe { unsafe_example(&p) };
    
        // But no `unsafe` block required here. This will
        // read the value of `p`:
        let q = future.await;
    }
    }

Note that this behavior is a consequence of the desugaring to a function that
returns an `impl Future` – in this case, the function we desugar to is an
`unsafe` function, but the return value remains the same.

Unsafe is used on an async function in precisely the same way that it is used
on other functions: it indicates that the function imposes some additional
obligations on its caller to ensure soundness. As in any other unsafe
function, these conditions may extend beyond the initial call itself – in the
snippet above, for example, the `unsafe_example` function took a pointer `x`
as argument, and then (when awaited) dereferenced that pointer. This implies
that `x` would have to be valid until the future is finished executing, and it
is the caller’s responsibility to ensure that.

[items.fn.attributes]

## Attributes on functions

[items.fn.attributes.intro]

Outer attributes are allowed on functions. Inner attributes are allowed
directly after the `{` inside its body block.

This example shows an inner attribute on a function. The function is
documented with just the word “Example”.

    
    
    #![allow(unused)]
    fn main() {
    fn documented() {
        #![doc = "Example"]
    }
    }

> Note
>
> Except for lints, it is idiomatic to only use outer attributes on function
> items.

[items.fn.attributes.builtin-attributes]

The attributes that have meaning on a function are:

  * `cfg_attr`
  * `cfg`
  * `cold`
  * `deprecated`
  * [`doc`](../rustdoc/the-doc-attribute.html)
  * `export_name`
  * `inline`
  * `link_section`
  * `must_use`
  * `no_mangle`
  * Lint check attributes
  * Procedural macro attributes
  * Testing attributes

[items.fn.param-attributes]

## Attributes on function parameters

[items.fn.param-attributes.intro]

Outer attributes are allowed on function parameters and the permitted built-in
attributes are restricted to `cfg`, `cfg_attr`, `allow`, `warn`, `deny`, and
`forbid`.

    
    
    #![allow(unused)]
    fn main() {
    fn len(
        #[cfg(windows)] slice: &[u16],
        #[cfg(not(windows))] slice: &[u8],
    ) -> usize {
        slice.len()
    }
    }

[items.fn.param-attributes.parsed-attributes]

Inert helper attributes used by procedural macro attributes applied to items
are also allowed but be careful to not include these inert attributes in your
final `TokenStream`.

For example, the following code defines an inert `some_inert_attribute`
attribute that is not formally defined anywhere and the
`some_proc_macro_attribute` procedural macro is responsible for detecting its
presence and removing it from the output token stream.

    
    
    #[some_proc_macro_attribute]
    fn foo_oof(#[some_inert_attribute] arg: u8) {
    }

* * *

  1. The `async` qualifier is not allowed in the 2015 edition. ↩

  2. _Relevant to editions earlier than Rust 2024_ : Within `extern` blocks, the `safe` or `unsafe` function qualifier is only allowed when the `extern` is qualified as `unsafe`. ↩

  3. The `safe` function qualifier is only allowed semantically within `extern` blocks. ↩

  4. Function parameters with only a type are only allowed in an associated function of a trait item in the 2015 edition. ↩

[items.type]

# Type aliases

[items.type.syntax]

**Syntax**  
TypeAlias →  
type IDENTIFIER GenericParams? ( : TypeParamBounds )?  
WhereClause?  
( = Type WhereClause? )? ;

Show Railroad

TypeAlias type IDENTIFIER GenericParams : TypeParamBounds WhereClause = Type
WhereClause ;

[items.type.intro]

A _type alias_ defines a new name for an existing type in the type namespace
of the module or block where it is located. Type aliases are declared with the
keyword `type`. Every value has a single, specific type, but may implement
several different traits, and may be compatible with several different type
constraints.

For example, the following defines the type `Point` as a synonym for the type
`(u8, u8)`, the type of pairs of unsigned 8 bit integers:

    
    
    #![allow(unused)]
    fn main() {
    type Point = (u8, u8);
    let p: Point = (41, 68);
    }

[items.type.constructor-alias]

A type alias to a tuple-struct or unit-struct cannot be used to qualify that
type’s constructor:

    
    
    #![allow(unused)]
    fn main() {
    struct MyStruct(u32);
    
    use MyStruct as UseAlias;
    type TypeAlias = MyStruct;
    
    let _ = UseAlias(5); // OK
    let _ = TypeAlias(5); // Doesn't work
    }

[items.type.associated-type]

A type alias, when not used as an associated type, must include a Type and may
not include TypeParamBounds.

[items.type.associated-trait]

A type alias, when used as an associated type in a trait, must not include a
Type specification but may include TypeParamBounds.

[items.type.associated-impl]

A type alias, when used as an associated type in a trait impl, must include a
Type specification and may not include TypeParamBounds.

[items.type.deprecated]

Where clauses before the equals sign on a type alias in a trait impl (like
`type TypeAlias<T> where T: Foo = Bar<T>`) are deprecated. Where clauses after
the equals sign (like `type TypeAlias<T> = Bar<T> where T: Foo`) are
preferred.

[items.struct]

# Structs

[items.struct.syntax]

**Syntax**  
Struct →  
StructStruct  
| TupleStruct

StructStruct →  
struct IDENTIFIER GenericParams? WhereClause? ( { StructFields? } | ; )

TupleStruct →  
struct IDENTIFIER GenericParams? ( TupleFields? ) WhereClause? ;

StructFields → StructField ( , StructField )* ,?

StructField → OuterAttribute* Visibility? IDENTIFIER : Type

TupleFields → TupleField ( , TupleField )* ,?

TupleField → OuterAttribute* Visibility? Type

Show Railroad

Struct StructStruct TupleStruct

StructStruct struct IDENTIFIER GenericParams WhereClause { StructFields } ;

TupleStruct struct IDENTIFIER GenericParams ( TupleFields ) WhereClause ;

StructFields StructField , StructField ,

StructField OuterAttribute Visibility IDENTIFIER : Type

TupleFields TupleField , TupleField ,

TupleField OuterAttribute Visibility Type

[items.struct.intro]

A _struct_ is a nominal struct type defined with the keyword `struct`.

[items.struct.namespace]

A struct declaration defines the given name in the type namespace of the
module or block where it is located.

An example of a `struct` item and its use:

    
    
    #![allow(unused)]
    fn main() {
    struct Point {x: i32, y: i32}
    let p = Point {x: 10, y: 11};
    let px: i32 = p.x;
    }

[items.struct.tuple]

A _tuple struct_ is a nominal tuple type, and is also defined with the keyword
`struct`. In addition to defining a type, it also defines a constructor of the
same name in the value namespace. The constructor is a function which can be
called to create a new instance of the struct. For example:

    
    
    #![allow(unused)]
    fn main() {
    struct Point(i32, i32);
    let p = Point(10, 11);
    let px: i32 = match p { Point(x, _) => x };
    }

[items.struct.unit]

A _unit-like struct_ is a struct without any fields, defined by leaving off
the list of fields entirely. Such a struct implicitly defines a constant of
its type with the same name. For example:

    
    
    #![allow(unused)]
    fn main() {
    struct Cookie;
    let c = [Cookie, Cookie {}, Cookie, Cookie {}];
    }

is equivalent to

    
    
    #![allow(unused)]
    fn main() {
    struct Cookie {}
    const Cookie: Cookie = Cookie {};
    let c = [Cookie, Cookie {}, Cookie, Cookie {}];
    }

[items.struct.layout]

The precise memory layout of a struct is not specified. One can specify a
particular layout using the `repr` attribute.

[items.enum]

# Enumerations

[items.enum.syntax]

**Syntax**  
Enumeration →  
enum IDENTIFIER GenericParams? WhereClause? { EnumVariants? }

EnumVariants → EnumVariant ( , EnumVariant )* ,?

EnumVariant →  
OuterAttribute* Visibility?  
IDENTIFIER ( EnumVariantTuple | EnumVariantStruct )? EnumVariantDiscriminant?

EnumVariantTuple → ( TupleFields? )

EnumVariantStruct → { StructFields? }

EnumVariantDiscriminant → = Expression

Show Railroad

Enumeration enum IDENTIFIER GenericParams WhereClause { EnumVariants }

EnumVariants EnumVariant , EnumVariant ,

EnumVariant OuterAttribute Visibility IDENTIFIER EnumVariantTuple
EnumVariantStruct EnumVariantDiscriminant

EnumVariantTuple ( TupleFields )

EnumVariantStruct { StructFields }

EnumVariantDiscriminant = Expression

[items.enum.intro]

An _enumeration_ , also referred to as an _enum_ , is a simultaneous
definition of a nominal enumerated type as well as a set of _constructors_ ,
that can be used to create or pattern-match values of the corresponding
enumerated type.

[items.enum.decl]

Enumerations are declared with the keyword `enum`.

[items.enum.namespace]

The `enum` declaration defines the enumeration type in the type namespace of
the module or block where it is located.

An example of an `enum` item and its use:

    
    
    #![allow(unused)]
    fn main() {
    enum Animal {
        Dog,
        Cat,
    }
    
    let mut a: Animal = Animal::Dog;
    a = Animal::Cat;
    }

[items.enum.constructor]

Enum constructors can have either named or unnamed fields:

    
    
    #![allow(unused)]
    fn main() {
    enum Animal {
        Dog(String, f64),
        Cat { name: String, weight: f64 },
    }
    
    let mut a: Animal = Animal::Dog("Cocoa".to_string(), 37.2);
    a = Animal::Cat { name: "Spotty".to_string(), weight: 2.7 };
    }

In this example, `Cat` is a _struct-like enum variant_ , whereas `Dog` is
simply called an enum variant.

[items.enum.fieldless]

An enum where no constructors contain fields is called a _field-less enum_.
For example, this is a fieldless enum:

    
    
    #![allow(unused)]
    fn main() {
    enum Fieldless {
        Tuple(),
        Struct{},
        Unit,
    }
    }

[items.enum.unit-only]

If a field-less enum only contains unit variants, the enum is called an _unit-
only enum_. For example:

    
    
    #![allow(unused)]
    fn main() {
    enum Enum {
        Foo = 3,
        Bar = 2,
        Baz = 1,
    }
    }

[items.enum.constructor-names]

Variant constructors are similar to struct definitions, and can be referenced
by a path from the enumeration name, including in use declarations.

[items.enum.constructor-namespace]

Each variant defines its type in the type namespace, though that type cannot
be used as a type specifier. Tuple-like and unit-like variants also define a
constructor in the value namespace.

[items.enum.struct-expr]

A struct-like variant can be instantiated with a struct expression.

[items.enum.tuple-expr]

A tuple-like variant can be instantiated with a call expression or a struct
expression.

[items.enum.path-expr]

A unit-like variant can be instantiated with a path expression or a struct
expression. For example:

    
    
    #![allow(unused)]
    fn main() {
    enum Examples {
        UnitLike,
        TupleLike(i32),
        StructLike { value: i32 },
    }
    
    use Examples::*; // Creates aliases to all variants.
    let x = UnitLike; // Path expression of the const item.
    let x = UnitLike {}; // Struct expression.
    let y = TupleLike(123); // Call expression.
    let y = TupleLike { 0: 123 }; // Struct expression using integer field names.
    let z = StructLike { value: 123 }; // Struct expression.
    }

[items.enum.discriminant]

## Discriminants

[items.enum.discriminant.intro]

Each enum instance has a _discriminant_ : an integer logically associated to
it that is used to determine which variant it holds.

[items.enum.discriminant.repr-rust]

Under the `Rust` representation, the discriminant is interpreted as an `isize`
value. However, the compiler is allowed to use a smaller type (or another
means of distinguishing variants) in its actual memory layout.

### Assigning discriminant values

[items.enum.discriminant.explicit]

#### Explicit discriminants

[items.enum.discriminant.explicit.intro]

In two circumstances, the discriminant of a variant may be explicitly set by
following the variant name with `=` and a constant expression:

[items.enum.discriminant.explicit.unit-only]

  1. if the enumeration is “unit-only”.

[items.enum.discriminant.explicit.primitive-repr]

  2. if a primitive representation is used. For example:
         
         #![allow(unused)]
         fn main() {
         #[repr(u8)]
         enum Enum {
             Unit = 3,
             Tuple(u16),
             Struct {
                 a: u8,
                 b: u16,
             } = 1,
         }
         }

[items.enum.discriminant.implicit]

#### Implicit discriminants

If a discriminant for a variant is not specified, then it is set to one higher
than the discriminant of the previous variant in the declaration. If the
discriminant of the first variant in the declaration is unspecified, then it
is set to zero.

    
    
    #![allow(unused)]
    fn main() {
    enum Foo {
        Bar,            // 0
        Baz = 123,      // 123
        Quux,           // 124
    }
    
    let baz_discriminant = Foo::Baz as u32;
    assert_eq!(baz_discriminant, 123);
    }

[items.enum.discriminant.restrictions]

#### Restrictions

[items.enum.discriminant.restrictions.same-discriminant]

It is an error when two variants share the same discriminant.

    
    
    #![allow(unused)]
    fn main() {
    enum SharedDiscriminantError {
        SharedA = 1,
        SharedB = 1
    }
    
    enum SharedDiscriminantError2 {
        Zero,       // 0
        One,        // 1
        OneToo = 1  // 1 (collision with previous!)
    }
    }

[items.enum.discriminant.restrictions.above-max-discriminant]

It is also an error to have an unspecified discriminant where the previous
discriminant is the maximum value for the size of the discriminant.

    
    
    #![allow(unused)]
    fn main() {
    #[repr(u8)]
    enum OverflowingDiscriminantError {
        Max = 255,
        MaxPlusOne // Would be 256, but that overflows the enum.
    }
    
    #[repr(u8)]
    enum OverflowingDiscriminantError2 {
        MaxMinusOne = 254, // 254
        Max,               // 255
        MaxPlusOne         // Would be 256, but that overflows the enum.
    }
    }

### Accessing discriminant

#### Via `mem::discriminant`

[items.enum.discriminant.access-opaque]

[`std::mem::discriminant`](../core/mem/fn.discriminant.html) returns an opaque
reference to the discriminant of an enum value which can be compared. This
cannot be used to get the value of the discriminant.

[items.enum.discriminant.coercion]

#### Casting

[items.enum.discriminant.coercion.intro]

If an enumeration is unit-only (with no tuple and struct variants), then its
discriminant can be directly accessed with a numeric cast; e.g.:

    
    
    #![allow(unused)]
    fn main() {
    enum Enum {
        Foo,
        Bar,
        Baz,
    }
    
    assert_eq!(0, Enum::Foo as isize);
    assert_eq!(1, Enum::Bar as isize);
    assert_eq!(2, Enum::Baz as isize);
    }

[items.enum.discriminant.coercion.fieldless]

Field-less enums can be cast if they do not have explicit discriminants, or
where only unit variants are explicit.

    
    
    #![allow(unused)]
    fn main() {
    enum Fieldless {
        Tuple(),
        Struct{},
        Unit,
    }
    
    assert_eq!(0, Fieldless::Tuple() as isize);
    assert_eq!(1, Fieldless::Struct{} as isize);
    assert_eq!(2, Fieldless::Unit as isize);
    
    #[repr(u8)]
    enum FieldlessWithDiscriminants {
        First = 10,
        Tuple(),
        Second = 20,
        Struct{},
        Unit,
    }
    
    assert_eq!(10, FieldlessWithDiscriminants::First as u8);
    assert_eq!(11, FieldlessWithDiscriminants::Tuple() as u8);
    assert_eq!(20, FieldlessWithDiscriminants::Second as u8);
    assert_eq!(21, FieldlessWithDiscriminants::Struct{} as u8);
    assert_eq!(22, FieldlessWithDiscriminants::Unit as u8);
    }

#### Pointer casting

[items.enum.discriminant.access-memory]

If the enumeration specifies a primitive representation, then the discriminant
may be reliably accessed via unsafe pointer casting:

    
    
    #![allow(unused)]
    fn main() {
    #[repr(u8)]
    enum Enum {
        Unit,
        Tuple(bool),
        Struct{a: bool},
    }
    
    impl Enum {
        fn discriminant(&self) -> u8 {
            unsafe { *(self as *const Self as *const u8) }
        }
    }
    
    let unit_like = Enum::Unit;
    let tuple_like = Enum::Tuple(true);
    let struct_like = Enum::Struct{a: false};
    
    assert_eq!(0, unit_like.discriminant());
    assert_eq!(1, tuple_like.discriminant());
    assert_eq!(2, struct_like.discriminant());
    }

[items.enum.empty]

## Zero-variant enums

[items.enum.empty.intro]

Enums with zero variants are known as _zero-variant enums_. As they have no
valid values, they cannot be instantiated.

    
    
    #![allow(unused)]
    fn main() {
    enum ZeroVariants {}
    }

[items.enum.empty.uninhabited]

Zero-variant enums are equivalent to the never type, but they cannot be
coerced into other types.

    
    
    #![allow(unused)]
    fn main() {
    enum ZeroVariants {}
    let x: ZeroVariants = panic!();
    let y: u32 = x; // mismatched type error
    }

[items.enum.variant-visibility]

## Variant visibility

Enum variants syntactically allow a Visibility annotation, but this is
rejected when the enum is validated. This allows items to be parsed with a
unified syntax across different contexts where they are used.

    
    
    #![allow(unused)]
    fn main() {
    macro_rules! mac_variant {
        ($vis:vis $name:ident) => {
            enum $name {
                $vis Unit,
    
                $vis Tuple(u8, u16),
    
                $vis Struct { f: u8 },
            }
        }
    }
    
    // Empty `vis` is allowed.
    mac_variant! { E }
    
    // This is allowed, since it is removed before being validated.
    #[cfg(false)]
    enum E {
        pub U,
        pub(crate) T(u8),
        pub(super) T { f: String }
    }
    }

[items.union]

# Unions

[items.union.syntax]

**Syntax**  
Union →  
union IDENTIFIER GenericParams? WhereClause? { StructFields? }

Show Railroad

Union union IDENTIFIER GenericParams WhereClause { StructFields }

[items.union.intro]

A union declaration uses the same syntax as a struct declaration, except with
`union` in place of `struct`.

[items.union.namespace]

A union declaration defines the given name in the type namespace of the module
or block where it is located.

    
    
    #![allow(unused)]
    fn main() {
    #[repr(C)]
    union MyUnion {
        f1: u32,
        f2: f32,
    }
    }

[items.union.common-storage]

The key property of unions is that all fields of a union share common storage.
As a result, writes to one field of a union can overwrite its other fields,
and size of a union is determined by the size of its largest field.

[items.union.field-restrictions]

Union field types are restricted to the following subset of types:

[items.union.field-copy]

  * `Copy` types

[items.union.field-references]

  * References (`&T` and `&mut T` for arbitrary `T`)

[items.union.field-manually-drop]

  * `ManuallyDrop<T>` (for arbitrary `T`)

[items.union.field-tuple]

  * Tuples and arrays containing only allowed union field types

[items.union.drop]

This restriction ensures, in particular, that union fields never need to be
dropped. Like for structs and enums, it is possible to `impl Drop` for a union
to manually define what happens when it gets dropped.

[items.union.fieldless]

Unions without any fields are not accepted by the compiler, but can be
accepted by macros.

[items.union.init]

## Initialization of a union

[items.union.init.intro]

A value of a union type can be created using the same syntax that is used for
struct types, except that it must specify exactly one field:

    
    
    #![allow(unused)]
    fn main() {
    union MyUnion { f1: u32, f2: f32 }
    
    let u = MyUnion { f1: 1 };
    }

[items.union.init.result]

The expression above creates a value of type `MyUnion` and initializes the
storage using field `f1`. The union can be accessed using the same syntax as
struct fields:

    
    
    #![allow(unused)]
    fn main() {
    union MyUnion { f1: u32, f2: f32 }
    
    let u = MyUnion { f1: 1 };
    let f = unsafe { u.f1 };
    }

[items.union.fields]

## Reading and writing union fields

[items.union.fields.intro]

Unions have no notion of an “active field”. Instead, every union access just
interprets the storage as the type of the field used for the access.

[items.union.fields.read]

Reading a union field reads the bits of the union at the field’s type.

[items.union.fields.offset]

Fields might have a non-zero offset (except when the C representation is
used); in that case the bits starting at the offset of the fields are read

[items.union.fields.validity]

It is the programmer’s responsibility to make sure that the data is valid at
the field’s type. Failing to do so results in undefined behavior. For example,
reading the value `3` from a field of the boolean type is undefined behavior.
Effectively, writing to and then reading from a union with the C
representation is analogous to a
[`transmute`](../core/intrinsics/fn.transmute.html) from the type used for
writing to the type used for reading.

[items.union.fields.read-safety]

Consequently, all reads of union fields have to be placed in `unsafe` blocks:

    
    
    #![allow(unused)]
    fn main() {
    union MyUnion { f1: u32, f2: f32 }
    let u = MyUnion { f1: 1 };
    
    unsafe {
        let f = u.f1;
    }
    }

Commonly, code using unions will provide safe wrappers around unsafe union
field accesses.

[items.union.fields.write-safety]

In contrast, writes to union fields are safe, since they just overwrite
arbitrary data, but cannot cause undefined behavior. (Note that union field
types can never have drop glue, so a union field write will never implicitly
drop anything.)

[items.union.pattern]

## Pattern matching on unions

[items.union.pattern.intro]

Another way to access union fields is to use pattern matching.

[items.union.pattern.one-field]

Pattern matching on union fields uses the same syntax as struct patterns,
except that the pattern must specify exactly one field.

[items.union.pattern.safety]

Since pattern matching is like reading the union with a particular field, it
has to be placed in `unsafe` blocks as well.

    
    
    #![allow(unused)]
    fn main() {
    union MyUnion { f1: u32, f2: f32 }
    
    fn f(u: MyUnion) {
        unsafe {
            match u {
                MyUnion { f1: 10 } => { println!("ten"); }
                MyUnion { f2 } => { println!("{}", f2); }
            }
        }
    }
    }

[items.union.pattern.subpattern]

Pattern matching may match a union as a field of a larger structure. In
particular, when using a Rust union to implement a C tagged union via FFI,
this allows matching on the tag and the corresponding field simultaneously:

    
    
    #![allow(unused)]
    fn main() {
    #[repr(u32)]
    enum Tag { I, F }
    
    #[repr(C)]
    union U {
        i: i32,
        f: f32,
    }
    
    #[repr(C)]
    struct Value {
        tag: Tag,
        u: U,
    }
    
    fn is_zero(v: Value) -> bool {
        unsafe {
            match v {
                Value { tag: Tag::I, u: U { i: 0 } } => true,
                Value { tag: Tag::F, u: U { f: num } } if num == 0.0 => true,
                _ => false,
            }
        }
    }
    }

[items.union.ref]

## References to union fields

[items.union.ref.intro]

Since union fields share common storage, gaining write access to one field of
a union can give write access to all its remaining fields.

[items.union.ref.borrow]

Borrow checking rules have to be adjusted to account for this fact. As a
result, if one field of a union is borrowed, all its remaining fields are
borrowed as well for the same lifetime.

    
    
    #![allow(unused)]
    fn main() {
    union MyUnion { f1: u32, f2: f32 }
    // ERROR: cannot borrow `u` (via `u.f2`) as mutable more than once at a time
    fn test() {
        let mut u = MyUnion { f1: 1 };
        unsafe {
            let b1 = &mut u.f1;
    //                    ---- first mutable borrow occurs here (via `u.f1`)
            let b2 = &mut u.f2;
    //                    ^^^^ second mutable borrow occurs here (via `u.f2`)
            *b1 = 5;
        }
    //  - first borrow ends here
        assert_eq!(unsafe { u.f1 }, 5);
    }
    }

[items.union.ref.usage]

As you could see, in many aspects (except for layouts, safety, and ownership)
unions behave exactly like structs, largely as a consequence of inheriting
their syntactic shape from structs. This is also true for many unmentioned
aspects of Rust language (such as privacy, name resolution, type inference,
generics, trait implementations, inherent implementations, coherence, pattern
checking, etc etc etc).

[items.const]

# Constant items

[items.const.syntax]

**Syntax**  
ConstantItem →  
const ( IDENTIFIER | _ ) : Type ( = Expression )? ;

Show Railroad

ConstantItem const IDENTIFIER _ : Type = Expression ;

[items.const.intro]

A _constant item_ is an optionally named _constant value_ which is not
associated with a specific memory location in the program.

[items.const.behavior]

Constants are essentially inlined wherever they are used, meaning that they
are copied directly into the relevant context when used. This includes usage
of constants from external crates, and non-`Copy` types. References to the
same constant are not necessarily guaranteed to refer to the same memory
address.

[items.const.namespace]

The constant declaration defines the constant value in the value namespace of
the module or block where it is located.

[items.const.static]

Constants must be explicitly typed. The type must have a `'static` lifetime:
any references in the initializer must have `'static` lifetimes. References in
the type of a constant default to `'static` lifetime; see static lifetime
elision.

[items.const.static-temporary]

A reference to a constant will have `'static` lifetime if the constant value
is eligible for promotion; otherwise, a temporary will be created.

    
    
    #![allow(unused)]
    fn main() {
    const BIT1: u32 = 1 << 0;
    const BIT2: u32 = 1 << 1;
    
    const BITS: [u32; 2] = [BIT1, BIT2];
    const STRING: &'static str = "bitstring";
    
    struct BitsNStrings<'a> {
        mybits: [u32; 2],
        mystring: &'a str,
    }
    
    const BITS_N_STRINGS: BitsNStrings<'static> = BitsNStrings {
        mybits: BITS,
        mystring: STRING,
    };
    }

[items.const.expr-omission]

The constant expression may only be omitted in a trait definition.

[items.const.destructor]

## Constants with destructors

Constants can contain destructors. Destructors are run when the value goes out
of scope.

    
    
    #![allow(unused)]
    fn main() {
    struct TypeWithDestructor(i32);
    
    impl Drop for TypeWithDestructor {
        fn drop(&mut self) {
            println!("Dropped. Held {}.", self.0);
        }
    }
    
    const ZERO_WITH_DESTRUCTOR: TypeWithDestructor = TypeWithDestructor(0);
    
    fn create_and_drop_zero_with_destructor() {
        let x = ZERO_WITH_DESTRUCTOR;
        // x gets dropped at end of function, calling drop.
        // prints "Dropped. Held 0.".
    }
    }

[items.const.unnamed]

## Unnamed constant

[items.const.unnamed.intro]

Unlike an associated constant, a free constant may be unnamed by using an
underscore instead of the name. For example:

    
    
    #![allow(unused)]
    fn main() {
    const _: () =  { struct _SameNameTwice; };
    
    // OK although it is the same name as above:
    const _: () =  { struct _SameNameTwice; };
    }

[items.const.unnamed.repetition]

As with underscore imports, macros may safely emit the same unnamed constant
in the same scope more than once. For example, the following should not
produce an error:

    
    
    #![allow(unused)]
    fn main() {
    macro_rules! m {
        ($item: item) => { $item $item }
    }
    
    m!(const _: () = (););
    // This expands to:
    // const _: () = ();
    // const _: () = ();
    }

[items.const.eval]

## Evaluation

Free constants are always evaluated at compile-time to surface panics. This
happens even within an unused function:

    
    
    #![allow(unused)]
    fn main() {
    // Compile-time panic
    const PANIC: () = std::unimplemented!();
    
    fn unused_generic_function<T>() {
        // A failing compile-time assertion
        const _: () = assert!(usize::BITS == 0);
    }
    }

[items.static]

# Static items

[items.static.syntax]

**Syntax**  
StaticItem →  
ItemSafety?​1 static mut? IDENTIFIER : Type ( = Expression )? ;

Show Railroad

StaticItem ItemSafety static mut IDENTIFIER : Type = Expression ;

[items.static.intro]

A _static item_ is similar to a constant, except that it represents an
allocation in the program that is initialized with the initializer expression.
All references and raw pointers to the static refer to the same allocation.

[items.static.lifetime]

Static items have the `static` lifetime, which outlives all other lifetimes in
a Rust program. Static items do not call `drop` at the end of the program.

[items.static.storage-disjointness]

If the `static` has a size of at least 1 byte, this allocation is disjoint
from all other such `static` allocations as well as heap allocations and
stack-allocated variables. However, the storage of immutable `static` items
can overlap with allocations that do not themselves have a unique address,
such as promoteds and `const` items.

[items.static.namespace]

The static declaration defines a static value in the value namespace of the
module or block where it is located.

[items.static.init]

The static initializer is a constant expression evaluated at compile time.
Static initializers may refer to and read from other statics. When reading
from mutable statics, they read the initial value of that static.

[items.static.read-only]

Non-`mut` static items that contain a type that is not interior mutable may be
placed in read-only memory.

[items.static.safety]

All access to a static is safe, but there are a number of restrictions on
statics:

[items.static.sync]

  * The type must have the [`Sync`](../core/marker/trait.Sync.html) trait bound to allow thread-safe access.

[items.static.init.omission]

The initializer expression must be omitted in an external block, and must be
provided for free static items.

[items.static.safety-qualifiers]

The `safe` and `unsafe` qualifiers are semantically only allowed when used in
an external block.

[items.static.generics]

## Statics & generics

A static item defined in a generic scope (for example in a blanket or default
implementation) will result in exactly one static item being defined, as if
the static definition was pulled out of the current scope into the module.
There will _not_ be one item per monomorphization.

This code:

    
    
    use std::sync::atomic::{AtomicUsize, Ordering};
    
    trait Tr {
        fn default_impl() {
            static COUNTER: AtomicUsize = AtomicUsize::new(0);
            println!("default_impl: counter was {}", COUNTER.fetch_add(1, Ordering::Relaxed));
        }
    
        fn blanket_impl();
    }
    
    struct Ty1 {}
    struct Ty2 {}
    
    impl<T> Tr for T {
        fn blanket_impl() {
            static COUNTER: AtomicUsize = AtomicUsize::new(0);
            println!("blanket_impl: counter was {}", COUNTER.fetch_add(1, Ordering::Relaxed));
        }
    }
    
    fn main() {
        <Ty1 as Tr>::default_impl();
        <Ty2 as Tr>::default_impl();
        <Ty1 as Tr>::blanket_impl();
        <Ty2 as Tr>::blanket_impl();
    }

prints

    
    
    default_impl: counter was 0
    default_impl: counter was 1
    blanket_impl: counter was 0
    blanket_impl: counter was 1
    

[items.static.mut]

## Mutable statics

[items.static.mut.intro]

If a static item is declared with the `mut` keyword, then it is allowed to be
modified by the program. One of Rust’s goals is to make concurrency bugs hard
to run into, and this is obviously a very large source of race conditions or
other bugs.

[items.static.mut.safety]

For this reason, an `unsafe` block is required when either reading or writing
a mutable static variable. Care should be taken to ensure that modifications
to a mutable static are safe with respect to other threads running in the same
process.

[items.static.mut.extern]

Mutable statics are still very useful, however. They can be used with C
libraries and can also be bound from C libraries in an `extern` block.

    
    
    #![allow(unused)]
    fn main() {
    fn atomic_add(_: *mut u32, _: u32) -> u32 { 2 }
    
    static mut LEVELS: u32 = 0;
    
    // This violates the idea of no shared state, and this doesn't internally
    // protect against races, so this function is `unsafe`
    unsafe fn bump_levels_unsafe() -> u32 {
        unsafe {
            let ret = LEVELS;
            LEVELS += 1;
            return ret;
        }
    }
    
    // As an alternative to `bump_levels_unsafe`, this function is safe, assuming
    // that we have an atomic_add function which returns the old value. This
    // function is safe only if no other code accesses the static in a non-atomic
    // fashion. If such accesses are possible (such as in `bump_levels_unsafe`),
    // then this would need to be `unsafe` to indicate to the caller that they
    // must still guard against concurrent access.
    fn bump_levels_safe() -> u32 {
        unsafe {
            return atomic_add(&raw mut LEVELS, 1);
        }
    }
    }

[items.static.mut.sync]

Mutable statics have the same restrictions as normal statics, except that the
type does not have to implement the `Sync` trait.

[items.static.alternate]

## Using statics or consts

It can be confusing whether or not you should use a constant item or a static
item. Constants should, in general, be preferred over statics unless one of
the following are true:

  * Large amounts of data are being stored.
  * The single-address property of statics is required.
  * Interior mutability is required.

* * *

  1. The `safe` and `unsafe` function qualifiers are only allowed semantically within `extern` blocks. ↩

[items.traits]

# Traits

[items.traits.syntax]

**Syntax**  
Trait →  
unsafe? trait IDENTIFIER GenericParams? ( : TypeParamBounds? )? WhereClause?  
{  
InnerAttribute*  
AssociatedItem*  
}

Show Railroad

Trait unsafe trait IDENTIFIER GenericParams : TypeParamBounds WhereClause {
InnerAttribute AssociatedItem }

[items.traits.intro]

A _trait_ describes an abstract interface that types can implement. This
interface consists of associated items, which come in three varieties:

  * functions
  * types
  * constants

[items.traits.namespace]

The trait declaration defines a trait in the type namespace of the module or
block where it is located.

[items.traits.associated-item-namespaces]

Associated items are defined as members of the trait within their respective
namespaces. Associated types are defined in the type namespace. Associated
constants and associated functions are defined in the value namespace.

[items.traits.self-param]

All traits define an implicit type parameter `Self` that refers to “the type
that is implementing this interface”. Traits may also contain additional type
parameters. These type parameters, including `Self`, may be constrained by
other traits and so forth as usual.

[items.traits.impls]

Traits are implemented for specific types through separate implementations.

[items.traits.associated-item-decls]

Trait functions may omit the function body by replacing it with a semicolon.
This indicates that the implementation must define the function. If the trait
function defines a body, this definition acts as a default for any
implementation which does not override it. Similarly, associated constants may
omit the equals sign and expression to indicate implementations must define
the constant value. Associated types must never define the type, the type may
only be specified in an implementation.

    
    
    #![allow(unused)]
    fn main() {
    // Examples of associated trait items with and without definitions.
    trait Example {
        const CONST_NO_DEFAULT: i32;
        const CONST_WITH_DEFAULT: i32 = 99;
        type TypeNoDefault;
        fn method_without_default(&self);
        fn method_with_default(&self) {}
    }
    }

[items.traits.const-fn]

Trait functions are not allowed to be `const`.

[items.traits.bounds]

## Trait bounds

Generic items may use traits as bounds on their type parameters.

[items.traits.generic]

## Generic traits

Type parameters can be specified for a trait to make it generic. These appear
after the trait name, using the same syntax used in generic functions.

    
    
    #![allow(unused)]
    fn main() {
    trait Seq<T> {
        fn len(&self) -> u32;
        fn elt_at(&self, n: u32) -> T;
        fn iter<F>(&self, f: F) where F: Fn(T);
    }
    }

[items.traits.dyn-compatible]

## Dyn compatibility

[items.traits.dyn-compatible.intro]

A dyn-compatible trait can be the base trait of a trait object. A trait is
_dyn compatible_ if it has the following qualities:

[items.traits.dyn-compatible.supertraits]

  * All supertraits must also be dyn compatible.

[items.traits.dyn-compatible.sized]

  * `Sized` must not be a supertrait. In other words, it must not require `Self: Sized`.

[items.traits.dyn-compatible.associated-consts]

  * It must not have any associated constants.

[items.traits.dyn-compatible.associated-types]

  * It must not have any associated types with generics.

[items.traits.dyn-compatible.associated-functions]

  * All associated functions must either be dispatchable from a trait object or be explicitly non-dispatchable: 
    * Dispatchable functions must: 
      * Not have any type parameters (although lifetime parameters are allowed).
      * Be a method that does not use `Self` except in the type of the receiver.
      * Have a receiver with one of the following types: 
        * `&Self` (i.e. `&self`)
        * `&mut Self` (i.e `&mut self`)
        * `Box<Self>`
        * `Rc<Self>`
        * `Arc<Self>`
        * `Pin<P>` where `P` is one of the types above
      * Not have an opaque return type; that is, 
        * Not be an `async fn` (which has a hidden `Future` type).
        * Not have a return position `impl Trait` type (`fn example(&self) -> impl Trait`).
      * Not have a `where Self: Sized` bound (receiver type of `Self` (i.e. `self`) implies this).
    * Explicitly non-dispatchable functions require: 
      * Have a `where Self: Sized` bound (receiver type of `Self` (i.e. `self`) implies this).

[items.traits.dyn-compatible.async-traits]

  * The [`AsyncFn`](../core/ops/async_function/trait.AsyncFn.html), [`AsyncFnMut`](../core/ops/async_function/trait.AsyncFnMut.html), and [`AsyncFnOnce`](../core/ops/async_function/trait.AsyncFnOnce.html) traits are not dyn-compatible.

> Note
>
> This concept was formerly known as _object safety_.
    
    
    #![allow(unused)]
    fn main() {
    use std::rc::Rc;
    use std::sync::Arc;
    use std::pin::Pin;
    // Examples of dyn compatible methods.
    trait TraitMethods {
        fn by_ref(self: &Self) {}
        fn by_ref_mut(self: &mut Self) {}
        fn by_box(self: Box<Self>) {}
        fn by_rc(self: Rc<Self>) {}
        fn by_arc(self: Arc<Self>) {}
        fn by_pin(self: Pin<&Self>) {}
        fn with_lifetime<'a>(self: &'a Self) {}
        fn nested_pin(self: Pin<Arc<Self>>) {}
    }
    struct S;
    impl TraitMethods for S {}
    let t: Box<dyn TraitMethods> = Box::new(S);
    }
    
    
    #![allow(unused)]
    fn main() {
    // This trait is dyn compatible, but these methods cannot be dispatched on a trait object.
    trait NonDispatchable {
        // Non-methods cannot be dispatched.
        fn foo() where Self: Sized {}
        // Self type isn't known until runtime.
        fn returns(&self) -> Self where Self: Sized;
        // `other` may be a different concrete type of the receiver.
        fn param(&self, other: Self) where Self: Sized {}
        // Generics are not compatible with vtables.
        fn typed<T>(&self, x: T) where Self: Sized {}
    }
    
    struct S;
    impl NonDispatchable for S {
        fn returns(&self) -> Self where Self: Sized { S }
    }
    let obj: Box<dyn NonDispatchable> = Box::new(S);
    obj.returns(); // ERROR: cannot call with Self return
    obj.param(S);  // ERROR: cannot call with Self parameter
    obj.typed(1);  // ERROR: cannot call with generic type
    }
    
    
    #![allow(unused)]
    fn main() {
    use std::rc::Rc;
    // Examples of dyn-incompatible traits.
    trait DynIncompatible {
        const CONST: i32 = 1;  // ERROR: cannot have associated const
    
        fn foo() {}  // ERROR: associated function without Sized
        fn returns(&self) -> Self; // ERROR: Self in return type
        fn typed<T>(&self, x: T) {} // ERROR: has generic type parameters
        fn nested(self: Rc<Box<Self>>) {} // ERROR: nested receiver cannot be dispatched on
    }
    
    struct S;
    impl DynIncompatible for S {
        fn returns(&self) -> Self { S }
    }
    let obj: Box<dyn DynIncompatible> = Box::new(S); // ERROR
    }
    
    
    #![allow(unused)]
    fn main() {
    // `Self: Sized` traits are dyn-incompatible.
    trait TraitWithSize where Self: Sized {}
    
    struct S;
    impl TraitWithSize for S {}
    let obj: Box<dyn TraitWithSize> = Box::new(S); // ERROR
    }
    
    
    #![allow(unused)]
    fn main() {
    // Dyn-incompatible if `Self` is a type argument.
    trait Super<A> {}
    trait WithSelf: Super<Self> where Self: Sized {}
    
    struct S;
    impl<A> Super<A> for S {}
    impl WithSelf for S {}
    let obj: Box<dyn WithSelf> = Box::new(S); // ERROR: cannot use `Self` type parameter
    }

[items.traits.supertraits]

## Supertraits

[items.traits.supertraits.intro]

**Supertraits** are traits that are required to be implemented for a type to
implement a specific trait. Furthermore, anywhere a generic or trait object is
bounded by a trait, it has access to the associated items of its supertraits.

[items.traits.supertraits.decl]

Supertraits are declared by trait bounds on the `Self` type of a trait and
transitively the supertraits of the traits declared in those trait bounds. It
is an error for a trait to be its own supertrait.

[items.traits.supertraits.subtrait]

The trait with a supertrait is called a **subtrait** of its supertrait.

The following is an example of declaring `Shape` to be a supertrait of
`Circle`.

    
    
    #![allow(unused)]
    fn main() {
    trait Shape { fn area(&self) -> f64; }
    trait Circle: Shape { fn radius(&self) -> f64; }
    }

And the following is the same example, except using where clauses.

    
    
    #![allow(unused)]
    fn main() {
    trait Shape { fn area(&self) -> f64; }
    trait Circle where Self: Shape { fn radius(&self) -> f64; }
    }

This next example gives `radius` a default implementation using the `area`
function from `Shape`.

    
    
    #![allow(unused)]
    fn main() {
    trait Shape { fn area(&self) -> f64; }
    trait Circle where Self: Shape {
        fn radius(&self) -> f64 {
            // A = pi * r^2
            // so algebraically,
            // r = sqrt(A / pi)
            (self.area() / std::f64::consts::PI).sqrt()
        }
    }
    }

This next example calls a supertrait method on a generic parameter.

    
    
    #![allow(unused)]
    fn main() {
    trait Shape { fn area(&self) -> f64; }
    trait Circle: Shape { fn radius(&self) -> f64; }
    fn print_area_and_radius<C: Circle>(c: C) {
        // Here we call the area method from the supertrait `Shape` of `Circle`.
        println!("Area: {}", c.area());
        println!("Radius: {}", c.radius());
    }
    }

Similarly, here is an example of calling supertrait methods on trait objects.

    
    
    #![allow(unused)]
    fn main() {
    trait Shape { fn area(&self) -> f64; }
    trait Circle: Shape { fn radius(&self) -> f64; }
    struct UnitCircle;
    impl Shape for UnitCircle { fn area(&self) -> f64 { std::f64::consts::PI } }
    impl Circle for UnitCircle { fn radius(&self) -> f64 { 1.0 } }
    let circle = UnitCircle;
    let circle = Box::new(circle) as Box<dyn Circle>;
    let nonsense = circle.radius() * circle.area();
    }

[items.traits.safety]

## Unsafe traits

[items.traits.safety.intro]

Traits items that begin with the `unsafe` keyword indicate that _implementing_
the trait may be unsafe. It is safe to use a correctly implemented unsafe
trait. The trait implementation must also begin with the `unsafe` keyword.

`Sync` and `Send` are examples of unsafe traits.

[items.traits.params]

## Parameter patterns

[items.traits.params.patterns-no-body]

Parameters in associated functions without a body only allow IDENTIFIER or `_`
wild card patterns, as well as the form allowed by SelfParam. `mut` IDENTIFIER
is currently allowed, but it is deprecated and will become a hard error in the
future.

    
    
    #![allow(unused)]
    fn main() {
    trait T {
        fn f1(&self);
        fn f2(x: Self, _: i32);
    }
    }
    
    
    #![allow(unused)]
    fn main() {
    trait T {
        fn f2(&x: &i32); // ERROR: patterns aren't allowed in functions without bodies
    }
    }

[items.traits.params.patterns-with-body]

Parameters in associated functions with a body only allow irrefutable
patterns.

    
    
    #![allow(unused)]
    fn main() {
    trait T {
        fn f1((a, b): (i32, i32)) {} // OK: is irrefutable
    }
    }
    
    
    #![allow(unused)]
    fn main() {
    trait T {
        fn f1(123: i32) {} // ERROR: pattern is refutable
        fn f2(Some(x): Option<i32>) {} // ERROR: pattern is refutable
    }
    }

[items.traits.params.pattern-required.edition2018]

> 2018 Edition differences
>
> Prior to the 2018 edition, the pattern for an associated function parameter
> is optional:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     // 2015 Edition
>     trait T {
>         fn f(i32); // OK: parameter identifiers are not required
>     }
>     }
>
> Beginning in the 2018 edition, patterns are no longer optional.

[items.traits.params.restriction-patterns.edition2018]

> 2018 Edition differences
>
> Prior to the 2018 edition, parameters in associated functions with a body
> are limited to the following kinds of patterns:
>
>   * IDENTIFIER
>   * `mut` IDENTIFIER
>   * `_`
>   * `&` IDENTIFIER
>   * `&&` IDENTIFIER
>

>  
>  
>     #![allow(unused)]
>     fn main() {
>     // 2015 Edition
>     trait T {
>         fn f1((a, b): (i32, i32)) {} // ERROR: pattern not allowed
>     }
>     }
>
> Beginning in 2018, all irrefutable patterns are allowed as described in
> items.traits.params.patterns-with-body.

[items.traits.associated-visibility]

## Item visibility

[items.traits.associated-visibility.intro]

Trait items syntactically allow a Visibility annotation, but this is rejected
when the trait is validated. This allows items to be parsed with a unified
syntax across different contexts where they are used. As an example, an empty
`vis` macro fragment specifier can be used for trait items, where the macro
rule may be used in other situations where visibility is allowed.

    
    
    macro_rules! create_method {
        ($vis:vis $name:ident) => {
            $vis fn $name(&self) {}
        };
    }
    
    trait T1 {
        // Empty `vis` is allowed.
        create_method! { method_of_t1 }
    }
    
    struct S;
    
    impl S {
        // Visibility is allowed here.
        create_method! { pub method_of_s }
    }
    
    impl T1 for S {}
    
    fn main() {
        let s = S;
        s.method_of_t1();
        s.method_of_s();
    }

[items.impl]

# Implementations

[items.impl.syntax]

**Syntax**  
Implementation → InherentImpl | TraitImpl

InherentImpl →  
impl GenericParams? Type WhereClause? {  
InnerAttribute*  
AssociatedItem*  
}

TraitImpl →  
unsafe? impl GenericParams? !? TypePath for Type  
WhereClause?  
{  
InnerAttribute*  
AssociatedItem*  
}

Show Railroad

Implementation InherentImpl TraitImpl

InherentImpl impl GenericParams Type WhereClause { InnerAttribute
AssociatedItem }

TraitImpl unsafe impl GenericParams ! TypePath for Type WhereClause {
InnerAttribute AssociatedItem }

[items.impl.intro]

An _implementation_ is an item that associates items with an _implementing
type_. Implementations are defined with the keyword `impl` and contain
functions that belong to an instance of the type that is being implemented or
to the type statically.

[items.impl.kinds]

There are two types of implementations:

  * inherent implementations
  * trait implementations

[items.impl.inherent]

## Inherent implementations

[items.impl.inherent.intro]

An inherent implementation is defined as the sequence of the `impl` keyword,
generic type declarations, a path to a nominal type, a where clause, and a
bracketed set of associable items.

[items.impl.inherent.implementing-type]

The nominal type is called the _implementing type_ and the associable items
are the _associated items_ to the implementing type.

[items.impl.inherent.associated-items]

Inherent implementations associate the contained items to the implementing
type.

[items.impl.inherent.associated-items.allowed-items]

Inherent implementations can contain associated functions (including methods)
and associated constants.

[items.impl.inherent.type-alias]

They cannot contain associated type aliases.

[items.impl.inherent.associated-item-path]

The path to an associated item is any path to the implementing type, followed
by the associated item’s identifier as the final path component.

[items.impl.inherent.coherence]

A type can also have multiple inherent implementations. An implementing type
must be defined within the same crate as the original type definition.

    
    
    pub mod color {
        pub struct Color(pub u8, pub u8, pub u8);
    
        impl Color {
            pub const WHITE: Color = Color(255, 255, 255);
        }
    }
    
    mod values {
        use super::color::Color;
        impl Color {
            pub fn red() -> Color {
                Color(255, 0, 0)
            }
        }
    }
    
    pub use self::color::Color;
    fn main() {
        // Actual path to the implementing type and impl in the same module.
        color::Color::WHITE;
    
        // Impl blocks in different modules are still accessed through a path to the type.
        color::Color::red();
    
        // Re-exported paths to the implementing type also work.
        Color::red();
    
        // Does not work, because use in `values` is not pub.
        // values::Color::red();
    }

[items.impl.trait]

## Trait implementations

[items.impl.trait.intro]

A _trait implementation_ is defined like an inherent implementation except
that the optional generic type declarations are followed by a trait, followed
by the keyword `for`, followed by a path to a nominal type.

[items.impl.trait.implemented-trait]

The trait is known as the _implemented trait_. The implementing type
implements the implemented trait.

[items.impl.trait.def-requirement]

A trait implementation must define all non-default associated items declared
by the implemented trait, may redefine default associated items defined by the
implemented trait, and cannot define any other items.

[items.impl.trait.associated-item-path]

The path to the associated items is `<` followed by a path to the implementing
type followed by `as` followed by a path to the trait followed by `>` as a
path component followed by the associated item’s path component.

[items.impl.trait.safety]

Unsafe traits require the trait implementation to begin with the `unsafe`
keyword.

    
    
    #![allow(unused)]
    fn main() {
    #[derive(Copy, Clone)]
    struct Point {x: f64, y: f64};
    type Surface = i32;
    struct BoundingBox {x: f64, y: f64, width: f64, height: f64};
    trait Shape { fn draw(&self, s: Surface); fn bounding_box(&self) -> BoundingBox; }
    fn do_draw_circle(s: Surface, c: Circle) { }
    struct Circle {
        radius: f64,
        center: Point,
    }
    
    impl Copy for Circle {}
    
    impl Clone for Circle {
        fn clone(&self) -> Circle { *self }
    }
    
    impl Shape for Circle {
        fn draw(&self, s: Surface) { do_draw_circle(s, *self); }
        fn bounding_box(&self) -> BoundingBox {
            let r = self.radius;
            BoundingBox {
                x: self.center.x - r,
                y: self.center.y - r,
                width: 2.0 * r,
                height: 2.0 * r,
            }
        }
    }
    }

[items.impl.trait.coherence]

### Trait implementation coherence

[items.impl.trait.coherence.intro]

A trait implementation is considered incoherent if either the orphan rules
check fails or there are overlapping implementation instances.

[items.impl.trait.coherence.overlapping]

Two trait implementations overlap when there is a non-empty intersection of
the traits the implementation is for, the implementations can be instantiated
with the same type.

[items.impl.trait.orphan-rule]

#### Orphan rules

[items.impl.trait.orphan-rule.intro]

The _orphan rule_ states that a trait implementation is only allowed if either
the trait or at least one of the types in the implementation is defined in the
current crate. It prevents conflicting trait implementations across different
crates and is key to ensuring coherence.

An orphan implementation is one that implements a foreign trait for a foreign
type. If these were freely allowed, two crates could implement the same trait
for the same type in incompatible ways, creating a situation where adding or
updating a dependency could break compilation due to conflicting
implementations.

The orphan rule enables library authors to add new implementations to their
traits without fear that they’ll break downstream code. Without these
restrictions, a library couldn’t add an implementation like `impl<T: Display>
MyTrait for T` without potentially conflicting with downstream
implementations.

[items.impl.trait.orphan-rule.general]

Given `impl<P1..=Pn> Trait<T1..=Tn> for T0`, an `impl` is valid only if at
least one of the following is true:

  * `Trait` is a local trait
  * All of 
    * At least one of the types `T0..=Tn` must be a local type. Let `Ti` be the first such type.
    * No uncovered type parameters `P1..=Pn` may appear in `T0..Ti` (excluding `Ti`)

[items.impl.trait.uncovered-param]

Only the appearance of _uncovered_ type parameters is restricted.

[items.impl.trait.fundamental]

Note that for the purposes of coherence, fundamental types are special. The
`T` in `Box<T>` is not considered covered, and `Box<LocalType>` is considered
local.

[items.impl.generics]

## Generic implementations

[items.impl.generics.intro]

An implementation can take generic parameters, which can be used in the rest
of the implementation. Implementation parameters are written directly after
the `impl` keyword.

    
    
    #![allow(unused)]
    fn main() {
    trait Seq<T> { fn dummy(&self, _: T) { } }
    impl<T> Seq<T> for Vec<T> {
        /* ... */
    }
    impl Seq<bool> for u32 {
        /* Treat the integer as a sequence of bits */
    }
    }

[items.impl.generics.usage]

Generic parameters _constrain_ an implementation if the parameter appears at
least once in one of:

  * The implemented trait, if it has one
  * The implementing type
  * As an associated type in the bounds of a type that contains another parameter that constrains the implementation

[items.impl.generics.constrain]

Type and const parameters must always constrain the implementation. Lifetimes
must constrain the implementation if the lifetime is used in an associated
type.

Examples of constraining situations:

    
    
    #![allow(unused)]
    fn main() {
    trait Trait{}
    trait GenericTrait<T> {}
    trait HasAssocType { type Ty; }
    struct Struct;
    struct GenericStruct<T>(T);
    struct ConstGenericStruct<const N: usize>([(); N]);
    // T constrains by being an argument to GenericTrait.
    impl<T> GenericTrait<T> for i32 { /* ... */ }
    
    // T constrains by being an argument to GenericStruct
    impl<T> Trait for GenericStruct<T> { /* ... */ }
    
    // Likewise, N constrains by being an argument to ConstGenericStruct
    impl<const N: usize> Trait for ConstGenericStruct<N> { /* ... */ }
    
    // T constrains by being in an associated type in a bound for type `U` which is
    // itself a generic parameter constraining the trait.
    impl<T, U> GenericTrait<U> for u32 where U: HasAssocType<Ty = T> { /* ... */ }
    
    // Like previous, except the type is `(U, isize)`. `U` appears inside the type
    // that includes `T`, and is not the type itself.
    impl<T, U> GenericStruct<U> where (U, isize): HasAssocType<Ty = T> { /* ... */ }
    }

Examples of non-constraining situations:

    
    
    #![allow(unused)]
    fn main() {
    // The rest of these are errors, since they have type or const parameters that
    // do not constrain.
    
    // T does not constrain since it does not appear at all.
    impl<T> Struct { /* ... */ }
    
    // N does not constrain for the same reason.
    impl<const N: usize> Struct { /* ... */ }
    
    // Usage of T inside the implementation does not constrain the impl.
    impl<T> Struct {
        fn uses_t(t: &T) { /* ... */ }
    }
    
    // T is used as an associated type in the bounds for U, but U does not constrain.
    impl<T, U> Struct where U: HasAssocType<Ty = T> { /* ... */ }
    
    // T is used in the bounds, but not as an associated type, so it does not constrain.
    impl<T, U> GenericTrait<U> for u32 where U: GenericTrait<T> {}
    }

Example of an allowed unconstraining lifetime parameter:

    
    
    #![allow(unused)]
    fn main() {
    struct Struct;
    impl<'a> Struct {}
    }

Example of a disallowed unconstraining lifetime parameter:

    
    
    #![allow(unused)]
    fn main() {
    struct Struct;
    trait HasAssocType { type Ty; }
    impl<'a> HasAssocType for Struct {
        type Ty = &'a Struct;
    }
    }

[items.impl.attributes]

## Attributes on implementations

Implementations may contain outer attributes before the `impl` keyword and
inner attributes inside the brackets that contain the associated items. Inner
attributes must come before any associated items. The attributes that have
meaning here are `cfg`, `deprecated`, [`doc`](../rustdoc/the-doc-
attribute.html), and the lint check attributes.

[items.extern]

# External blocks

[items.extern.syntax]

**Syntax**  
ExternBlock →  
unsafe?​1 extern Abi? {  
InnerAttribute*  
ExternalItem*  
}

ExternalItem →  
OuterAttribute* (  
MacroInvocationSemi  
| Visibility? StaticItem  
| Visibility? Function  
)

Show Railroad

ExternBlock unsafe extern Abi { InnerAttribute ExternalItem }

ExternalItem OuterAttribute MacroInvocationSemi Visibility StaticItem
Visibility Function

[items.extern.intro]

External blocks provide _declarations_ of items that are not _defined_ in the
current crate and are the basis of Rust’s foreign function interface. These
are akin to unchecked imports.

[items.extern.allowed-kinds]

Two kinds of item _declarations_ are allowed in external blocks: functions and
statics.

[items.extern.safety]

Calling unsafe functions or accessing unsafe statics that are declared in
external blocks is only allowed in an `unsafe` context.

[items.extern.namespace]

The external block defines its functions and statics in the value namespace of
the module or block where it is located.

[items.extern.unsafe-required]

The `unsafe` keyword is semantically required to appear before the `extern`
keyword on external blocks.

[items.extern.edition2024]

> 2024 Edition differences
>
> Prior to the 2024 edition, the `unsafe` keyword is optional. The `safe` and
> `unsafe` item qualifiers are only allowed if the external block itself is
> marked as `unsafe`.

[items.extern.fn]

## Functions

[items.extern.fn.body]

Functions within external blocks are declared in the same way as other Rust
functions, with the exception that they must not have a body and are instead
terminated by a semicolon.

[items.extern.fn.param-patterns]

Patterns are not allowed in parameters, only IDENTIFIER or `_` may be used.

[items.extern.fn.qualifiers]

The `safe` and `unsafe` function qualifiers are allowed, but other function
qualifiers (e.g. `const`, `async`, `extern`) are not.

[items.extern.fn.foreign-abi]

Functions within external blocks may be called by Rust code, just like
functions defined in Rust. The Rust compiler automatically translates between
the Rust ABI and the foreign ABI.

[items.extern.fn.safety]

A function declared in an extern block is implicitly `unsafe` unless the
`safe` function qualifier is present.

[items.extern.fn.fn-ptr]

When coerced to a function pointer, a function declared in an extern block has
type `extern "abi" for<'l1, ..., 'lm> fn(A1, ..., An) -> R`, where `'l1`, …
`'lm` are its lifetime parameters, `A1`, …, `An` are the declared types of its
parameters, and `R` is the declared return type.

[items.extern.static]

## Statics

[items.extern.static.intro]

Statics within external blocks are declared in the same way as statics outside
of external blocks, except that they do not have an expression initializing
their value.

[items.extern.static.safety]

Unless a static item declared in an extern block is qualified as `safe`, it is
`unsafe` to access that item, whether or not it’s mutable, because there is
nothing guaranteeing that the bit pattern at the static’s memory is valid for
the type it is declared with, since some arbitrary (e.g. C) code is in charge
of initializing the static.

[items.extern.static.mut]

Extern statics can be either immutable or mutable just like statics outside of
external blocks.

[items.extern.static.read-only]

An immutable static _must_ be initialized before any Rust code is executed. It
is not enough for the static to be initialized before Rust code reads from it.
Once Rust code runs, mutating an immutable static (from inside or outside
Rust) is UB, except if the mutation happens to bytes inside of an
`UnsafeCell`.

[items.extern.abi]

## ABI

[items.extern.abi.intro]

The `extern` keyword can be followed by an optional ABI string. The ABI
specifies the calling convention of the functions in the block. The calling
convention defines a low-level interface for functions, such as how arguments
are placed in registers or on the stack, how return values are passed, and who
is responsible for cleaning up the stack.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     // Interface to the Windows API.
>     unsafe extern "system" { /* ... */ }
>     }

[items.extern.abi.default]

If the ABI string is not specified, it defaults to `"C"`.

> Note
>
> The `extern` syntax without an explicit ABI is being phased out, so it’s
> better to always write the ABI explicitly.
>
> For more details, see [Rust issue #134986](https://github.com/rust-
> lang/rust/issues/134986).

[items.extern.abi.standard]

The following ABI strings are supported on all platforms:

[items.extern.abi.rust]

  * `unsafe extern "Rust"` — The native calling convention for Rust functions and closures. This is the default when a function is declared without using `extern fn`. The Rust ABI offers no stability guarantees.

[items.extern.abi.c]

  * `unsafe extern "C"` — The “C” ABI matches the default ABI chosen by the dominant C compiler for the target.

[items.extern.abi.system]

  * `unsafe extern "system"` — This is equivalent to `extern "C"` except on Windows x86_32 where it is equivalent to `"stdcall"` for non-variadic functions, and equivalent to `"C"` for variadic functions.

> Note
>
> As the correct underlying ABI on Windows is target-specific, it’s best to
> use `extern "system"` when attempting to link Windows API functions that
> don’t use an explicitly defined ABI.

[items.extern.abi.unwind]

  * `extern "C-unwind"` and `extern "system-unwind"` — Identical to `"C"` and `"system"`, respectively, but with different behavior when the callee unwinds (by panicking or throwing a C++ style exception).

[items.extern.abi.platform]

There are also some platform-specific ABI strings:

[items.extern.abi.cdecl]

  * `unsafe extern "cdecl"` — The calling convention typically used with x86_32 C code.

    * Only available on x86_32 targets.
    * Corresponds to MSVC’s `__cdecl` and GCC and clang’s `__attribute__((cdecl))`.

> Note
>
> For details, see:
>
>     * <https://learn.microsoft.com/en-us/cpp/cpp/cdecl>
>     * <https://en.wikipedia.org/wiki/X86_calling_conventions#cdecl>

[items.extern.abi.stdcall]

  * `unsafe extern "stdcall"` — The calling convention typically used by the [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) on x86_32.

    * Only available on x86_32 targets.
    * Corresponds to MSVC’s `__stdcall` and GCC and clang’s `__attribute__((stdcall))`.

> Note
>
> For details, see:
>
>     * <https://learn.microsoft.com/en-us/cpp/cpp/stdcall>
>     * <https://en.wikipedia.org/wiki/X86_calling_conventions#stdcall>

[items.extern.abi.win64]

  * `unsafe extern "win64"` — The Windows x64 ABI.

    * Only available on x86_64 targets.
    * “win64” is the same as the “C” ABI on Windows x86_64 targets.
    * Corresponds to GCC and clang’s `__attribute__((ms_abi))`.

> Note
>
> For details, see:
>
>     * <https://learn.microsoft.com/en-us/cpp/build/x64-software-conventions>
>     *
> <https://en.wikipedia.org/wiki/X86_calling_conventions#Microsoft_x64_calling_convention>

[items.extern.abi.sysv64]

  * `unsafe extern "sysv64"` — The System V ABI.

    * Only available on x86_64 targets.
    * “sysv64” is the same as the “C” ABI on non-Windows x86_64 targets.
    * Corresponds to GCC and clang’s `__attribute__((sysv_abi))`.

> Note
>
> For details, see:
>
>     * <https://wiki.osdev.org/System_V_ABI>
>     *
> <https://en.wikipedia.org/wiki/X86_calling_conventions#System_V_AMD64_ABI>

[items.extern.abi.aapcs]

  * `unsafe extern "aapcs"` — The soft-float ABI for ARM.

    * Only available on ARM32 targets.
    * “aapcs” is the same as the “C” ABI on soft-float ARM32.
    * Corresponds to clang’s `__attribute__((pcs("aapcs")))`.

> Note
>
> For details, see:
>
>     * [Arm Procedure Call
> Standard](https://developer.arm.com/documentation/107656/0101/Getting-
> started-with-Armv8-M-based-systems/Procedure-Call-Standard-for-Arm-
> Architecture--AAPCS-)

[items.extern.abi.fastcall]

  * `unsafe extern "fastcall"` — A “fast” variant of stdcall that passes some arguments in registers.

    * Only available on x86_32 targets.
    * Corresponds to MSVC’s `__fastcall` and GCC and clang’s `__attribute__((fastcall))`.

> Note
>
> For details, see:
>
>     * <https://learn.microsoft.com/en-us/cpp/cpp/fastcall>
>     *
> <https://en.wikipedia.org/wiki/X86_calling_conventions#Microsoft_fastcall>

[items.extern.abi.thiscall]

  * `unsafe extern "thiscall"` — The calling convention typically used on C++ class member functions on x86_32 MSVC.

    * Only available on x86_32 targets.
    * Corresponds to MSVC’s `__thiscall` and GCC and clang’s `__attribute__((thiscall))`.

> Note
>
> For details, see:
>
>     * <https://en.wikipedia.org/wiki/X86_calling_conventions#thiscall>
>     * <https://learn.microsoft.com/en-us/cpp/cpp/thiscall>

[items.extern.abi.efiapi]

  * `unsafe extern "efiapi"` — The ABI used for [UEFI](https://uefi.org/specifications) functions. 
    * Only available on x86 and ARM targets (32bit and 64bit).

[items.extern.abi.platform-unwind-variants]

Like `"C"` and `"system"`, most platform-specific ABI strings also have a
corresponding `-unwind` variant; specifically, these are:

  * `"aapcs-unwind"`
  * `"cdecl-unwind"`
  * `"fastcall-unwind"`
  * `"stdcall-unwind"`
  * `"sysv64-unwind"`
  * `"thiscall-unwind"`
  * `"win64-unwind"`

[items.extern.variadic]

## Variadic functions

Functions within external blocks may be variadic by specifying `...` as the
last argument. The variadic parameter may optionally be specified with an
identifier.

    
    
    #![allow(unused)]
    fn main() {
    unsafe extern "C" {
        unsafe fn foo(...);
        unsafe fn bar(x: i32, ...);
        unsafe fn with_name(format: *const u8, args: ...);
        // SAFETY: This function guarantees it will not access
        // variadic arguments.
        safe fn ignores_variadic_arguments(x: i32, ...);
    }
    }

> Warning
>
> The `safe` qualifier should not be used on a function in an `extern` block
> unless that function guarantees that it will not access the variadic
> arguments at all. Passing an unexpected number of arguments or arguments of
> unexpected type to a variadic function may lead to undefined behavior.

[items.extern.variadic.conventions]

Variadic parameters can only be specified within `extern` blocks with the
following ABI strings or their corresponding `-unwind` variants:

  * `"aapcs"`
  * `"C"`
  * `"cdecl"`
  * `"efiapi"`
  * `"system"`
  * `"sysv64"`
  * `"win64"`

[items.extern.attributes]

## Attributes on extern blocks

[items.extern.attributes.intro]

The following attributes control the behavior of external blocks.

[items.extern.attributes.link]

### The `link` attribute

[items.extern.attributes.link.intro]

The _`link` attribute_ specifies the name of a native library that the
compiler should link with for the items within an `extern` block.

[items.extern.attributes.link.syntax]

It uses the MetaListNameValueStr syntax to specify its inputs. The `name` key
is the name of the native library to link. The `kind` key is an optional value
which specifies the kind of library with the following possible values:

[items.extern.attributes.link.dylib]

  * `dylib` — Indicates a dynamic library. This is the default if `kind` is not specified.

[items.extern.attributes.link.static]

  * `static` — Indicates a static library.

[items.extern.attributes.link.framework]

  * `framework` — Indicates a macOS framework. This is only valid for macOS targets.

[items.extern.attributes.link.raw-dylib]

  * `raw-dylib` — Indicates a dynamic library where the compiler will generate an import library to link against (see `dylib` versus `raw-dylib` below for details). This is only valid for Windows targets.

[items.extern.attributes.link.name-requirement]

The `name` key must be included if `kind` is specified.

[items.extern.attributes.link.modifiers]

The optional `modifiers` argument is a way to specify linking modifiers for
the library to link.

[items.extern.attributes.link.modifiers.syntax]

Modifiers are specified as a comma-delimited string with each modifier
prefixed with either a `+` or `-` to indicate that the modifier is enabled or
disabled, respectively.

[items.extern.attributes.link.modifiers.multiple]

Specifying multiple `modifiers` arguments in a single `link` attribute, or
multiple identical modifiers in the same `modifiers` argument is not currently
supported.  
Example: `#[link(name = "mylib", kind = "static", modifiers = "+whole-
archive")]`.

[items.extern.attributes.link.wasm_import_module]

The `wasm_import_module` key may be used to specify the [WebAssembly
module](https://webassembly.github.io/spec/core/syntax/modules.html) name for
the items within an `extern` block when importing symbols from the host
environment. The default module name is `env` if `wasm_import_module` is not
specified.

    
    
    #[link(name = "crypto")]
    unsafe extern {
        // …
    }
    
    #[link(name = "CoreFoundation", kind = "framework")]
    unsafe extern {
        // …
    }
    
    #[link(wasm_import_module = "foo")]
    unsafe extern {
        // …
    }

[items.extern.attributes.link.empty-block]

It is valid to add the `link` attribute on an empty extern block. You can use
this to satisfy the linking requirements of extern blocks elsewhere in your
code (including upstream crates) instead of adding the attribute to each
extern block.

[items.extern.attributes.link.modifiers.bundle]

#### Linking modifiers: `bundle`

[items.extern.attributes.link.modifiers.bundle.allowed-kinds]

This modifier is only compatible with the `static` linking kind. Using any
other kind will result in a compiler error.

[items.extern.attributes.link.modifiers.bundle.behavior]

When building a rlib or staticlib `+bundle` means that the native static
library will be packed into the rlib or staticlib archive, and then retrieved
from there during linking of the final binary.

[items.extern.attributes.link.modifiers.bundle.behavior-negative]

When building a rlib `-bundle` means that the native static library is
registered as a dependency of that rlib “by name”, and object files from it
are included only during linking of the final binary, the file search by that
name is also performed during final linking.  
When building a staticlib `-bundle` means that the native static library is
simply not included into the archive and some higher level build system will
need to add it later during linking of the final binary.

[items.extern.attributes.link.modifiers.bundle.no-effect]

This modifier has no effect when building other targets like executables or
dynamic libraries.

[items.extern.attributes.link.modifiers.bundle.default]

The default for this modifier is `+bundle`.

More implementation details about this modifier can be found in [`bundle`
documentation for rustc](../rustc/command-line-arguments.html#linking-
modifiers-bundle).

[items.extern.attributes.link.modifiers.whole-archive]

#### Linking modifiers: `whole-archive`

[items.extern.attributes.link.modifiers.whole-archive.allowed-kinds]

This modifier is only compatible with the `static` linking kind. Using any
other kind will result in a compiler error.

[items.extern.attributes.link.modifiers.whole-archive.behavior]

`+whole-archive` means that the static library is linked as a whole archive
without throwing any object files away.

[items.extern.attributes.link.modifiers.whole-archive.default]

The default for this modifier is `-whole-archive`.

More implementation details about this modifier can be found in [`whole-
archive` documentation for rustc](../rustc/command-line-
arguments.html#linking-modifiers-whole-archive).

[items.extern.attributes.link.modifiers.verbatim]

### Linking modifiers: `verbatim`

[items.extern.attributes.link.modifiers.verbatim.allowed-kinds]

This modifier is compatible with all linking kinds.

[items.extern.attributes.link.modifiers.verbatim.behavior]

`+verbatim` means that rustc itself won’t add any target-specified library
prefixes or suffixes (like `lib` or `.a`) to the library name, and will try
its best to ask for the same thing from the linker.

[items.extern.attributes.link.modifiers.verbatim.behavior-negative]

`-verbatim` means that rustc will either add a target-specific prefix and
suffix to the library name before passing it to linker, or won’t prevent
linker from implicitly adding it.

[items.extern.attributes.link.modifiers.verbatim.default]

The default for this modifier is `-verbatim`.

More implementation details about this modifier can be found in [`verbatim`
documentation for rustc](../rustc/command-line-arguments.html#linking-
modifiers-verbatim).

[items.extern.attributes.link.kind-raw-dylib]

#### `dylib` versus `raw-dylib`

[items.extern.attributes.link.kind-raw-dylib.intro]

On Windows, linking against a dynamic library requires that an import library
is provided to the linker: this is a special static library that declares all
of the symbols exported by the dynamic library in such a way that the linker
knows that they have to be dynamically loaded at runtime.

[items.extern.attributes.link.kind-raw-dylib.import]

Specifying `kind = "dylib"` instructs the Rust compiler to link an import
library based on the `name` key. The linker will then use its normal library
resolution logic to find that import library. Alternatively, specifying `kind
= "raw-dylib"` instructs the compiler to generate an import library during
compilation and provide that to the linker instead.

[items.extern.attributes.link.kind-raw-dylib.platform-specific]

`raw-dylib` is only supported on Windows. Using it when targeting other
platforms will result in a compiler error.

[items.extern.attributes.link.import_name_type]

#### The `import_name_type` key

[items.extern.attributes.link.import_name_type.intro]

On x86 Windows, names of functions are “decorated” (i.e., have a specific
prefix and/or suffix added) to indicate their calling convention. For example,
a `stdcall` calling convention function with the name `fn1` that has no
arguments would be decorated as `_fn1@0`. However, the [PE
Format](https://learn.microsoft.com/windows/win32/debug/pe-format#import-name-
type) does also permit names to have no prefix or be undecorated.
Additionally, the MSVC and GNU toolchains use different decorations for the
same calling conventions which means, by default, some Win32 functions cannot
be called using the `raw-dylib` link kind via the GNU toolchain.

[items.extern.attributes.link.import_name_type.values]

To allow for these differences, when using the `raw-dylib` link kind you may
also specify the `import_name_type` key with one of the following values to
change how functions are named in the generated import library:

  * `decorated`: The function name will be fully-decorated using the MSVC toolchain format.
  * `noprefix`: The function name will be decorated using the MSVC toolchain format, but skipping the leading `?`, `@`, or optionally `_`.
  * `undecorated`: The function name will not be decorated.

[items.extern.attributes.link.import_name_type.default]

If the `import_name_type` key is not specified, then the function name will be
fully-decorated using the target toolchain’s format.

[items.extern.attributes.link.import_name_type.variables]

Variables are never decorated and so the `import_name_type` key has no effect
on how they are named in the generated import library.

[items.extern.attributes.link.import_name_type.platform-specific]

The `import_name_type` key is only supported on x86 Windows. Using it when
targeting other platforms will result in a compiler error.

[items.extern.attributes.link_name]

### The `link_name` attribute

[items.extern.attributes.link_name.intro]

The _`link_name` attribute_ may be applied to declarations inside an `extern`
block to specify the symbol to import for the given function or static.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     unsafe extern "C" {
>         #[link_name = "actual_symbol_name"]
>         safe fn name_in_rust();
>     }
>     }

[items.extern.attributes.link_name.syntax]

The `link_name` attribute uses the MetaNameValueStr syntax.

[items.extern.attributes.link_name.allowed-positions]

The `link_name` attribute may only be applied to a function or static item in
an `extern` block.

> Note
>
> `rustc` ignores use in other positions but lints against it. This may become
> an error in the future.

[items.extern.attributes.link_name.duplicates]

Only the last use of `link_name` on an item has effect.

> Note
>
> `rustc` lints against any use preceding the last. This may become an error
> in the future.

[items.extern.attributes.link_name.link_ordinal]

The `link_name` attribute may not be used with the `link_ordinal` attribute.

[items.extern.attributes.link_ordinal]

### The `link_ordinal` attribute

[items.extern.attributes.link_ordinal.intro]

The _`link_ordinal` attribute_ can be applied on declarations inside an
`extern` block to indicate the numeric ordinal to use when generating the
import library to link against. An ordinal is a unique number per symbol
exported by a dynamic library on Windows and can be used when the library is
being loaded to find that symbol rather than having to look it up by name.

> Warning
>
> `link_ordinal` should only be used in cases where the ordinal of the symbol
> is known to be stable: if the ordinal of a symbol is not explicitly set when
> its containing binary is built then one will be automatically assigned to
> it, and that assigned ordinal may change between builds of the binary.
    
    
    #![allow(unused)]
    fn main() {
    #[cfg(all(windows, target_arch = "x86"))]
    #[link(name = "exporter", kind = "raw-dylib")]
    unsafe extern "stdcall" {
        #[link_ordinal(15)]
        safe fn imported_function_stdcall(i: i32);
    }
    }

[items.extern.attributes.link_ordinal.allowed-kinds]

This attribute is only used with the `raw-dylib` linking kind. Using any other
kind will result in a compiler error.

[items.extern.attributes.link_ordinal.exclusive]

Using this attribute with the `link_name` attribute will result in a compiler
error.

[items.extern.attributes.fn-parameters]

### Attributes on function parameters

Attributes on extern function parameters follow the same rules and
restrictions as regular function parameters.

* * *

  1. Starting with the 2024 Edition, the `unsafe` keyword is required semantically. ↩

[items.generics]

# Generic parameters

[items.generics.syntax]

**Syntax**  
GenericParams → < ( GenericParam ( , GenericParam )* ,? )? >

GenericParam → OuterAttribute* ( LifetimeParam | TypeParam | ConstParam )

LifetimeParam → Lifetime ( : LifetimeBounds )?

TypeParam → IDENTIFIER ( : TypeParamBounds? )? ( = Type )?

ConstParam →  
const IDENTIFIER : Type  
( = ( BlockExpression | IDENTIFIER | -? LiteralExpression ) )?

Show Railroad

GenericParams < GenericParam , GenericParam , >

GenericParam OuterAttribute LifetimeParam TypeParam ConstParam

LifetimeParam Lifetime : LifetimeBounds

TypeParam IDENTIFIER : TypeParamBounds = Type

ConstParam const IDENTIFIER : Type = BlockExpression IDENTIFIER -
LiteralExpression

[items.generics.syntax.intro]

Functions, type aliases, structs, enumerations, unions, traits, and
implementations may be _parameterized_ by types, constants, and lifetimes.
These parameters are listed in angle brackets (`<...>`), usually immediately
after the name of the item and before its definition. For implementations,
which don’t have a name, they come directly after `impl`.

[items.generics.syntax.decl-order]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/const-generics/argument_order.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/const-generics/argument_order.rs)

The order of generic parameters is restricted to lifetime parameters and then
type and const parameters intermixed.

[items.generics.syntax.duplicate-params]

The same parameter name may not be declared more than once in a GenericParams
list.

Some examples of items with type, const, and lifetime parameters:

    
    
    #![allow(unused)]
    fn main() {
    fn foo<'a, T>() {}
    trait A<U> {}
    struct Ref<'a, T> where T: 'a { r: &'a T }
    struct InnerArray<T, const N: usize>([T; N]);
    struct EitherOrderWorks<const N: bool, U>(U);
    }

[items.generics.syntax.scope]

Generic parameters are in scope within the item definition where they are
declared. They are not in scope for items declared within the body of a
function as described in item declarations. See generic parameter scopes for
more details.

[items.generics.builtin-generic-types]

References, raw pointers, arrays, slices, tuples, and function pointers have
lifetime or type parameters as well, but are not referred to with path syntax.

[items.generics.invalid-lifetimes]

`'_` and `'static` are not valid lifetime parameter names.

[items.generics.const]

### Const generics

[items.generics.const.intro]

_Const generic parameters_ allow items to be generic over constant values.

[items.generics.const.namespace]

The const identifier introduces a name in the value namespace for the constant
parameter, and all instances of the item must be instantiated with a value of
the given type.

[items.generics.const.allowed-types]

The only allowed types of const parameters are `u8`, `u16`, `u32`, `u64`,
`u128`, `usize`, `i8`, `i16`, `i32`, `i64`, `i128`, `isize`, `char` and
`bool`.

[items.generics.const.usage]

Const parameters can be used anywhere a const item can be used, with the
exception that when used in a type or array repeat expression, it must be
standalone (as described below). That is, they are allowed in the following
places:

  1. As an applied const to any type which forms a part of the signature of the item in question.
  2. As part of a const expression used to define an associated const, or as a parameter to an associated type.
  3. As a value in any runtime expression in the body of any functions in the item.
  4. As a parameter to any type used in the body of any functions in the item.
  5. As a part of the type of any fields in the item.

    
    
    #![allow(unused)]
    fn main() {
    // Examples where const generic parameters can be used.
    
    // Used in the signature of the item itself.
    fn foo<const N: usize>(arr: [i32; N]) {
        // Used as a type within a function body.
        let x: [i32; N];
        // Used as an expression.
        println!("{}", N * 2);
    }
    
    // Used as a field of a struct.
    struct Foo<const N: usize>([i32; N]);
    
    impl<const N: usize> Foo<N> {
        // Used as an associated constant.
        const CONST: usize = N * 4;
    }
    
    trait Trait {
        type Output;
    }
    
    impl<const N: usize> Trait for Foo<N> {
        // Used as an associated type.
        type Output = [i32; N];
    }
    }
    
    
    #![allow(unused)]
    fn main() {
    // Examples where const generic parameters cannot be used.
    fn foo<const N: usize>() {
        // Cannot use in item definitions within a function body.
        const BAD_CONST: [usize; N] = [1; N];
        static BAD_STATIC: [usize; N] = [1; N];
        fn inner(bad_arg: [usize; N]) {
            let bad_value = N * 2;
        }
        type BadAlias = [usize; N];
        struct BadStruct([usize; N]);
    }
    }

[items.generics.const.standalone]

As a further restriction, const parameters may only appear as a standalone
argument inside of a type or array repeat expression. In those contexts, they
may only be used as a single segment path expression, possibly inside a block
(such as `N` or `{N}`). That is, they cannot be combined with other
expressions.

    
    
    #![allow(unused)]
    fn main() {
    // Examples where const parameters may not be used.
    
    // Not allowed to combine in other expressions in types, such as the
    // arithmetic expression in the return type here.
    fn bad_function<const N: usize>() -> [u8; {N + 1}] {
        // Similarly not allowed for array repeat expressions.
        [1; {N + 1}]
    }
    }

[items.generics.const.argument]

A const argument in a path specifies the const value to use for that item.

[items.generics.const.argument.const-expr]

The argument must either be an inferred const or be a const expression of the
type ascribed to the const parameter. The const expression must be a block
expression (surrounded with braces) unless it is a single path segment (an
IDENTIFIER) or a literal (with a possibly leading `-` token).

> Note
>
> This syntactic restriction is necessary to avoid requiring infinite
> lookahead when parsing an expression inside of a type.
    
    
    #![allow(unused)]
    fn main() {
    struct S<const N: i64>;
    const C: i64 = 1;
    fn f<const N: i64>() -> S<N> { S }
    
    let _ = f::<1>(); // Literal.
    let _ = f::<-1>(); // Negative literal.
    let _ = f::<{ 1 + 2 }>(); // Constant expression.
    let _ = f::<C>(); // Single segment path.
    let _ = f::<{ C + 1 }>(); // Constant expression.
    let _: S<1> = f::<_>(); // Inferred const.
    let _: S<1> = f::<(((_)))>(); // Inferred const.
    }

> Note
>
> In a generic argument list, an inferred const is parsed as an inferred type
> but then semantically treated as a separate kind of const generic argument.

[items.generics.const.inferred]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/const-generics/generic_arg_infer/paren_infer.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/const-generics/generic_arg_infer/paren_infer.rs)

Where a const argument is expected, an `_` (optionally surrounded by any
number of matching parentheses), called the _inferred const_ (path rules,
array expression rules), can be used instead. This asks the compiler to infer
the const argument if possible based on surrounding information.

    
    
    #![allow(unused)]
    fn main() {
    fn make_buf<const N: usize>() -> [u8; N] {
        [0; _]
        //  ^ Infers `N`.
    }
    let _: [u8; 1024] = make_buf::<_>();
    //                             ^ Infers `1024`.
    }

> Note
>
> An inferred const is not semantically an expression and so is not accepted
> within braces.
>  
>  
>     #![allow(unused)]
>     fn main() {
>     fn f<const N: usize>() -> [u8; N] { [0; _] }
>     let _: [_; 1] = f::<{ _ }>();
>     //                    ^ ERROR `_` not allowed here
>     }

[items.generics.const.inferred.constraint]

The inferred const cannot be used in item signatures.

    
    
    #![allow(unused)]
    fn main() {
    fn f<const N: usize>(x: [u8; N]) -> [u8; _] { x }
    //                                       ^ ERROR not allowed
    }

[items.generics.const.type-ambiguity]

When there is ambiguity if a generic argument could be resolved as either a
type or const argument, it is always resolved as a type. Placing the argument
in a block expression can force it to be interpreted as a const argument.

    
    
    #![allow(unused)]
    fn main() {
    type N = u32;
    struct Foo<const N: usize>;
    // The following is an error, because `N` is interpreted as the type alias `N`.
    fn foo<const N: usize>() -> Foo<N> { todo!() } // ERROR
    // Can be fixed by wrapping in braces to force it to be interpreted as the `N`
    // const parameter:
    fn bar<const N: usize>() -> Foo<{ N }> { todo!() } // ok
    }

[items.generics.const.variance]

Unlike type and lifetime parameters, const parameters can be declared without
being used inside of a parameterized item, with the exception of
implementations as described in generic implementations:

    
    
    #![allow(unused)]
    fn main() {
    // ok
    struct Foo<const N: usize>;
    enum Bar<const M: usize> { A, B }
    
    // ERROR: unused parameter
    struct Baz<T>;
    struct Biz<'a>;
    struct Unconstrained;
    impl<const N: usize> Unconstrained {}
    }

[items.generics.const.exhaustiveness]

When resolving a trait bound obligation, the exhaustiveness of all
implementations of const parameters is not considered when determining if the
bound is satisfied. For example, in the following, even though all possible
const values for the `bool` type are implemented, it is still an error that
the trait bound is not satisfied:

    
    
    #![allow(unused)]
    fn main() {
    struct Foo<const B: bool>;
    trait Bar {}
    impl Bar for Foo<true> {}
    impl Bar for Foo<false> {}
    
    fn needs_bar(_: impl Bar) {}
    fn generic<const B: bool>() {
        let v = Foo::<B>;
        needs_bar(v); // ERROR: trait bound `Foo<B>: Bar` is not satisfied
    }
    }

[items.generics.where]

## Where clauses

[items.generics.where.syntax]

**Syntax**  
WhereClause → where ( WhereClauseItem , )* WhereClauseItem?

WhereClauseItem →  
LifetimeWhereClauseItem  
| TypeBoundWhereClauseItem

LifetimeWhereClauseItem → Lifetime : LifetimeBounds

TypeBoundWhereClauseItem → ForLifetimes? Type : TypeParamBounds?

Show Railroad

WhereClause where WhereClauseItem , WhereClauseItem

WhereClauseItem LifetimeWhereClauseItem TypeBoundWhereClauseItem

LifetimeWhereClauseItem Lifetime : LifetimeBounds

TypeBoundWhereClauseItem ForLifetimes Type : TypeParamBounds

[items.generics.where.intro]

_Where clauses_ provide another way to specify bounds on type and lifetime
parameters as well as a way to specify bounds on types that aren’t type
parameters.

[items.generics.where.higher-ranked-lifetimes]

The `for` keyword can be used to introduce higher-ranked lifetimes. It only
allows LifetimeParam parameters.

    
    
    #![allow(unused)]
    fn main() {
    struct A<T>
    where
        T: Iterator,            // Could use A<T: Iterator> instead
        T::Item: Copy,          // Bound on an associated type
        String: PartialEq<T>,   // Bound on `String`, using the type parameter
        i32: Default,           // Allowed, but not useful
    {
        f: T,
    }
    }

[items.generics.attributes]

## Attributes

Generic lifetime and type parameters allow attributes on them. There are no
built-in attributes that do anything in this position, although custom derive
attributes may give meaning to it.

This example shows using a custom derive attribute to modify the meaning of a
generic parameter.

    
    
    // Assume that the derive for MyFlexibleClone declared `my_flexible_clone` as
    // an attribute it understands.
    #[derive(MyFlexibleClone)]
    struct Foo<#[my_flexible_clone(unbounded)] H> {
        a: *const H
    }

[items.associated]

# Associated items

[items.associated.syntax]

**Syntax**  
AssociatedItem →  
OuterAttribute* (  
MacroInvocationSemi  
| ( Visibility? ( TypeAlias | ConstantItem | Function ) )   
)

Show Railroad

AssociatedItem OuterAttribute MacroInvocationSemi Visibility TypeAlias
ConstantItem Function

[items.associated.intro]

_Associated Items_ are the items declared in traits or defined in
implementations. They are called this because they are defined on an associate
type — the type in the implementation.

[items.associated.kinds]

They are a subset of the kinds of items you can declare in a module.
Specifically, there are associated functions (including methods), associated
types, and associated constants.

[items.associated.related]

Associated items are useful when the associated item is logically related to
the associating item. For example, the `is_some` method on `Option` is
intrinsically related to Options, so should be associated.

[items.associated.decl-def]

Every associated item kind comes in two varieties: definitions that contain
the actual implementation and declarations that declare signatures for
definitions.

[items.associated.trait-items]

It is the declarations that make up the contract of traits and what is
available on generic types.

[items.associated.fn]

## Associated functions and methods

[items.associated.fn.intro]

_Associated functions_ are functions associated with a type.

[items.associated.fn.decl]

An _associated function declaration_ declares a signature for an associated
function definition. It is written as a function item, except the function
body is replaced with a `;`.

[items.associated.name]

The identifier is the name of the function.

[items.associated.same-signature]

The generics, parameter list, return type, and where clause of the associated
function must be the same as the associated function declarations’s.

[items.associated.fn.def]

An _associated function definition_ defines a function associated with another
type. It is written the same as a function item.

> Note
>
> A common example is an associated function named `new` that returns a value
> of the type with which it is associated.
    
    
    struct Struct {
        field: i32
    }
    
    impl Struct {
        fn new() -> Struct {
            Struct {
                field: 0i32
            }
        }
    }
    
    fn main () {
        let _struct = Struct::new();
    }

[items.associated.fn.qualified-self]

When the associated function is declared on a trait, the function can also be
called with a path that is a path to the trait appended by the name of the
trait. When this happens, it is substituted for `<_ as Trait>::function_name`.

    
    
    #![allow(unused)]
    fn main() {
    trait Num {
        fn from_i32(n: i32) -> Self;
    }
    
    impl Num for f64 {
        fn from_i32(n: i32) -> f64 { n as f64 }
    }
    
    // These 4 are all equivalent in this case.
    let _: f64 = Num::from_i32(42);
    let _: f64 = <_ as Num>::from_i32(42);
    let _: f64 = <f64 as Num>::from_i32(42);
    let _: f64 = f64::from_i32(42);
    }

[items.associated.fn.method]

### Methods

[items.associated.fn.method.intro]

Associated functions whose first parameter is named `self` are called
_methods_ and may be invoked using the method call operator, for example,
`x.foo()`, as well as the usual function call notation.

[items.associated.fn.method.self-ty]

If the type of the `self` parameter is specified, it is limited to types
resolving to one generated by the following grammar (where `'lt` denotes some
arbitrary lifetime):

    
    
    P = &'lt S | &'lt mut S | Box<S> | Rc<S> | Arc<S> | Pin<P>
    S = Self | P
    

The `Self` terminal in this grammar denotes a type resolving to the
implementing type. This can also include the contextual type alias `Self`,
other type aliases, or associated type projections resolving to the
implementing type.

    
    
    #![allow(unused)]
    fn main() {
    use std::rc::Rc;
    use std::sync::Arc;
    use std::pin::Pin;
    // Examples of methods implemented on struct `Example`.
    struct Example;
    type Alias = Example;
    trait Trait { type Output; }
    impl Trait for Example { type Output = Example; }
    impl Example {
        fn by_value(self: Self) {}
        fn by_ref(self: &Self) {}
        fn by_ref_mut(self: &mut Self) {}
        fn by_box(self: Box<Self>) {}
        fn by_rc(self: Rc<Self>) {}
        fn by_arc(self: Arc<Self>) {}
        fn by_pin(self: Pin<&Self>) {}
        fn explicit_type(self: Arc<Example>) {}
        fn with_lifetime<'a>(self: &'a Self) {}
        fn nested<'a>(self: &mut &'a Arc<Rc<Box<Alias>>>) {}
        fn via_projection(self: <Example as Trait>::Output) {}
    }
    }

[associated.fn.method.self-pat-shorthands]

Shorthand syntax can be used without specifying a type, which have the
following equivalents:

Shorthand| Equivalent  
---|---  
`self`| `self: Self`  
`&'lifetime self`| `self: &'lifetime Self`  
`&'lifetime mut self`| `self: &'lifetime mut Self`  
  
> Note
>
> Lifetimes can be, and usually are, elided with this shorthand.

[associated.fn.method.self-pat-mut]

If the `self` parameter is prefixed with `mut`, it becomes a mutable variable,
similar to regular parameters using a `mut` identifier pattern. For example:

    
    
    #![allow(unused)]
    fn main() {
    trait Changer: Sized {
        fn change(mut self) {}
        fn modify(mut self: Box<Self>) {}
    }
    }

As an example of methods on a trait, consider the following:

    
    
    #![allow(unused)]
    fn main() {
    type Surface = i32;
    type BoundingBox = i32;
    trait Shape {
        fn draw(&self, surface: Surface);
        fn bounding_box(&self) -> BoundingBox;
    }
    }

This defines a trait with two methods. All values that have implementations of
this trait while the trait is in scope can have their `draw` and
`bounding_box` methods called.

    
    
    #![allow(unused)]
    fn main() {
    type Surface = i32;
    type BoundingBox = i32;
    trait Shape {
        fn draw(&self, surface: Surface);
        fn bounding_box(&self) -> BoundingBox;
    }
    
    struct Circle {
        // ...
    }
    
    impl Shape for Circle {
        // ...
      fn draw(&self, _: Surface) {}
      fn bounding_box(&self) -> BoundingBox { 0i32 }
    }
    
    impl Circle {
        fn new() -> Circle { Circle{} }
    }
    
    let circle_shape = Circle::new();
    let bounding_box = circle_shape.bounding_box();
    }

[items.associated.fn.params.edition2018]

> 2018 Edition differences
>
> In the 2015 edition, it is possible to declare trait methods with anonymous
> parameters (e.g. `fn foo(u8)`). This is deprecated and an error as of the
> 2018 edition. All parameters must have an argument name.

[items.associated.fn.param-attributes]

#### Attributes on method parameters

Attributes on method parameters follow the same rules and restrictions as
regular function parameters.

[items.associated.type]

## Associated types

[items.associated.type.intro]

_Associated types_ are type aliases associated with another type.

[items.associated.type.restrictions]

Associated types cannot be defined in inherent implementations nor can they be
given a default implementation in traits.

[items.associated.type.decl]

An _associated type declaration_ declares a signature for associated type
definitions. It is written in one of the following forms, where `Assoc` is the
name of the associated type, `Params` is a comma-separated list of type,
lifetime or const parameters, `Bounds` is a plus-separated list of trait
bounds that the associated type must meet, and `WhereBounds` is a comma-
separated list of bounds that the parameters must meet:

    
    
    type Assoc;
    type Assoc: Bounds;
    type Assoc<Params>;
    type Assoc<Params>: Bounds;
    type Assoc<Params> where WhereBounds;
    type Assoc<Params>: Bounds where WhereBounds;

[items.associated.type.name]

The identifier is the name of the declared type alias.

[items.associated.type.impl-fulfillment]

The optional trait bounds must be fulfilled by the implementations of the type
alias.

[items.associated.type.sized]

There is an implicit `Sized` bound on associated types that can be relaxed
using the special `?Sized` bound.

[items.associated.type.def]

An _associated type definition_ defines a type alias for the implementation of
a trait on a type.

[items.associated.type.def.restriction]

They are written similarly to an _associated type declaration_ , but cannot
contain `Bounds`, but instead must contain a `Type`:

    
    
    type Assoc = Type;
    type Assoc<Params> = Type; // the type `Type` here may reference `Params`
    type Assoc<Params> = Type where WhereBounds;
    type Assoc<Params> where WhereBounds = Type; // deprecated, prefer the form above

[items.associated.type.alias]

If a type `Item` has an associated type `Assoc` from a trait `Trait`, then
`<Item as Trait>::Assoc` is a type that is an alias of the type specified in
the associated type definition.

[items.associated.type.param]

Furthermore, if `Item` is a type parameter, then `Item::Assoc` can be used in
type parameters.

[items.associated.type.generic]

Associated types may include generic parameters and where clauses; these are
often referred to as _generic associated types_ , or _GATs_. If the type
`Thing` has an associated type `Item` from a trait `Trait` with the generics
`<'a>` , the type can be named like `<Thing as Trait>::Item<'x>`, where `'x`
is some lifetime in scope. In this case, `'x` will be used wherever `'a`
appears in the associated type definitions on impls.

    
    
    trait AssociatedType {
        // Associated type declaration
        type Assoc;
    }
    
    struct Struct;
    
    struct OtherStruct;
    
    impl AssociatedType for Struct {
        // Associated type definition
        type Assoc = OtherStruct;
    }
    
    impl OtherStruct {
        fn new() -> OtherStruct {
            OtherStruct
        }
    }
    
    fn main() {
        // Usage of the associated type to refer to OtherStruct as <Struct as AssociatedType>::Assoc
        let _other_struct: OtherStruct = <Struct as AssociatedType>::Assoc::new();
    }

An example of associated types with generics and where clauses:

    
    
    struct ArrayLender<'a, T>(&'a mut [T; 16]);
    
    trait Lend {
        // Generic associated type declaration
        type Lender<'a> where Self: 'a;
        fn lend<'a>(&'a mut self) -> Self::Lender<'a>;
    }
    
    impl<T> Lend for [T; 16] {
        // Generic associated type definition
        type Lender<'a> = ArrayLender<'a, T> where Self: 'a;
    
        fn lend<'a>(&'a mut self) -> Self::Lender<'a> {
            ArrayLender(self)
        }
    }
    
    fn borrow<'a, T: Lend>(array: &'a mut T) -> <T as Lend>::Lender<'a> {
        array.lend()
    }
    
    fn main() {
        let mut array = [0usize; 16];
        let lender = borrow(&mut array);
    }

### Associated types container example

Consider the following example of a `Container` trait. Notice that the type is
available for use in the method signatures:

    
    
    #![allow(unused)]
    fn main() {
    trait Container {
        type E;
        fn empty() -> Self;
        fn insert(&mut self, elem: Self::E);
    }
    }

In order for a type to implement this trait, it must not only provide
implementations for every method, but it must specify the type `E`. Here’s an
implementation of `Container` for the standard library type `Vec`:

    
    
    #![allow(unused)]
    fn main() {
    trait Container {
        type E;
        fn empty() -> Self;
        fn insert(&mut self, elem: Self::E);
    }
    impl<T> Container for Vec<T> {
        type E = T;
        fn empty() -> Vec<T> { Vec::new() }
        fn insert(&mut self, x: T) { self.push(x); }
    }
    }

### Relationship between `Bounds` and `WhereBounds`

In this example:

    
    
    #![allow(unused)]
    fn main() {
    use std::fmt::Debug;
    trait Example {
        type Output<T>: Ord where T: Debug;
    }
    }

Given a reference to the associated type like `<X as Example>::Output<Y>`, the
associated type itself must be `Ord`, and the type `Y` must be `Debug`.

[items.associated.type.generic-where-clause]

### Required where clauses on generic associated types

[items.associated.type.generic-where-clause.intro]

Generic associated type declarations on traits currently may require a list of
where clauses, dependent on functions in the trait and how the GAT is used.
These rules may be loosened in the future; updates can be found [on the
generic associated types initiative repository](https://rust-
lang.github.io/generic-associated-types-
initiative/explainer/required_bounds.html).

[items.associated.type.generic-where-clause.valid-fn]

In a few words, these where clauses are required in order to maximize the
allowed definitions of the associated type in impls. To do this, any clauses
that _can be proven to hold_ on functions (using the parameters of the
function or trait) where a GAT appears as an input or output must also be
written on the GAT itself.

    
    
    #![allow(unused)]
    fn main() {
    trait LendingIterator {
        type Item<'x> where Self: 'x;
        fn next<'a>(&'a mut self) -> Self::Item<'a>;
    }
    }

In the above, on the `next` function, we can prove that `Self: 'a`, because of
the implied bounds from `&'a mut self`; therefore, we must write the
equivalent bound on the GAT itself: `where Self: 'x`.

[items.associated.type.generic-where-clause.intersection]

When there are multiple functions in a trait that use the GAT, then the
_intersection_ of the bounds from the different functions are used, rather
than the union.

    
    
    #![allow(unused)]
    fn main() {
    trait Check<T> {
        type Checker<'x>;
        fn create_checker<'a>(item: &'a T) -> Self::Checker<'a>;
        fn do_check(checker: Self::Checker<'_>);
    }
    }

In this example, no bounds are required on the `type Checker<'a>;`. While we
know that `T: 'a` on `create_checker`, we do not know that on `do_check`.
However, if `do_check` was commented out, then the `where T: 'x` bound would
be required on `Checker`.

[items.associated.type.generic-where-clause.forward]

The bounds on associated types also propagate required where clauses.

    
    
    #![allow(unused)]
    fn main() {
    trait Iterable {
        type Item<'a> where Self: 'a;
        type Iterator<'a>: Iterator<Item = Self::Item<'a>> where Self: 'a;
        fn iter<'a>(&'a self) -> Self::Iterator<'a>;
    }
    }

Here, `where Self: 'a` is required on `Item` because of `iter`. However,
`Item` is used in the bounds of `Iterator`, the `where Self: 'a` clause is
also required there.

[items.associated.type.generic-where-clause.static]

Finally, any explicit uses of `'static` on GATs in the trait do not count
towards the required bounds.

    
    
    #![allow(unused)]
    fn main() {
    trait StaticReturn {
        type Y<'a>;
        fn foo(&self) -> Self::Y<'static>;
    }
    }

[items.associated.const]

## Associated constants

[items.associated.const.intro]

_Associated constants_ are constants associated with a type.

[items.associated.const.decl]

An _associated constant declaration_ declares a signature for associated
constant definitions. It is written as `const`, then an identifier, then `:`,
then a type, finished by a `;`.

[items.associated.const.name]

The identifier is the name of the constant used in the path. The type is the
type that the definition has to implement.

[items.associated.const.def]

An _associated constant definition_ defines a constant associated with a type.
It is written the same as a constant item.

[items.associated.const.eval]

Associated constant definitions undergo constant evaluation only when
referenced. Further, definitions that include generic parameters are evaluated
after monomorphization.

    
    
    struct Struct;
    struct GenericStruct<const ID: i32>;
    
    impl Struct {
        // Definition not immediately evaluated
        const PANIC: () = panic!("compile-time panic");
    }
    
    impl<const ID: i32> GenericStruct<ID> {
        // Definition not immediately evaluated
        const NON_ZERO: () = if ID == 0 {
            panic!("contradiction")
        };
    }
    
    fn main() {
        // Referencing Struct::PANIC causes compilation error
        let _ = Struct::PANIC;
    
        // Fine, ID is not 0
        let _ = GenericStruct::<1>::NON_ZERO;
    
        // Compilation error from evaluating NON_ZERO with ID=0
        let _ = GenericStruct::<0>::NON_ZERO;
    }

### Associated constants examples

A basic example:

    
    
    trait ConstantId {
        const ID: i32;
    }
    
    struct Struct;
    
    impl ConstantId for Struct {
        const ID: i32 = 1;
    }
    
    fn main() {
        assert_eq!(1, Struct::ID);
    }

Using default values:

    
    
    trait ConstantIdDefault {
        const ID: i32 = 1;
    }
    
    struct Struct;
    struct OtherStruct;
    
    impl ConstantIdDefault for Struct {}
    
    impl ConstantIdDefault for OtherStruct {
        const ID: i32 = 5;
    }
    
    fn main() {
        assert_eq!(1, Struct::ID);
        assert_eq!(5, OtherStruct::ID);
    }

[attributes]

# Attributes

[attributes.syntax]

**Syntax**  
InnerAttribute → # ! [ Attr ]

OuterAttribute → # [ Attr ]

Attr →  
SimplePath AttrInput?  
| unsafe ( SimplePath AttrInput? )

AttrInput →  
DelimTokenTree  
| = Expression

Show Railroad

InnerAttribute # ! [ Attr ]

OuterAttribute # [ Attr ]

Attr SimplePath AttrInput unsafe ( SimplePath AttrInput )

AttrInput DelimTokenTree = Expression

[attributes.intro]

An _attribute_ is a general, free-form metadatum that is interpreted according
to name, convention, language, and compiler version. Attributes are modeled on
Attributes in [ECMA-335](https://www.ecma-international.org/publications-and-
standards/standards/ecma-335/), with the syntax coming from
[ECMA-334](https://www.ecma-international.org/publications-and-
standards/standards/ecma-334/) (C#).

[attributes.inner]

_Inner attributes_ , written with a bang (`!`) after the hash (`#`), apply to
the form that the attribute is declared within.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     // General metadata applied to the enclosing module or crate.
>     #![crate_type = "lib"]
>  
>     // Inner attribute applies to the entire function.
>     fn some_unused_variables() {
>       #![allow(unused_variables)]
>  
>       let x = ();
>       let y = ();
>       let z = ();
>     }
>     }

[attributes.outer]

_Outer attributes_ , written without the bang after the hash, apply to the
form that follows the attribute.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     // A function marked as a unit test
>     #[test]
>     fn test_foo() {
>         /* ... */
>     }
>  
>     // A conditionally-compiled module
>     #[cfg(target_os = "linux")]
>     mod bar {
>         /* ... */
>     }
>  
>     // A lint attribute used to suppress a warning/error
>     #[allow(non_camel_case_types)]
>     type int8_t = i8;
>     }

[attributes.input]

The attribute consists of a path to the attribute, followed by an optional
delimited token tree whose interpretation is defined by the attribute.
Attributes other than macro attributes also allow the input to be an equals
sign (`=`) followed by an expression. See the meta item syntax below for more
details.

[attributes.safety]

An attribute may be unsafe to apply. To avoid undefined behavior when using
these attributes, certain obligations that cannot be checked by the compiler
must be met. To assert these have been, the attribute is wrapped in
`unsafe(..)`, e.g. `#[unsafe(no_mangle)]`.

The following attributes are unsafe:

  * `export_name`
  * `link_section`
  * `naked`
  * `no_mangle`

[attributes.kind]

Attributes can be classified into the following kinds:

  * Built-in attributes
  * Proc macro attributes
  * Derive macro helper attributes
  * Tool attributes

[attributes.allowed-position]

Attributes may be applied to many forms in the language:

  * All item declarations accept outer attributes while external blocks, functions, implementations, and modules accept inner attributes.
  * Most statements accept outer attributes (see Expression Attributes for limitations on expression statements).
  * Block expressions accept outer and inner attributes, but only when they are the outer expression of an expression statement or the final expression of another block expression.
  * Enum variants and struct and union fields accept outer attributes.
  * Match expression arms accept outer attributes.
  * Generic lifetime or type parameter accept outer attributes.
  * Expressions accept outer attributes in limited situations, see Expression Attributes for details.
  * Function, closure and function pointer parameters accept outer attributes. This includes attributes on variadic parameters denoted with `...` in function pointers and external blocks.
  * Inline assembly template strings and operands accept outer attributes. Only certain attributes are accepted semantically; for details, see asm.attributes.supported-attributes.

[attributes.meta]

## Meta item attribute syntax

[attributes.meta.intro]

A “meta item” is the syntax used for the Attr rule by most built-in
attributes. It has the following grammar:

[attributes.meta.syntax]

**Syntax**  
MetaItem →  
SimplePath  
| SimplePath = Expression  
| SimplePath ( MetaSeq? )

MetaSeq →  
MetaItemInner ( , MetaItemInner )* ,?

MetaItemInner →  
MetaItem  
| Expression

Show Railroad

MetaItem SimplePath SimplePath = Expression SimplePath ( MetaSeq )

MetaSeq MetaItemInner , MetaItemInner ,

MetaItemInner MetaItem Expression

[attributes.meta.literal-expr]

Expressions in meta items must macro-expand to literal expressions, which must
not include integer or float type suffixes. Expressions which are not literal
expressions will be syntactically accepted (and can be passed to proc-macros),
but will be rejected after parsing.

[attributes.meta.order]

Note that if the attribute appears within another macro, it will be expanded
after that outer macro. For example, the following code will expand the
`Serialize` proc-macro first, which must preserve the `include_str!` call in
order for it to be expanded:

    
    
    #[derive(Serialize)]
    struct Foo {
        #[doc = include_str!("x.md")]
        x: u32
    }

[attributes.meta.order-macro]

Additionally, macros in attributes will be expanded only after all other
attributes applied to the item:

    
    
    #[macro_attr1] // expanded first
    #[doc = mac!()] // `mac!` is expanded fourth.
    #[macro_attr2] // expanded second
    #[derive(MacroDerive1, MacroDerive2)] // expanded third
    fn foo() {}

[attributes.meta.builtin]

Various built-in attributes use different subsets of the meta item syntax to
specify their inputs. The following grammar rules show some commonly used
forms:

[attributes.meta.builtin.syntax]

**Syntax**  
MetaWord →  
IDENTIFIER

MetaNameValueStr →  
IDENTIFIER = ( STRING_LITERAL | RAW_STRING_LITERAL )

MetaListPaths →  
IDENTIFIER ( ( SimplePath ( , SimplePath )* ,? )? )

MetaListIdents →  
IDENTIFIER ( ( IDENTIFIER ( , IDENTIFIER )* ,? )? )

MetaListNameValueStr →  
IDENTIFIER ( ( MetaNameValueStr ( , MetaNameValueStr )* ,? )? )

Show Railroad

MetaWord IDENTIFIER

MetaNameValueStr IDENTIFIER = STRING_LITERAL RAW_STRING_LITERAL

MetaListPaths IDENTIFIER ( SimplePath , SimplePath , )

MetaListIdents IDENTIFIER ( IDENTIFIER , IDENTIFIER , )

MetaListNameValueStr IDENTIFIER ( MetaNameValueStr , MetaNameValueStr , )

Some examples of meta items are:

Style| Example  
---|---  
MetaWord| `no_std`  
MetaNameValueStr| `doc = "example"`  
MetaListPaths| `allow(unused, clippy::inline_always)`  
MetaListIdents| `macro_use(foo, bar)`  
MetaListNameValueStr| `link(name = "CoreFoundation", kind = "framework")`  
  
[attributes.activity]

## Active and inert attributes

[attributes.activity.intro]

An attribute is either active or inert. During attribute processing, _active
attributes_ remove themselves from the form they are on while _inert
attributes_ stay on.

The `cfg` and `cfg_attr` attributes are active. Attribute macros are active.
All other attributes are inert.

[attributes.tool]

## Tool attributes

[attributes.tool.intro]

The compiler may allow attributes for external tools where each tool resides
in its own module in the tool prelude. The first segment of the attribute path
is the name of the tool, with one or more additional segments whose
interpretation is up to the tool.

[attributes.tool.ignored]

When a tool is not in use, the tool’s attributes are accepted without a
warning. When the tool is in use, the tool is responsible for processing and
interpretation of its attributes.

[attributes.tool.prelude]

Tool attributes are not available if the `no_implicit_prelude` attribute is
used.

    
    
    #![allow(unused)]
    fn main() {
    // Tells the rustfmt tool to not format the following element.
    #[rustfmt::skip]
    struct S {
    }
    
    // Controls the "cyclomatic complexity" threshold for the clippy tool.
    #[clippy::cyclomatic_complexity = "100"]
    pub fn f() {}
    }

> Note
>
> `rustc` currently recognizes the tools “clippy”, “rustfmt”, “diagnostic”,
> “miri”, and “rust_analyzer”.

[attributes.builtin]

## Built-in attributes index

The following is an index of all built-in attributes.

  * Conditional compilation

    * `cfg` — Controls conditional compilation.
    * `cfg_attr` — Conditionally includes attributes.
  * Testing

    * `test` — Marks a function as a test.
    * `ignore` — Disables a test function.
    * `should_panic` — Indicates a test should generate a panic.
  * Derive

    * `derive` — Automatic trait implementations.
    * `automatically_derived` — Marker for implementations created by `derive`.
  * Macros

    * `macro_export` — Exports a `macro_rules` macro for cross-crate usage.
    * `macro_use` — Expands macro visibility, or imports macros from other crates.
    * `proc_macro` — Defines a function-like macro.
    * `proc_macro_derive` — Defines a derive macro.
    * `proc_macro_attribute` — Defines an attribute macro.
  * Diagnostics

    * `allow`, `expect`, `warn`, `deny`, `forbid` — Alters the default lint level.
    * `deprecated` — Generates deprecation notices.
    * `must_use` — Generates a lint for unused values.
    * `diagnostic::on_unimplemented` — Hints the compiler to emit a certain error message if a trait is not implemented.
    * `diagnostic::do_not_recommend` — Hints the compiler to not show a certain trait impl in error messages.
  * ABI, linking, symbols, and FFI

    * `link` — Specifies a native library to link with an `extern` block.
    * `link_name` — Specifies the name of the symbol for functions or statics in an `extern` block.
    * `link_ordinal` — Specifies the ordinal of the symbol for functions or statics in an `extern` block.
    * `no_link` — Prevents linking an extern crate.
    * `repr` — Controls type layout.
    * `crate_type` — Specifies the type of crate (library, executable, etc.).
    * `no_main` — Disables emitting the `main` symbol.
    * `export_name` — Specifies the exported symbol name for a function or static.
    * `link_section` — Specifies the section of an object file to use for a function or static.
    * `no_mangle` — Disables symbol name encoding.
    * `used` — Forces the compiler to keep a static item in the output object file.
    * `crate_name` — Specifies the crate name.
  * Code generation

    * `inline` — Hint to inline code.
    * `cold` — Hint that a function is unlikely to be called.
    * `naked` — Prevent the compiler from emitting a function prologue and epilogue.
    * `no_builtins` — Disables use of certain built-in functions.
    * `target_feature` — Configure platform-specific code generation.
    * `track_caller` — Pass the parent call location to `std::panic::Location::caller()`.
    * `instruction_set` — Specify the instruction set used to generate a function’s code.
  * Documentation

    * `doc` — Specifies documentation. See [The Rustdoc Book](../rustdoc/the-doc-attribute.html) for more information. Doc comments are transformed into `doc` attributes.
  * Preludes

    * `no_std` — Removes std from the prelude.
    * `no_implicit_prelude` — Disables prelude lookups within a module.
  * Modules

    * `path` — Specifies the filename for a module.
  * Limits

    * `recursion_limit` — Sets the maximum recursion limit for certain compile-time operations.
    * `type_length_limit` — Sets the maximum size of a polymorphic type.
  * Runtime

    * `panic_handler` — Sets the function to handle panics.
    * `global_allocator` — Sets the global memory allocator.
    * `windows_subsystem` — Specifies the windows subsystem to link with.
  * Features

    * `feature` — Used to enable unstable or experimental compiler features. See [The Unstable Book](../unstable-book/index.html) for features implemented in `rustc`.
  * Type System

    * `non_exhaustive` — Indicate that a type will have more fields/variants added in future.
  * Debugger

    * `debugger_visualizer` — Embeds a file that specifies debugger output for a type.
    * `collapse_debuginfo` — Controls how macro invocations are encoded in debuginfo.

[attributes.testing]

# Testing attributes

The following attributes are used for specifying functions for performing
tests. Compiling a crate in “test” mode enables building the test functions
along with a test harness for executing the tests. Enabling the test mode also
enables the `test` conditional compilation option.

[attributes.testing.test]

## The `test` attribute

[attributes.testing.test.intro]

The _`test` attribute_ marks a function to be executed as a test.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     pub fn add(left: u64, right: u64) -> u64 { left + right }
>     #[test]
>     fn it_works() {
>         let result = add(2, 2);
>         assert_eq!(result, 4);
>     }
>     }

[attributes.testing.test.syntax]

The `test` attribute uses the MetaWord syntax.

[attributes.testing.test.allowed-positions]

The `test` attribute may only be applied to free functions that are
monomorphic, that take no arguments, and where the return type implements the
[`Termination`](../std/process/trait.Termination.html) trait.

> Note
>
> Some of types that implement the
> [`Termination`](../std/process/trait.Termination.html) trait include:
>
>   * `()`
>   * `Result<T, E> where T: Termination, E: Debug`
>

[attributes.testing.test.duplicates]

Only the first use of `test` on a function has effect.

> Note
>
> `rustc` lints against any use following the first. This may become an error
> in the future.

[attributes.testing.test.stdlib]

The `test` attribute is exported from the standard library prelude as
[`std::prelude::v1::test`](../core/macros/builtin/attr.test.html).

[attributes.testing.test.enabled]

These functions are only compiled when in test mode.

> Note
>
> The test mode is enabled by passing the `--test` argument to `rustc` or
> using `cargo test`.

[attributes.testing.test.success]

The test harness calls the returned value’s
[`report`](../std/process/trait.Termination.html#tymethod.report) method, and
classifies the test as passed or failed depending on whether the resulting
[`ExitCode`](../std/process/struct.ExitCode.html) represents successful
termination. In particular:

  * Tests that return `()` pass as long as they terminate and do not panic.
  * Tests that return a `Result<(), E>` pass as long as they return `Ok(())`.
  * Tests that return `ExitCode::SUCCESS` pass, and tests that return `ExitCode::FAILURE` fail.
  * Tests that do not terminate neither pass nor fail.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     use std::io;
>     fn setup_the_thing() -> io::Result<i32> { Ok(1) }
>     fn do_the_thing(s: &i32) -> io::Result<()> { Ok(()) }
>     #[test]
>     fn test_the_thing() -> io::Result<()> {
>         let state = setup_the_thing()?; // expected to succeed
>         do_the_thing(&state)?;          // expected to succeed
>         Ok(())
>     }
>     }

[attributes.testing.ignore]

## The `ignore` attribute

[attributes.testing.ignore.intro]

The _`ignore` attribute_ can be used with the `test` attribute to tell the
test harness to not execute that function as a test.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[test]
>     #[ignore]
>     fn check_thing() {
>         // …
>     }
>     }

> Note
>
> The `rustc` test harness supports the `--include-ignored` flag to force
> ignored tests to be run.

[attributes.testing.ignore.syntax]

The `ignore` attribute uses the MetaWord and MetaNameValueStr syntaxes.

[attributes.testing.ignore.reason]

The MetaNameValueStr form of the `ignore` attribute provides a way to specify
a reason why the test is ignored.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[test]
>     #[ignore = "not yet implemented"]
>     fn mytest() {
>         // …
>     }
>     }

[attributes.testing.ignore.allowed-positions]

The `ignore` attribute may only be applied to functions annotated with the
`test` attribute.

> Note
>
> `rustc` ignores use in other positions but lints against it. This may become
> an error in the future.

[attributes.testing.ignore.duplicates]

Only the first use of `ignore` on a function has effect.

> Note
>
> `rustc` lints against any use following the first. This may become an error
> in the future.

[attributes.testing.ignore.behavior]

Ignored tests are still compiled when in test mode, but they are not executed.

[attributes.testing.should_panic]

## The `should_panic` attribute

[attributes.testing.should_panic.intro]

The _`should_panic` attribute_ causes a test to pass only if the test function
to which the attribute is applied panics.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[test]
>     #[should_panic(expected = "values don't match")]
>     fn mytest() {
>         assert_eq!(1, 2, "values don't match");
>     }
>     }

[attributes.testing.should_panic.syntax]

The `should_panic` attribute has these forms:

  * MetaWord

> Example
>  
>         #![allow(unused)]
>         fn main() {
>         #[test]
>         #[should_panic]
>         fn mytest() { panic!("error: some message, and more"); }
>         }

  * MetaNameValueStr — The given string must appear within the panic message for the test to pass.

> Example
>  
>         #![allow(unused)]
>         fn main() {
>         #[test]
>         #[should_panic = "some message"]
>         fn mytest() { panic!("error: some message, and more"); }
>         }

  * MetaListNameValueStr — As with the MetaNameValueStr syntax, the given string must appear within the panic message.

> Example
>  
>         #![allow(unused)]
>         fn main() {
>         #[test]
>         #[should_panic(expected = "some message")]
>         fn mytest() { panic!("error: some message, and more"); }
>         }

[attributes.testing.should_panic.allowed-positions]

The `should_panic` attribute may only be applied to functions annotated with
the `test` attribute.

> Note
>
> `rustc` ignores use in other positions but lints against it. This may become
> an error in the future.

[attributes.testing.should_panic.duplicates]

Only the first use of `should_panic` on a function has effect.

> Note
>
> `rustc` lints against any use following the first with a future-
> compatibility warning. This may become an error in the future.

[attributes.testing.should_panic.expected]

When the MetaNameValueStr form or the MetaListNameValueStr form with the
`expected` key is used, the given string must appear somewhere within the
panic message for the test to pass.

[attributes.testing.should_panic.return]

The return type of the test function must be `()`.

[attributes.derive]

# Derive

[attributes.derive.intro]

The _`derive` attribute_ invokes one or more derive macros, allowing new items
to be automatically generated for data structures. You can create `derive`
macros with procedural macros.

> Example
>
> The [`PartialEq`](../core/cmp/derive.PartialEq.html) derive macro emits an
> implementation of [`PartialEq`](../core/cmp/trait.PartialEq.html) for
> `Foo<T> where T: PartialEq`. The [`Clone`](../core/clone/derive.Clone.html)
> derive macro does likewise for [`Clone`](../core/clone/trait.Clone.html).
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[derive(PartialEq, Clone)]
>     struct Foo<T> {
>         a: i32,
>         b: T,
>     }
>     }
>
> The generated `impl` items are equivalent to:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     struct Foo<T> { a: i32, b: T }
>     impl<T: PartialEq> PartialEq for Foo<T> {
>         fn eq(&self, other: &Foo<T>) -> bool {
>             self.a == other.a && self.b == other.b
>         }
>     }
>  
>     impl<T: Clone> Clone for Foo<T> {
>         fn clone(&self) -> Self {
>             Foo { a: self.a.clone(), b: self.b.clone() }
>         }
>     }
>     }

[attributes.derive.syntax]

The `derive` attribute uses the MetaListPaths syntax to specify a list of
paths to derive macros to invoke.

[attributes.derive.allowed-positions]

The `derive` attribute may only be applied to structs, enums, and unions.

[attributes.derive.duplicates]

The `derive` attribute may be used any number of times on an item. All derive
macros listed in all attributes are invoked.

[attributes.derive.stdlib]

The `derive` attribute is exported in the standard library prelude as
[`core::prelude::v1::derive`](../core/macros/builtin/attr.derive.html).

[attributes.derive.built-in]

Built-in derives are defined in the language prelude. The list of built-in
derives are:

  * [`Clone`](../core/clone/trait.Clone.html)
  * [`Copy`](../core/marker/trait.Copy.html)
  * [`Debug`](../core/fmt/macros/derive.Debug.html)
  * [`Default`](../core/default/trait.Default.html)
  * [`Eq`](../core/cmp/trait.Eq.html)
  * [`Hash`](../core/hash/macros/derive.Hash.html)
  * [`Ord`](../core/cmp/trait.Ord.html)
  * [`PartialEq`](../core/cmp/trait.PartialEq.html)
  * [`PartialOrd`](../core/cmp/trait.PartialOrd.html)

[attributes.derive.built-in-automatically_derived]

The built-in derives include the `automatically_derived` attribute on the
implementations they generate.

[attributes.derive.behavior]

During macro expansion, for each element in the list of derives, the
corresponding derive macro expands to zero or more items.

[attributes.derive.automatically_derived]

## The `automatically_derived` attribute

[attributes.derive.automatically_derived.intro]

The _`automatically_derived` attribute_ is used to annotate an implementation
to indicate that it was automatically created by a derive macro. It has no
direct effect, but it may be used by tools and diagnostic lints to detect
these automatically generated implementations.

> Example
>
> Given [`#[derive(Clone)]`](../core/clone/derive.Clone.html) on `struct
> Example`, the derive macro may produce:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     struct Example;
>     #[automatically_derived]
>     impl ::core::clone::Clone for Example {
>         #[inline]
>         fn clone(&self) -> Self {
>             Example
>         }
>     }
>     }

[attributes.derive.automatically_derived.syntax]

The `automatically_derived` attribute uses the MetaWord syntax.

[attributes.derive.automatically_derived.allowed-positions]

The `automatically_derived` attribute may only be applied to an
implementation.

> Note
>
> `rustc` ignores use in other positions but lints against it. This may become
> an error in the future.

[attributes.derive.automatically_derived.duplicates]

Using `automatically_derived` more than once on an implementation has the same
effect as using it once.

> Note
>
> `rustc` lints against any use following the first.

[attributes.derive.automatically_derived.behavior]

The `automatically_derived` attribute has no behavior.

[attributes.diagnostics]

# Diagnostic attributes

The following attributes are used for controlling or generating diagnostic
messages during compilation.

[attributes.diagnostics.lint]

## Lint check attributes

A lint check names a potentially undesirable coding pattern, such as
unreachable code or omitted documentation.

[attributes.diagnostics.lint.level]

The lint attributes `allow`, `expect`, `warn`, `deny`, and `forbid` use the
MetaListPaths syntax to specify a list of lint names to change the lint level
for the entity to which the attribute applies.

For any lint check `C`:

[attributes.diagnostics.lint.allow]

  * `#[allow(C)]` overrides the check for `C` so that violations will go unreported.

[attributes.diagnostics.lint.expect]

  * `#[expect(C)]` indicates that lint `C` is expected to be emitted. The attribute will suppress the emission of `C` or issue a warning, if the expectation is unfulfilled.

[attributes.diagnostics.lint.warn]

  * `#[warn(C)]` warns about violations of `C` but continues compilation.

[attributes.diagnostics.lint.deny]

  * `#[deny(C)]` signals an error after encountering a violation of `C`,

[attributes.diagnostics.lint.forbid]

  * `#[forbid(C)]` is the same as `deny(C)`, but also forbids changing the lint level afterwards,

> Note
>
> The lint checks supported by `rustc` can be found via `rustc -W help`, along
> with their default settings and are documented in the [rustc
> book](../rustc/lints/index.html).
    
    
    #![allow(unused)]
    fn main() {
    pub mod m1 {
        // Missing documentation is ignored here
        #[allow(missing_docs)]
        pub fn undocumented_one() -> i32 { 1 }
    
        // Missing documentation signals a warning here
        #[warn(missing_docs)]
        pub fn undocumented_too() -> i32 { 2 }
    
        // Missing documentation signals an error here
        #[deny(missing_docs)]
        pub fn undocumented_end() -> i32 { 3 }
    }
    }

[attributes.diagnostics.lint.override]

Lint attributes can override the level specified from a previous attribute, as
long as the level does not attempt to change a forbidden lint (except for
`deny`, which is allowed inside a `forbid` context, but ignored). Previous
attributes are those from a higher level in the syntax tree, or from a
previous attribute on the same entity as listed in left-to-right source order.

This example shows how one can use `allow` and `warn` to toggle a particular
check on and off:

    
    
    #![allow(unused)]
    fn main() {
    #[warn(missing_docs)]
    pub mod m2 {
        #[allow(missing_docs)]
        pub mod nested {
            // Missing documentation is ignored here
            pub fn undocumented_one() -> i32 { 1 }
    
            // Missing documentation signals a warning here,
            // despite the allow above.
            #[warn(missing_docs)]
            pub fn undocumented_two() -> i32 { 2 }
        }
    
        // Missing documentation signals a warning here
        pub fn undocumented_too() -> i32 { 3 }
    }
    }

This example shows how one can use `forbid` to disallow uses of `allow` or
`expect` for that lint check:

    
    
    #![allow(unused)]
    fn main() {
    #[forbid(missing_docs)]
    pub mod m3 {
        // Attempting to toggle warning signals an error here
        #[allow(missing_docs)]
        /// Returns 2.
        pub fn undocumented_too() -> i32 { 2 }
    }
    }

> Note
>
> `rustc` allows setting lint levels on the [command-
> line](../rustc/lints/levels.html#via-compiler-flag), and also supports
> [setting caps](../rustc/lints/levels.html#capping-lints) on the lints that
> are reported.

[attributes.diagnostics.lint.reason]

### Lint reasons

All lint attributes support an additional `reason` parameter, to give context
why a certain attribute was added. This reason will be displayed as part of
the lint message if the lint is emitted at the defined level.

    
    
    #![allow(unused)]
    fn main() {
    // `keyword_idents` is allowed by default. Here we deny it to
    // avoid migration of identifiers when we update the edition.
    #![deny(
        keyword_idents,
        reason = "we want to avoid these idents to be future compatible"
    )]
    
    // This name was allowed in Rust's 2015 edition. We still aim to avoid
    // this to be future compatible and not confuse end users.
    fn dyn() {}
    }

Here is another example, where the lint is allowed with a reason:

    
    
    #![allow(unused)]
    fn main() {
    use std::path::PathBuf;
    
    pub fn get_path() -> PathBuf {
        // The `reason` parameter on `allow` attributes acts as documentation for the reader.
        #[allow(unused_mut, reason = "this is only modified on some platforms")]
        let mut file_name = PathBuf::from("git");
    
        #[cfg(target_os = "windows")]
        file_name.set_extension("exe");
    
        file_name
    }
    }

[attributes.diagnostics.expect]

### The `#[expect]` attribute

[attributes.diagnostics.expect.intro]

The `#[expect(C)]` attribute creates a lint expectation for lint `C`. The
expectation will be fulfilled, if a `#[warn(C)]` attribute at the same
location would result in a lint emission. If the expectation is unfulfilled,
because lint `C` would not be emitted, the `unfulfilled_lint_expectations`
lint will be emitted at the attribute.

    
    
    fn main() {
        // This `#[expect]` attribute creates a lint expectation, that the `unused_variables`
        // lint would be emitted by the following statement. This expectation is
        // unfulfilled, since the `question` variable is used by the `println!` macro.
        // Therefore, the `unfulfilled_lint_expectations` lint will be emitted at the
        // attribute.
        #[expect(unused_variables)]
        let question = "who lives in a pineapple under the sea?";
        println!("{question}");
    
        // This `#[expect]` attribute creates a lint expectation that will be fulfilled, since
        // the `answer` variable is never used. The `unused_variables` lint, that would usually
        // be emitted, is suppressed. No warning will be issued for the statement or attribute.
        #[expect(unused_variables)]
        let answer = "SpongeBob SquarePants!";
    }

[attributes.diagnostics.expect.fulfillment]

The lint expectation is only fulfilled by lint emissions which have been
suppressed by the `expect` attribute. If the lint level is modified in the
scope with other level attributes like `allow` or `warn`, the lint emission
will be handled accordingly and the expectation will remain unfulfilled.

    
    
    #![allow(unused)]
    fn main() {
    #[expect(unused_variables)]
    fn select_song() {
        // This will emit the `unused_variables` lint at the warn level
        // as defined by the `warn` attribute. This will not fulfill the
        // expectation above the function.
        #[warn(unused_variables)]
        let song_name = "Crab Rave";
    
        // The `allow` attribute suppresses the lint emission. This will not
        // fulfill the expectation as it has been suppressed by the `allow`
        // attribute and not the `expect` attribute above the function.
        #[allow(unused_variables)]
        let song_creator = "Noisestorm";
    
        // This `expect` attribute will suppress the `unused_variables` lint emission
        // at the variable. The `expect` attribute above the function will still not
        // be fulfilled, since this lint emission has been suppressed by the local
        // expect attribute.
        #[expect(unused_variables)]
        let song_version = "Monstercat Release";
    }
    }

[attributes.diagnostics.expect.independent]

If the `expect` attribute contains several lints, each one is expected
separately. For a lint group it’s enough if one lint inside the group has been
emitted:

    
    
    #![allow(unused)]
    fn main() {
    // This expectation will be fulfilled by the unused value inside the function
    // since the emitted `unused_variables` lint is inside the `unused` lint group.
    #[expect(unused)]
    pub fn thoughts() {
        let unused = "I'm running out of examples";
    }
    
    pub fn another_example() {
        // This attribute creates two lint expectations. The `unused_mut` lint will be
        // suppressed and with that fulfill the first expectation. The `unused_variables`
        // wouldn't be emitted, since the variable is used. That expectation will therefore
        // be unsatisfied, and a warning will be emitted.
        #[expect(unused_mut, unused_variables)]
        let mut link = "https://www.rust-lang.org/";
    
        println!("Welcome to our community: {link}");
    }
    }

> Note
>
> The behavior of `#[expect(unfulfilled_lint_expectations)]` is currently
> defined to always generate the `unfulfilled_lint_expectations` lint.

[attributes.diagnostics.lint.group]

### Lint groups

Lints may be organized into named groups so that the level of related lints
can be adjusted together. Using a named group is equivalent to listing out the
lints within that group.

    
    
    #![allow(unused)]
    fn main() {
    // This allows all lints in the "unused" group.
    #[allow(unused)]
    // This overrides the "unused_must_use" lint from the "unused"
    // group to deny.
    #[deny(unused_must_use)]
    fn example() {
        // This does not generate a warning because the "unused_variables"
        // lint is in the "unused" group.
        let x = 1;
        // This generates an error because the result is unused and
        // "unused_must_use" is marked as "deny".
        std::fs::remove_file("some_file"); // ERROR: unused `Result` that must be used
    }
    }

[attributes.diagnostics.lint.group.warnings]

There is a special group named “warnings” which includes all lints at the
“warn” level. The “warnings” group ignores attribute order and applies to all
lints that would otherwise warn within the entity.

    
    
    #![allow(unused)]
    fn main() {
    unsafe fn an_unsafe_fn() {}
    // The order of these two attributes does not matter.
    #[deny(warnings)]
    // The unsafe_code lint is normally "allow" by default.
    #[warn(unsafe_code)]
    fn example_err() {
        // This is an error because the `unsafe_code` warning has
        // been lifted to "deny".
        unsafe { an_unsafe_fn() } // ERROR: usage of `unsafe` block
    }
    }

[attributes.diagnostics.lint.tool]

### Tool lint attributes

[attributes.diagnostics.lint.tool.intro]

Tool lints allows using scoped lints, to `allow`, `warn`, `deny` or `forbid`
lints of certain tools.

[attributes.diagnostics.lint.tool.activation]

Tool lints only get checked when the associated tool is active. If a lint
attribute, such as `allow`, references a nonexistent tool lint, the compiler
will not warn about the nonexistent lint until you use the tool.

Otherwise, they work just like regular lint attributes:

    
    
    // set the entire `pedantic` clippy lint group to warn
    #![warn(clippy::pedantic)]
    // silence warnings from the `filter_map` clippy lint
    #![allow(clippy::filter_map)]
    
    fn main() {
        // ...
    }
    
    // silence the `cmp_nan` clippy lint just for this function
    #[allow(clippy::cmp_nan)]
    fn foo() {
        // ...
    }

> Note
>
> `rustc` currently recognizes the tool lints for
> “[clippy](https://github.com/rust-lang/rust-clippy)” and
> “[rustdoc](../rustdoc/lints.html)”.

[attributes.diagnostics.deprecated]

## The `deprecated` attribute

[attributes.diagnostics.deprecated.intro]

The _`deprecated` attribute_ marks an item as deprecated. `rustc` will issue
warnings on usage of `#[deprecated]` items. `rustdoc` will show item
deprecation, including the `since` version and `note`, if available.

[attributes.diagnostics.deprecated.syntax]

The `deprecated` attribute has several forms:

  * `deprecated` — Issues a generic message.
  * `deprecated = "message"` — Includes the given string in the deprecation message.
  * MetaListNameValueStr syntax with two optional fields: 
    * `since` — Specifies a version number when the item was deprecated. `rustc` does not currently interpret the string, but external tools like [Clippy](https://github.com/rust-lang/rust-clippy) may check the validity of the value.
    * `note` — Specifies a string that should be included in the deprecation message. This is typically used to provide an explanation about the deprecation and preferred alternatives.

[attributes.diagnostic.deprecated.allowed-positions]

The `deprecated` attribute may be applied to any item, trait item, enum
variant, struct field, external block item, or macro definition. It cannot be
applied to trait implementation items. When applied to an item containing
other items, such as a module or implementation, all child items inherit the
deprecation attribute.

Here is an example:

    
    
    #![allow(unused)]
    fn main() {
    #[deprecated(since = "5.2.0", note = "foo was rarely used. Users should instead use bar")]
    pub fn foo() {}
    
    pub fn bar() {}
    }

The [RFC](https://github.com/rust-
lang/rfcs/blob/master/text/1270-deprecation.md) contains motivations and more
details.

[attributes.diagnostics.must_use]

## The `must_use` attribute

[attributes.diagnostics.must_use.intro]

The _`must_use` attribute_ is used to issue a diagnostic warning when a value
is not “used”.

[attributes.diagnostics.must_use.allowed-positions]

The `must_use` attribute can be applied to user-defined composite types
(`struct`s, `enum`s, and `union`s), functions, and traits.

[attributes.diagnostics.must_use.message]

The `must_use` attribute may include a message by using the MetaNameValueStr
syntax such as `#[must_use = "example message"]`. The message will be given
alongside the warning.

[attributes.diagnostics.must_use.type]

When used on user-defined composite types, if the expression of an expression
statement has that type, then the `unused_must_use` lint is violated.

    
    
    #![allow(unused)]
    fn main() {
    #[must_use]
    struct MustUse {
        // some fields
    }
    
    impl MustUse {
      fn new() -> MustUse { MustUse {} }
    }
    
    // Violates the `unused_must_use` lint.
    MustUse::new();
    }

[attributes.diagnostics.must_use.fn]

When used on a function, if the expression of an expression statement is a
call expression to that function, then the `unused_must_use` lint is violated.

    
    
    #![allow(unused)]
    fn main() {
    #[must_use]
    fn five() -> i32 { 5i32 }
    
    // Violates the unused_must_use lint.
    five();
    }

[attributes.diagnostics.must_use.trait]

When used on a trait declaration, a call expression of an expression statement
to a function that returns an impl trait or a dyn trait of that trait violates
the `unused_must_use` lint.

    
    
    #![allow(unused)]
    fn main() {
    #[must_use]
    trait Critical {}
    impl Critical for i32 {}
    
    fn get_critical() -> impl Critical {
        4i32
    }
    
    // Violates the `unused_must_use` lint.
    get_critical();
    }

[attributes.diagnostics.must_use.trait-function]

When used on a function in a trait declaration, then the behavior also applies
when the call expression is a function from an implementation of the trait.

    
    
    #![allow(unused)]
    fn main() {
    trait Trait {
        #[must_use]
        fn use_me(&self) -> i32;
    }
    
    impl Trait for i32 {
        fn use_me(&self) -> i32 { 0i32 }
    }
    
    // Violates the `unused_must_use` lint.
    5i32.use_me();
    }

[attributes.diagnostics.must_use.trait-impl-function]

When used on a function in a trait implementation, the attribute does nothing.

> Note
>
> Trivial no-op expressions containing the value will not violate the lint.
> Examples include wrapping the value in a type that does not implement `Drop`
> and then not using that type and being the final expression of a block
> expression that is not used.
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[must_use]
>     fn five() -> i32 { 5i32 }
>  
>     // None of these violate the unused_must_use lint.
>     (five(),);
>     Some(five());
>     { five() };
>     if true { five() } else { 0i32 };
>     match true {
>         _ => five()
>     };
>     }

> Note
>
> It is idiomatic to use a let statement with a pattern of `_` when a must-
> used value is purposely discarded.
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[must_use]
>     fn five() -> i32 { 5i32 }
>  
>     // Does not violate the unused_must_use lint.
>     let _ = five();
>     }

[attributes.diagnostic.namespace]

## The `diagnostic` tool attribute namespace

[attributes.diagnostic.namespace.intro]

The `#[diagnostic]` attribute namespace is a home for attributes to influence
compile-time error messages. The hints provided by these attributes are not
guaranteed to be used.

[attributes.diagnostic.namespace.unknown-invalid-syntax]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/deny_malformed_attribute.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/deny_malformed_attribute.rs)
  * [tests/ui/diagnostic_namespace/non_existing_attributes_accepted.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/non_existing_attributes_accepted.rs)
  * [tests/ui/diagnostic_namespace/suggest_typos.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/suggest_typos.rs)

Unknown attributes in this namespace are accepted, though they may emit
warnings for unused attributes. Additionally, invalid inputs to known
attributes will typically be a warning (see the attribute definitions for
details). This is meant to allow adding or discarding attributes and changing
inputs in the future to allow changes without the need to keep the non-
meaningful attributes or options working.

[attributes.diagnostic.on_unimplemented]

### The `diagnostic::on_unimplemented` attribute

[attributes.diagnostic.on_unimplemented.intro]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/on_unimplemented/custom-on-unimplemented-diagnostic.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/custom-on-unimplemented-diagnostic.rs)
  * [tests/ui/diagnostic_namespace/on_unimplemented/error_is_shown_in_downstream_crates.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/error_is_shown_in_downstream_crates.rs)
  * [tests/ui/diagnostic_namespace/on_unimplemented/on_unimplemented_simple.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/on_unimplemented_simple.rs)
  * [tests/ui/traits/negative-bounds/on-unimplemented.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/traits/negative-bounds/on-unimplemented.rs)

The `#[diagnostic::on_unimplemented]` attribute is a hint to the compiler to
supplement the error message that would normally be generated in scenarios
where a trait is required but not implemented on a type.

[attributes.diagnostic.on_unimplemented.allowed-positions]

The attribute should be placed on a trait declaration, though it is not an
error to be located in other positions.

[attributes.diagnostic.on_unimplemented.syntax]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/malformed_foreign_on_unimplemented.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/malformed_foreign_on_unimplemented.rs)
  * [tests/ui/diagnostic_namespace/on_unimplemented/do_not_accept_options_of_the_internal_rustc_attribute.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/do_not_accept_options_of_the_internal_rustc_attribute.rs)
  * [tests/ui/diagnostic_namespace/on_unimplemented/do_not_fail_parsing_on_invalid_options_1.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/do_not_fail_parsing_on_invalid_options_1.rs)
  * [tests/ui/diagnostic_namespace/on_unimplemented/ignore_unsupported_options_and_continue_to_use_fallback.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/ignore_unsupported_options_and_continue_to_use_fallback.rs)

The attribute uses the MetaListNameValueStr syntax to specify its inputs,
though any malformed input to the attribute is not considered as an error to
provide both forwards and backwards compatibility.

[attributes.diagnostic.on_unimplemented.keys]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/on_unimplemented/custom-on-unimplemented-diagnostic.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/custom-on-unimplemented-diagnostic.rs)
  * [tests/ui/diagnostic_namespace/on_unimplemented/do_not_accept_options_of_the_internal_rustc_attribute.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/do_not_accept_options_of_the_internal_rustc_attribute.rs)
  * [tests/ui/diagnostic_namespace/on_unimplemented/on_unimplemented_simple.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/on_unimplemented_simple.rs)

The following keys have the given meaning:

  * `message` — The text for the top level error message.
  * `label` — The text for the label shown inline in the broken code in the error message.
  * `note` — Provides additional notes.

[attributes.diagnostic.on_unimplemented.note-repetition]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/on_unimplemented/multiple_notes.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/multiple_notes.rs)

The `note` option can appear several times, which results in several note
messages being emitted.

[attributes.diagnostic.on_unimplemented.repetition]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/on_unimplemented/ignore_unsupported_options_and_continue_to_use_fallback.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/ignore_unsupported_options_and_continue_to_use_fallback.rs)
  * [tests/ui/diagnostic_namespace/on_unimplemented/report_warning_on_duplicated_options.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/report_warning_on_duplicated_options.rs)

If any of the other options appears several times the first occurrence of the
relevant option specifies the actually used value. Subsequent occurrences
generates a warning.

[attributes.diagnostic.on_unimplemented.unknown-keys]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/on_unimplemented/do_not_fail_parsing_on_invalid_options_1.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/do_not_fail_parsing_on_invalid_options_1.rs)

A warning is generated for any unknown keys.

[attributes.diagnostic.on_unimplemented.format-string]

All three options accept a string as an argument, interpreted using the same
formatting as a [`std::fmt`](../alloc/fmt/index.html) string.

[attributes.diagnostic.on_unimplemented.format-parameters]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/on_unimplemented/do_not_accept_options_of_the_internal_rustc_attribute.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/do_not_accept_options_of_the_internal_rustc_attribute.rs)

Format parameters with the given named parameter will be replaced with the
following text:

  * `{Self}` — The name of the type implementing the trait.
  * `{` _GenericParameterName_ `}` — The name of the generic argument’s type for the given generic parameter.

[attributes.diagnostic.on_unimplemented.invalid-formats]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/on_unimplemented/do_not_accept_options_of_the_internal_rustc_attribute.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/do_not_accept_options_of_the_internal_rustc_attribute.rs)

Any other format parameter will generate a warning, but will otherwise be
included in the string as-is.

[attributes.diagnostic.on_unimplemented.invalid-string]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/on_unimplemented/broken_format.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/on_unimplemented/broken_format.rs)

Invalid format strings may generate a warning, but are otherwise allowed, but
may not display as intended. Format specifiers may generate a warning, but are
otherwise ignored.

In this example:

    
    
    #[diagnostic::on_unimplemented(
        message = "My Message for `ImportantTrait<{A}>` implemented for `{Self}`",
        label = "My Label",
        note = "Note 1",
        note = "Note 2"
    )]
    trait ImportantTrait<A> {}
    
    fn use_my_trait(_: impl ImportantTrait<i32>) {}
    
    fn main() {
        use_my_trait(String::new());
    }

the compiler may generate an error message which looks like this:

    
    
    error[E0277]: My Message for `ImportantTrait<i32>` implemented for `String`
      --> src/main.rs:14:18
       |
    14 |     use_my_trait(String::new());
       |     ------------ ^^^^^^^^^^^^^ My Label
       |     |
       |     required by a bound introduced by this call
       |
       = help: the trait `ImportantTrait<i32>` is not implemented for `String`
       = note: Note 1
       = note: Note 2
    

[attributes.diagnostic.do_not_recommend]

### The `diagnostic::do_not_recommend` attribute

[attributes.diagnostic.do_not_recommend.intro]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/do_not_recommend/as_expression.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/do_not_recommend/as_expression.rs)
  * [tests/ui/diagnostic_namespace/do_not_recommend/nested.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/do_not_recommend/nested.rs)
  * [tests/ui/diagnostic_namespace/do_not_recommend/simple.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/do_not_recommend/simple.rs)
  * [tests/ui/diagnostic_namespace/do_not_recommend/stacked.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/do_not_recommend/stacked.rs)
  * [tests/ui/diagnostic_namespace/do_not_recommend/supress_suggestions_in_help.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/do_not_recommend/supress_suggestions_in_help.rs)
  * [tests/ui/diagnostic_namespace/do_not_recommend/type_mismatch.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/do_not_recommend/type_mismatch.rs)
  * [tests/ui/diagnostic_namespace/do_not_recommend/with_lifetime.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/do_not_recommend/with_lifetime.rs)

The `#[diagnostic::do_not_recommend]` attribute is a hint to the compiler to
not show the annotated trait implementation as part of a diagnostic message.

> Note
>
> Suppressing the recommendation can be useful if you know that the
> recommendation would normally not be useful to the programmer. This often
> occurs with broad, blanket impls. The recommendation may send the programmer
> down the wrong path, or the trait implementation may be an internal detail
> that you don’t want to expose, or the bounds may not be able to be satisfied
> by the programmer.
>
> For example, in an error message about a type not implementing a required
> trait, the compiler may find a trait implementation that would satisfy the
> requirements if it weren’t for specific bounds in the trait implementation.
> The compiler may tell the user that there is an impl, but the problem is the
> bounds in the trait implementation. The `#[diagnostic::do_not_recommend]`
> attribute can be used to tell the compiler to _not_ tell the user about the
> trait implementation, and instead simply tell the user the type doesn’t
> implement the required trait.

[attributes.diagnostic.do_not_recommend.allowed-positions]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/do_not_recommend/incorrect-locations.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/do_not_recommend/incorrect-locations.rs)

The attribute should be placed on a trait implementation item, though it is
not an error to be located in other positions.

[attributes.diagnostic.do_not_recommend.syntax]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/ui/diagnostic_namespace/do_not_recommend/does_not_acccept_args.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/ui/diagnostic_namespace/do_not_recommend/does_not_acccept_args.rs)

The attribute does not accept any arguments, though unexpected arguments are
not considered as an error.

In the following example, there is a trait called `AsExpression` which is used
for casting arbitrary types to the `Expression` type used in an SQL library.
There is a method called `check` which takes an `AsExpression`.

    
    
    pub trait Expression {
        type SqlType;
    }
    
    pub trait AsExpression<ST> {
        type Expression: Expression<SqlType = ST>;
    }
    
    pub struct Text;
    pub struct Integer;
    
    pub struct Bound<T>(T);
    pub struct SelectInt;
    
    impl Expression for SelectInt {
        type SqlType = Integer;
    }
    
    impl<T> Expression for Bound<T> {
        type SqlType = T;
    }
    
    impl AsExpression<Integer> for i32 {
        type Expression = Bound<Integer>;
    }
    
    impl AsExpression<Text> for &'_ str {
        type Expression = Bound<Text>;
    }
    
    impl<T> Foo for T where T: Expression {}
    
    // Uncomment this line to change the recommendation.
    // #[diagnostic::do_not_recommend]
    impl<T, ST> AsExpression<ST> for T
    where
        T: Expression<SqlType = ST>,
    {
        type Expression = T;
    }
    
    trait Foo: Expression + Sized {
        fn check<T>(&self, _: T) -> <T as AsExpression<<Self as Expression>::SqlType>>::Expression
        where
            T: AsExpression<Self::SqlType>,
        {
            todo!()
        }
    }
    
    fn main() {
        SelectInt.check("bar");
    }

The `SelectInt` type’s `check` method is expecting an `Integer` type. Calling
it with an i32 type works, as it gets converted to an `Integer` by the
`AsExpression` trait. However, calling it with a string does not, and
generates a an error that may look like this:

    
    
    error[E0277]: the trait bound `&str: Expression` is not satisfied
      --> src/main.rs:53:15
       |
    53 |     SelectInt.check("bar");
       |               ^^^^^ the trait `Expression` is not implemented for `&str`
       |
       = help: the following other types implement trait `Expression`:
                 Bound<T>
                 SelectInt
    note: required for `&str` to implement `AsExpression<Integer>`
      --> src/main.rs:45:13
       |
    45 | impl<T, ST> AsExpression<ST> for T
       |             ^^^^^^^^^^^^^^^^     ^
    46 | where
    47 |     T: Expression<SqlType = ST>,
       |        ------------------------ unsatisfied trait bound introduced here
    

By adding the `#[diagnostic::do_not_recommend]` attribute to the blanket
`impl` for `AsExpression`, the message changes to:

    
    
    error[E0277]: the trait bound `&str: AsExpression<Integer>` is not satisfied
      --> src/main.rs:53:15
       |
    53 |     SelectInt.check("bar");
       |               ^^^^^ the trait `AsExpression<Integer>` is not implemented for `&str`
       |
       = help: the trait `AsExpression<Integer>` is not implemented for `&str`
               but trait `AsExpression<Text>` is implemented for it
       = help: for that trait implementation, expected `Text`, found `Integer`
    

The first error message includes a somewhat confusing error message about the
relationship of `&str` and `Expression`, as well as the unsatisfied trait
bound in the blanket impl. After adding `#[diagnostic::do_not_recommend]`, it
no longer considers the blanket impl for the recommendation. The message
should be a little clearer, with an indication that a string cannot be
converted to an `Integer`.

[attributes.codegen]

# Code generation attributes

The following attributes are used for controlling code generation.

[attributes.codegen.inline]

### The `inline` attribute

[attributes.codegen.inline.intro]

The _`inline` attribute_ suggests whether a copy of the attributed function’s
code should be placed in the caller rather than generating a call to the
function.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[inline]
>     pub fn example1() {}
>  
>     #[inline(always)]
>     pub fn example2() {}
>  
>     #[inline(never)]
>     pub fn example3() {}
>     }

> Note
>
> `rustc` automatically inlines functions when doing so seems worthwhile. Use
> this attribute carefully as poor decisions about what to inline can slow
> down programs.

[attributes.codegen.inline.syntax]

The syntax for the `inline` attribute is:

**Syntax**  
InlineAttribute →  
inline ( always )  
| inline ( never )  
| inline

Show Railroad

InlineAttribute inline ( always ) inline ( never ) inline

[attributes.codegen.inline.allowed-positions]

The `inline` attribute may only be applied to functions with bodies —
closures, async blocks, free functions, associated functions in an inherent
impl or trait impl, and associated functions in a trait definition when those
functions have a default definition .

> Note
>
> `rustc` ignores use in other positions but lints against it. This may become
> an error in the future.

> Note
>
> Though the attribute can be applied to closures and async blocks, the
> usefulness of this is limited as we do not yet support attributes on
> expressions.
>  
>  
>     #![allow(unused)]
>     fn main() {
>     // We allow attributes on statements.
>     #[inline] || (); // OK
>     #[inline] async {}; // OK
>     }
>  
>  
>     #![allow(unused)]
>     fn main() {
>     // We don't yet allow attributes on expressions.
>     let f = #[inline] || (); // ERROR
>     }

[attributes.codegen.inline.duplicates]

Only the first use of `inline` on a function has effect.

> Note
>
> `rustc` lints against any use following the first. This may become an error
> in the future.

[attributes.codegen.inline.modes]

The `inline` attribute supports these modes:

  * `#[inline]` _suggests_ performing inline expansion.
  * `#[inline(always)]` _suggests_ that inline expansion should always be performed.
  * `#[inline(never)]` _suggests_ that inline expansion should never be performed.

> Note
>
> In every form the attribute is a hint. The compiler may ignore it.

[attributes.codegen.inline.trait]

When `inline` is applied to a function in a trait, it applies only to the code
of the default definition.

[attributes.codegen.inline.async]

When `inline` is applied to an async function or async closure, it applies
only to the code of the generated `poll` function.

> Note
>
> For more details, see [Rust issue #129347](https://github.com/rust-
> lang/rust/issues/129347).

[attributes.codegen.inline.externally-exported]

The `inline` attribute is ignored if the function is externally exported with
`no_mangle` or `export_name`.

[attributes.codegen.cold]

### The `cold` attribute

[attributes.codegen.cold.intro]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/codegen-llvm/cold-attribute.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/codegen-llvm/cold-attribute.rs)

The _`cold` attribute_ suggests that the attributed function is unlikely to be
called which may help the compiler produce better code.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[cold]
>     pub fn example() {}
>     }

[attributes.codegen.cold.syntax]

The `cold` attribute uses the MetaWord syntax.

[attributes.codegen.cold.allowed-positions]

The `cold` attribute may only be applied to functions with bodies — closures,
async blocks, free functions, associated functions in an inherent impl or
trait impl, and associated functions in a trait definition when those
functions have a default definition .

> Note
>
> `rustc` ignores use in other positions but lints against it. This may become
> an error in the future.

> Note
>
> Though the attribute can be applied to closures and async blocks, the
> usefulness of this is limited as we do not yet support attributes on
> expressions.

[attributes.codegen.cold.duplicates]

Only the first use of `cold` on a function has effect.

> Note
>
> `rustc` lints against any use following the first. This may become an error
> in the future.

[attributes.codegen.cold.trait]  

[Tests](javascript:void\(0\))

Tests with this rule:

  * [tests/codegen-llvm/cold-attribute.rs](https://github.com/rust-lang/rust/blob/1.94.1/tests/codegen-llvm/cold-attribute.rs)

When `cold` is applied to a function in a trait, it applies only to the code
of the default definition.

[attributes.codegen.naked]

## The `naked` attribute

[attributes.codegen.naked.intro]

The _`naked` attribute_ prevents the compiler from emitting a function
prologue and epilogue for the attributed function.

[attributes.codegen.naked.body]

The function body must consist of exactly one `naked_asm!` macro invocation.

[attributes.codegen.naked.prologue-epilogue]

No function prologue or epilogue is generated for the attributed function. The
assembly code in the `naked_asm!` block constitutes the full body of a naked
function.

[attributes.codegen.naked.unsafe-attribute]

The `naked` attribute is an unsafe attribute. Annotating a function with
`#[unsafe(naked)]` comes with the safety obligation that the body must respect
the function’s calling convention, uphold its signature, and either return or
diverge (i.e., not fall through past the end of the assembly code).

[attributes.codegen.naked.call-stack]

The assembly code may assume that the call stack and register state are valid
on entry as per the signature and calling convention of the function.

[attributes.codegen.naked.no-duplication]

The assembly code may not be duplicated by the compiler except when
monomorphizing polymorphic functions.

> Note
>
> Guaranteeing when the assembly code may or may not be duplicated is
> important for naked functions that define symbols.

[attributes.codegen.naked.unused-variables]

The [`unused_variables`](../rustc/lints/listing/warn-by-default.html#unused-
variables) lint is suppressed within naked functions.

[attributes.codegen.naked.inline]

The `inline` attribute cannot by applied to a naked function.

[attributes.codegen.naked.track_caller]

The `track_caller` attribute cannot be applied to a naked function.

[attributes.codegen.naked.testing]

The testing attributes cannot be applied to a naked function.

[attributes.codegen.no_builtins]

## The `no_builtins` attribute

[attributes.codegen.no_builtins.intro]

The _`no_builtins` attribute_ disables optimization of certain code patterns
related to calls to library functions that are assumed to exist.

> Example
>  
>  
>     #![allow(unused)]
>     #![no_builtins]
>     fn main() {
>     }

[attributes.codegen.no_builtins.syntax]

The `no_builtins` attribute uses the MetaWord syntax.

[attributes.codegen.no_builtins.allowed-positions]

The `no_builtins` attribute can only be applied to the crate root.

[attributes.codegen.no_builtins.duplicates]

Only the first use of the `no_builtins` attribute has effect.

> Note
>
> `rustc` lints against any use following the first.

[attributes.codegen.target_feature]

## The `target_feature` attribute

[attributes.codegen.target_feature.intro]

The _`target_feature` attribute_ may be applied to a function to enable code
generation of that function for specific platform architecture features. It
uses the MetaListNameValueStr syntax with a single key of `enable` whose value
is a string of comma-separated feature names to enable.

    
    
    #![allow(unused)]
    fn main() {
    #[cfg(target_feature = "avx2")]
    #[target_feature(enable = "avx2")]
    fn foo_avx2() {}
    }

[attributes.codegen.target_feature.arch]

Each target architecture has a set of features that may be enabled. It is an
error to specify a feature for a target architecture that the crate is not
being compiled for.

[attributes.codegen.target_feature.closures]

Closures defined within a `target_feature`-annotated function inherit the
attribute from the enclosing function.

[attributes.codegen.target_feature.target-ub]

It is undefined behavior to call a function that is compiled with a feature
that is not supported on the current platform the code is running on, _except_
if the platform explicitly documents this to be safe.

[attributes.codegen.target_feature.safety-restrictions]

The following restrictions apply unless otherwise specified by the platform
rules below:

  * Safe `#[target_feature]` functions (and closures that inherit the attribute) can only be safely called within a caller that enables all the `target_feature`s that the callee enables. This restriction does not apply in an `unsafe` context.
  * Safe `#[target_feature]` functions (and closures that inherit the attribute) can only be coerced to _safe_ function pointers in contexts that enable all the `target_feature`s that the coercee enables. This restriction does not apply to `unsafe` function pointers.

Implicitly enabled features are included in this rule. For example an `sse2`
function can call ones marked with `sse`.

    
    
    #![allow(unused)]
    fn main() {
    #[cfg(target_feature = "sse2")] {
    #[target_feature(enable = "sse")]
    fn foo_sse() {}
    
    fn bar() {
        // Calling `foo_sse` here is unsafe, as we must ensure that SSE is
        // available first, even if `sse` is enabled by default on the target
        // platform or manually enabled as compiler flags.
        unsafe {
            foo_sse();
        }
    }
    
    #[target_feature(enable = "sse")]
    fn bar_sse() {
        // Calling `foo_sse` here is safe.
        foo_sse();
        || foo_sse();
    }
    
    #[target_feature(enable = "sse2")]
    fn bar_sse2() {
        // Calling `foo_sse` here is safe because `sse2` implies `sse`.
        foo_sse();
    }
    }
    }

[attributes.codegen.target_feature.fn-traits]

A function with a `#[target_feature]` attribute _never_ implements the `Fn`
family of traits, although closures inheriting features from the enclosing
function do.

[attributes.codegen.target_feature.allowed-positions]

The `#[target_feature]` attribute is not allowed on the following places:

  * the `main` function
  * a `panic_handler` function
  * safe trait methods
  * safe default functions in traits

[attributes.codegen.target_feature.inline]

Functions marked with `target_feature` are not inlined into a context that
does not support the given features. The `#[inline(always)]` attribute may not
be used with a `target_feature` attribute.

[attributes.codegen.target_feature.availability]

### Available features

The following is a list of the available feature names.

[attributes.codegen.target_feature.x86]

#### `x86` or `x86_64`

Executing code with unsupported features is undefined behavior on this
platform. Hence on this platform usage of `#[target_feature]` functions
follows the above restrictions.

Feature| Implicitly Enables| Description  
---|---|---  
`adx`| | [ADX](https://en.wikipedia.org/wiki/Intel_ADX) — Multi-Precision Add-Carry Instruction Extensions  
`aes`| `sse2`| [AES](https://en.wikipedia.org/wiki/AES_instruction_set) —
Advanced Encryption Standard  
`avx`| `sse4.2`|
[AVX](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) — Advanced
Vector Extensions  
`avx2`| `avx`|
[AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX2) —
Advanced Vector Extensions 2  
`avx512bf16`| `avx512bw`|
[AVX512-BF16](https://en.wikipedia.org/wiki/AVX-512#BF16) — Advanced Vector
Extensions 512-bit - Bfloat16 Extensions  
`avx512bitalg`| `avx512bw`|
[AVX512-BITALG](https://en.wikipedia.org/wiki/AVX-512#VPOPCNTDQ_and_BITALG) —
Advanced Vector Extensions 512-bit - Bit Algorithms  
`avx512bw`| `avx512f`|
[AVX512-BW](https://en.wikipedia.org/wiki/AVX-512#BW,_DQ_and_VBMI) — Advanced
Vector Extensions 512-bit - Byte and Word Instructions  
`avx512cd`| `avx512f`|
[AVX512-CD](https://en.wikipedia.org/wiki/AVX-512#Conflict_detection) —
Advanced Vector Extensions 512-bit - Conflict Detection Instructions  
`avx512dq`| `avx512f`|
[AVX512-DQ](https://en.wikipedia.org/wiki/AVX-512#BW,_DQ_and_VBMI) — Advanced
Vector Extensions 512-bit - Doubleword and Quadword Instructions  
`avx512f`| `avx2`, `fma`, `f16c`|
[AVX512-F](https://en.wikipedia.org/wiki/AVX-512) — Advanced Vector Extensions
512-bit - Foundation  
`avx512fp16`| `avx512bw`|
[AVX512-FP16](https://en.wikipedia.org/wiki/AVX-512#FP16) — Advanced Vector
Extensions 512-bit - Float16 Extensions  
`avx512ifma`| `avx512f`|
[AVX512-IFMA](https://en.wikipedia.org/wiki/AVX-512#IFMA) — Advanced Vector
Extensions 512-bit - Integer Fused Multiply Add  
`avx512vbmi`| `avx512bw`|
[AVX512-VBMI](https://en.wikipedia.org/wiki/AVX-512#BW,_DQ_and_VBMI) —
Advanced Vector Extensions 512-bit - Vector Byte Manipulation Instructions  
`avx512vbmi2`| `avx512bw`|
[AVX512-VBMI2](https://en.wikipedia.org/wiki/AVX-512#VBMI2) — Advanced Vector
Extensions 512-bit - Vector Byte Manipulation Instructions 2  
`avx512vl`| `avx512f`| [AVX512-VL](https://en.wikipedia.org/wiki/AVX-512) —
Advanced Vector Extensions 512-bit - Vector Length Extensions  
`avx512vnni`| `avx512f`|
[AVX512-VNNI](https://en.wikipedia.org/wiki/AVX-512#VNNI) — Advanced Vector
Extensions 512-bit - Vector Neural Network Instructions  
`avx512vp2intersect`| `avx512f`|
[AVX512-VP2INTERSECT](https://en.wikipedia.org/wiki/AVX-512#VP2INTERSECT) —
Advanced Vector Extensions 512-bit - Vector Pair Intersection to a Pair of
Mask Registers  
`avx512vpopcntdq`| `avx512f`|
[AVX512-VPOPCNTDQ](https://en.wikipedia.org/wiki/AVX-512#VPOPCNTDQ_and_BITALG)
— Advanced Vector Extensions 512-bit - Vector Population Count Instruction  
`avxifma`| `avx2`| [AVX-
IFMA](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-
IFMA) — Advanced Vector Extensions - Integer Fused Multiply Add  
`avxneconvert`| `avx2`| [AVX-NE-
CONVERT](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-
VNNI,_AVX-IFMA) — Advanced Vector Extensions - No-Exception Floating-Point
conversion Instructions  
`avxvnni`| `avx2`| [AVX-
VNNI](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-
IFMA) — Advanced Vector Extensions - Vector Neural Network Instructions  
`avxvnniint16`| `avx2`| [AVX-VNNI-
INT16](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-
IFMA) — Advanced Vector Extensions - Vector Neural Network Instructions with
16-bit Integers  
`avxvnniint8`| `avx2`| [AVX-VNNI-
INT8](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-
IFMA) — Advanced Vector Extensions - Vector Neural Network Instructions with
8-bit Integers  
`bmi1`| | [BMI1](https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets) — Bit Manipulation Instruction Sets  
`bmi2`| | [BMI2](https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets#BMI2) — Bit Manipulation Instruction Sets 2  
`cmpxchg16b`| | [`cmpxchg16b`](https://www.felixcloutier.com/x86/cmpxchg8b:cmpxchg16b) — Compares and exchange 16 bytes (128 bits) of data atomically  
`f16c`| `avx`| [F16C](https://en.wikipedia.org/wiki/F16C) — 16-bit floating
point conversion instructions  
`fma`| `avx`| [FMA3](https://en.wikipedia.org/wiki/FMA_instruction_set) —
Three-operand fused multiply-add  
`fxsr`| | [`fxsave`](https://www.felixcloutier.com/x86/fxsave) and [`fxrstor`](https://www.felixcloutier.com/x86/fxrstor) — Save and restore x87 FPU, MMX Technology, and SSE State  
`gfni`| `sse2`| [GFNI](https://en.wikipedia.org/wiki/AVX-512#GFNI) — Galois
Field New Instructions  
`kl`| `sse2`|
[KEYLOCKER](https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_Key_Locker_instructions)
— Intel Key Locker Instructions  
`lzcnt`| | [`lzcnt`](https://www.felixcloutier.com/x86/lzcnt) — Leading zeros count  
`movbe`| | [`movbe`](https://www.felixcloutier.com/x86/movbe) — Move data after swapping bytes  
`pclmulqdq`| `sse2`|
[`pclmulqdq`](https://www.felixcloutier.com/x86/pclmulqdq) — Packed carry-less
multiplication quadword  
`popcnt`| | [`popcnt`](https://www.felixcloutier.com/x86/popcnt) — Count of bits set to 1  
`rdrand`| | [`rdrand`](https://en.wikipedia.org/wiki/RdRand) — Read random number  
`rdseed`| | [`rdseed`](https://en.wikipedia.org/wiki/RdRand) — Read random seed  
`sha`| `sse2`| [SHA](https://en.wikipedia.org/wiki/Intel_SHA_extensions) —
Secure Hash Algorithm  
`sha512`| `avx2`| [SHA512](https://en.wikipedia.org/wiki/Intel_SHA_extensions)
— Secure Hash Algorithm with 512-bit digest  
`sm3`| `avx`|
[SM3](https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_SHA_and_SM3_instructions)
— ShangMi 3 Hash Algorithm  
`sm4`| `avx2`|
[SM4](https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_SHA_and_SM3_instructions)
— ShangMi 4 Cipher Algorithm  
`sse`| | [SSE](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions) — Streaming SIMD Extensions  
`sse2`| `sse`| [SSE2](https://en.wikipedia.org/wiki/SSE2) — Streaming SIMD
Extensions 2  
`sse3`| `sse2`| [SSE3](https://en.wikipedia.org/wiki/SSE3) — Streaming SIMD
Extensions 3  
`sse4.1`| `ssse3`| [SSE4.1](https://en.wikipedia.org/wiki/SSE4#SSE4.1) —
Streaming SIMD Extensions 4.1  
`sse4.2`| `sse4.1`| [SSE4.2](https://en.wikipedia.org/wiki/SSE4#SSE4.2) —
Streaming SIMD Extensions 4.2  
`sse4a`| `sse3`| [SSE4a](https://en.wikipedia.org/wiki/SSE4#SSE4a) — Streaming
SIMD Extensions 4a  
`ssse3`| `sse3`| [SSSE3](https://en.wikipedia.org/wiki/SSSE3) — Supplemental
Streaming SIMD Extensions 3  
`tbm`| | [TBM](https://en.wikipedia.org/wiki/X86_Bit_manipulation_instruction_set#TBM_\(Trailing_Bit_Manipulation\)) — Trailing Bit Manipulation  
`vaes`| `avx2`, `aes`| [VAES](https://en.wikipedia.org/wiki/AVX-512#VAES) —
Vector AES Instructions  
`vpclmulqdq`| `avx`, `pclmulqdq`|
[VPCLMULQDQ](https://en.wikipedia.org/wiki/AVX-512#VPCLMULQDQ) — Vector Carry-
less multiplication of Quadwords  
`widekl`| `kl`|
[KEYLOCKER_WIDE](https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_Key_Locker_instructions)
— Intel Wide Keylocker Instructions  
`xsave`| | [`xsave`](https://www.felixcloutier.com/x86/xsave) — Save processor extended states  
`xsavec`| | [`xsavec`](https://www.felixcloutier.com/x86/xsavec) — Save processor extended states with compaction  
`xsaveopt`| | [`xsaveopt`](https://www.felixcloutier.com/x86/xsaveopt) — Save processor extended states optimized  
`xsaves`| | [`xsaves`](https://www.felixcloutier.com/x86/xsaves) — Save processor extended states supervisor  
  
[attributes.codegen.target_feature.aarch64]

#### `aarch64`

On this platform the usage of `#[target_feature]` functions follows the above
restrictions.

Further documentation on these features can be found in the [ARM Architecture
Reference Manual](https://developer.arm.com/documentation/ddi0487/latest), or
elsewhere on [developer.arm.com](https://developer.arm.com).

> Note
>
> The following pairs of features should both be marked as enabled or disabled
> together if used:
>
>   * `paca` and `pacg`, which LLVM currently implements as one feature.
>

Feature| Implicitly Enables| Feature Name  
---|---|---  
`aes`| `neon`| FEAT_AES & FEAT_PMULL — Advanced SIMD AES & PMULL instructions  
`bf16`| | FEAT_BF16 — BFloat16 instructions  
`bti`| | FEAT_BTI — Branch Target Identification  
`crc`| | FEAT_CRC — CRC32 checksum instructions  
`dit`| | FEAT_DIT — Data Independent Timing instructions  
`dotprod`| `neon`| FEAT_DotProd — Advanced SIMD Int8 dot product instructions  
`dpb`| | FEAT_DPB — Data cache clean to point of persistence  
`dpb2`| `dpb`| FEAT_DPB2 — Data cache clean to point of deep persistence  
`f32mm`| `sve`| FEAT_F32MM — SVE single-precision FP matrix multiply
instruction  
`f64mm`| `sve`| FEAT_F64MM — SVE double-precision FP matrix multiply
instruction  
`fcma`| `neon`| FEAT_FCMA — Floating point complex number support  
`fhm`| `fp16`| FEAT_FHM — Half-precision FP FMLAL instructions  
`flagm`| | FEAT_FLAGM — Conditional flag manipulation  
`fp16`| `neon`| FEAT_FP16 — Half-precision FP data processing  
`frintts`| | FEAT_FRINTTS — Floating-point to int helper instructions  
`i8mm`| | FEAT_I8MM — Int8 Matrix Multiplication  
`jsconv`| `neon`| FEAT_JSCVT — JavaScript conversion instruction  
`lor`| | FEAT_LOR — Limited Ordering Regions extension  
`lse`| | FEAT_LSE — Large System Extensions  
`mte`| | FEAT_MTE & FEAT_MTE2 — Memory Tagging Extension  
`neon`| | FEAT_AdvSimd & FEAT_FP — Floating Point and Advanced SIMD extension  
`paca`| | FEAT_PAUTH — Pointer Authentication (address authentication)  
`pacg`| | FEAT_PAUTH — Pointer Authentication (generic authentication)  
`pan`| | FEAT_PAN — Privileged Access-Never extension  
`pmuv3`| | FEAT_PMUv3 — Performance Monitors extension (v3)  
`rand`| | FEAT_RNG — Random Number Generator  
`ras`| | FEAT_RAS & FEAT_RASv1p1 — Reliability, Availability and Serviceability extension  
`rcpc`| | FEAT_LRCPC — Release consistent Processor Consistent  
`rcpc2`| `rcpc`| FEAT_LRCPC2 — RcPc with immediate offsets  
`rdm`| `neon`| FEAT_RDM — Rounding Double Multiply accumulate  
`sb`| | FEAT_SB — Speculation Barrier  
`sha2`| `neon`| FEAT_SHA1 & FEAT_SHA256 — Advanced SIMD SHA instructions  
`sha3`| `sha2`| FEAT_SHA512 & FEAT_SHA3 — Advanced SIMD SHA instructions  
`sm4`| `neon`| FEAT_SM3 & FEAT_SM4 — Advanced SIMD SM3/4 instructions  
`spe`| | FEAT_SPE — Statistical Profiling Extension  
`ssbs`| | FEAT_SSBS & FEAT_SSBS2 — Speculative Store Bypass Safe  
`sve`| `neon`| FEAT_SVE — Scalable Vector Extension  
`sve2`| `sve`| FEAT_SVE2 — Scalable Vector Extension 2  
`sve2-aes`| `sve2`, `aes`| FEAT_SVE_AES & FEAT_SVE_PMULL128 — SVE AES
instructions  
`sve2-bitperm`| `sve2`| FEAT_SVE2_BitPerm — SVE Bit Permute  
`sve2-sha3`| `sve2`, `sha3`| FEAT_SVE2_SHA3 — SVE SHA3 instructions  
`sve2-sm4`| `sve2`, `sm4`| FEAT_SVE2_SM4 — SVE SM4 instructions  
`tme`| | FEAT_TME — Transactional Memory Extension  
`vh`| | FEAT_VHE — Virtualization Host Extensions  
  
[attributes.codegen.target_feature.loongarch]

#### `loongarch`

On this platform the usage of `#[target_feature]` functions follows the above
restrictions.

Feature| Implicitly Enables| Description  
---|---|---  
`f`| | [F](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-fp_sp) — Single-precision float-point instructions  
`d`| `f`| [D](https://loongson.github.io/LoongArch-Documentation/LoongArch-
Vol1-EN.html#cpucfg-fp_dp) — Double-precision float-point instructions  
`frecipe`| | [FRECIPE](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-frecipe) — Reciprocal approximation instructions  
`lasx`| `lsx`| [LASX](https://loongson.github.io/LoongArch-
Documentation/LoongArch-Vol1-EN.html#cpucfg-lasx) — 256-bit vector
instructions  
`lbt`| | [LBT](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-lbt_x86) — Binary translation instructions  
`lsx`| `d`| [LSX](https://loongson.github.io/LoongArch-
Documentation/LoongArch-Vol1-EN.html#cpucfg-lsx) — 128-bit vector instructions  
`lvz`| | [LVZ](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-lvz) — Virtualization instructions  
  
[attributes.codegen.target_feature.riscv]

#### `riscv32` or `riscv64`

On this platform the usage of `#[target_feature]` functions follows the above
restrictions.

Further documentation on these features can be found in their respective
specification. Many specifications are described in the [RISC-V ISA
Manual](https://github.com/riscv/riscv-isa-manual), [version
20250508](https://github.com/riscv/riscv-isa-manual/tree/20250508), or in
another manual hosted on the [RISC-V GitHub
Account](https://github.com/riscv).

Feature| Implicitly Enables| Description  
---|---|---  
`a`| `zaamo`, `zalrsc`| [A](https://github.com/riscv/riscv-isa-
manual/blob/20250508/src/a-st-ext.adoc) — Atomic instructions  
`b`| `zba`, `zbc`, `zbs`| [B](https://github.com/riscv/riscv-isa-
manual/blob/20250508/src/b-st-ext.adoc) — Bit Manipulation instructions  
`c`| `zca`| [C](https://github.com/riscv/riscv-isa-
manual/blob/20250508/src/c-st-ext.adoc) — Compressed instructions  
`m`| | [M](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/m-st-ext.adoc) — Integer Multiplication and Division instructions  
`za64rs`| `za128rs`| [Za64rs](https://github.com/riscv/riscv-
profiles/blob/rva23-rvb23-ratified/src/rva23-profile.adoc) — Platform
Behavior: Naturally aligned Reservation sets with ≦ 64 Bytes  
`za128rs`| | [Za128rs](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Naturally aligned Reservation sets with ≦ 128 Bytes  
`zaamo`| | [Zaamo](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/a-st-ext.adoc) — Atomic Memory Operation instructions  
`zabha`| `zaamo`| [Zabha](https://github.com/riscv/riscv-isa-
manual/blob/20250508/src/zabha.adoc) — Byte and Halfword Atomic Memory
Operation instructions  
`zacas`| `zaamo`| [Zacas](https://github.com/riscv/riscv-isa-
manual/blob/20250508/src/zacas.adoc) — Atomic Compare-and-Swap (CAS)
instructions  
`zalrsc`| | [Zalrsc](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/a-st-ext.adoc) — Load-Reserved/Store-Conditional instructions  
`zama16b`| | [Zama16b](https://github.com/riscv/riscv-profiles/blob/rva23-rvb23-ratified/src/rva23-profile.adoc) — Platform Behavior: Misaligned loads, stores, and AMOs to main memory regions that do not cross a naturally aligned 16-byte boundary are atomic  
`zawrs`| | [Zawrs](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zawrs.adoc) — Wait-on-Reservation-Set instructions  
`zba`| | [Zba](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Address Generation instructions  
`zbb`| | [Zbb](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Basic bit-manipulation  
`zbc`| `zbkc`| [Zbc](https://github.com/riscv/riscv-isa-
manual/blob/20250508/src/b-st-ext.adoc) — Carry-less multiplication  
`zbkb`| | [Zbkb](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Bit Manipulation Instructions for Cryptography  
`zbkc`| | [Zbkc](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Carry-less multiplication for Cryptography  
`zbkx`| | [Zbkx](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Crossbar permutations  
`zbs`| | [Zbs](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Single-bit instructions  
`zca`| | [Zca](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zc.adoc) — Compressed instructions: integer part subset  
`zcb`| `zca`| [Zcb](https://github.com/riscv/riscv-isa-
manual/blob/20250508/src/zc.adoc) — Simple Code-size Saving Compressed
instructions  
`zcmop`| `zca`| [Zcmop](https://github.com/riscv/riscv-isa-
manual/blob/20250508/src/zimop.adoc) — Compressed May-Be-Operations  
`zic64b`| | [Zic64b](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Naturally aligned 64 byte Cache blocks  
`zicbom`| | [Zicbom](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/cmo.adoc) — Cache-Block Management instructions  
`zicbop`| | [Zicbop](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/cmo.adoc) — Cache-Block Prefetch Hint instructions  
`zicboz`| | [Zicboz](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/cmo.adoc) — Cache-Block Zero instruction  
`ziccamoa`| | [Ziccamoa](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Cacheable and Coherent Main memory supports all basic atomic operations  
`ziccif`| | [Ziccif](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Cacheable and Coherent Main memory supports instruction fetch and fetches of naturally aligned power-of-2 sizes up to `min(ILEN,XLEN)` are atomic  
`zicclsm`| | [Zicclsm](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Cacheable and Coherent Main memory supports misaligned load/store accesses  
`ziccrse`| | [Ziccrse](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Cacheable and Coherent Main memory guarantees eventual success on LR/SC sequences  
`zicntr`| `zicsr`| [Zicntr](https://github.com/riscv/riscv-isa-
manual/blob/20250508/src/counters.adoc) — Base Counters and Timers  
`zicond`| | [Zicond](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zicond.adoc) — Integer Conditional Operation instructions  
`zicsr`| | [Zicsr](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zicsr.adoc) — Control and Status Register (CSR) instructions  
`zifencei`| | [Zifencei](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zifencei.adoc) — Instruction-Fetch Fence instruction  
`zihintntl`| | [Zihintntl](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zihintntl.adoc) — Non-Temporal Locality Hint instructions  
`zihintpause`| | [Zihintpause](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zihintpause.adoc) — Pause Hint instruction  
`zihpm`| `zicsr`| [Zihpm](https://github.com/riscv/riscv-isa-
manual/blob/20250508/src/counters.adoc) — Hardware Performance Counters  
`zimop`| | [Zimop](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zimop.adoc) — May-Be-Operations  
`zk`| `zkn`, `zkr`, `zks`, `zkt`, `zbkb`, `zbkc`, `zkbx`|
[Zk](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-
crypto.adoc) — Scalar Cryptography  
`zkn`| `zknd`, `zkne`, `zknh`, `zbkb`, `zbkc`, `zkbx`|
[Zkn](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-
crypto.adoc) — NIST Algorithm suite extension  
`zknd`| | [Zknd](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — NIST Suite: AES Decryption  
`zkne`| | [Zkne](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — NIST Suite: AES Encryption  
`zknh`| | [Zknh](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — NIST Suite: Hash Function Instructions  
`zkr`| | [Zkr](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — Entropy Source Extension  
`zks`| `zksed`, `zksh`, `zbkb`, `zbkc`, `zkbx`|
[Zks](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-
crypto.adoc) — ShangMi Algorithm Suite  
`zksed`| | [Zksed](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — ShangMi Suite: SM4 Block Cipher Instructions  
`zksh`| | [Zksh](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — ShangMi Suite: SM3 Hash Function Instructions  
`zkt`| | [Zkt](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — Data Independent Execution Latency Subset  
`ztso`| | [Ztso](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/ztso-st-ext.adoc) — Total Store Ordering  
  
[attributes.codegen.target_feature.wasm]

#### `wasm32` or `wasm64`

Safe `#[target_feature]` functions may always be used in safe contexts on Wasm
platforms. It is impossible to cause undefined behavior via the
`#[target_feature]` attribute because attempting to use instructions
unsupported by the Wasm engine will fail at load time without the risk of
being interpreted in a way different from what the compiler expected.

Feature| Implicitly Enables| Description  
---|---|---  
`bulk-memory`| | [WebAssembly bulk memory operations proposal](https://github.com/WebAssembly/bulk-memory-operations)  
`extended-const`| | [WebAssembly extended const expressions proposal](https://github.com/WebAssembly/extended-const)  
`mutable-globals`| | [WebAssembly mutable global proposal](https://github.com/WebAssembly/mutable-global)  
`nontrapping-fptoint`| | [WebAssembly non-trapping float-to-int conversion proposal](https://github.com/WebAssembly/nontrapping-float-to-int-conversions)  
`relaxed-simd`| `simd128`| [WebAssembly relaxed simd
proposal](https://github.com/WebAssembly/relaxed-simd)  
`sign-ext`| | [WebAssembly sign extension operators Proposal](https://github.com/WebAssembly/sign-extension-ops)  
`simd128`| | [WebAssembly simd proposal](https://github.com/webassembly/simd)  
`multivalue`| | [WebAssembly multivalue proposal](https://github.com/webassembly/multi-value)  
`reference-types`| | [WebAssembly reference-types proposal](https://github.com/webassembly/reference-types)  
`tail-call`| | [WebAssembly tail-call proposal](https://github.com/webassembly/tail-call)  
  
[attributes.codegen.target_feature.s390x]

#### `s390x`

On `s390x` targets, use of functions with the `#[target_feature]` attribute
follows the above restrictions.

Further documentation on these features can be found in the “Additions to
z/Architecture” section of Chapter 1 of the _[z/Architecture Principles of
Operation](https://publibfp.dhe.ibm.com/epubs/pdf/a227832d.pdf)_.

Feature| Implicitly Enables| Description  
---|---|---  
`vector`| | 128-bit vector instructions  
`vector-enhancements-1`| `vector`| vector enhancements 1  
`vector-enhancements-2`| `vector-enhancements-1`| vector enhancements 2  
`vector-enhancements-3`| `vector-enhancements-2`| vector enhancements 3  
`vector-packed-decimal`| `vector`| vector packed-decimal  
`vector-packed-decimal-enhancement`| `vector-packed-decimal`| vector packed-
decimal enhancement  
`vector-packed-decimal-enhancement-2`| `vector-packed-decimal-enhancement-2`|
vector packed-decimal enhancement 2  
`vector-packed-decimal-enhancement-3`| `vector-packed-decimal-enhancement-3`|
vector packed-decimal enhancement 3  
`nnp-assist`| `vector`| nnp assist  
`miscellaneous-extensions-2`| | miscellaneous extensions 2  
`miscellaneous-extensions-3`| | miscellaneous extensions 3  
`miscellaneous-extensions-4`| | miscellaneous extensions 4  
  
[attributes.codegen.target_feature.info]

### Additional information

[attributes.codegen.target_feature.remark-cfg]

See the `target_feature` conditional compilation option for selectively
enabling or disabling compilation of code based on compile-time settings. Note
that this option is not affected by the `target_feature` attribute, and is
only driven by the features enabled for the entire crate.

[attributes.codegen.target_feature.remark-rt]

Whether a feature is enabled can be checked at runtime using a platform-
specific macro from the standard library, for instance
[`is_x86_feature_detected`](../std/arch/macro.is_x86_feature_detected.html) or
[`is_aarch64_feature_detected`](../std/arch/macro.is_aarch64_feature_detected.html).

> Note
>
> `rustc` has a default set of features enabled for each target and CPU. The
> CPU may be chosen with the [`-C target-cpu`](../rustc/codegen-
> options/index.html#target-cpu) flag. Individual features may be enabled or
> disabled for an entire crate with the [`-C target-
> feature`](../rustc/codegen-options/index.html#target-feature) flag.

[attributes.codegen.track_caller]

## The `track_caller` attribute

[attributes.codegen.track_caller.allowed-positions]

The `track_caller` attribute may be applied to any function with `"Rust"` ABI
with the exception of the entry point `fn main`.

[attributes.codegen.track_caller.traits]

When applied to functions and methods in trait declarations, the attribute
applies to all implementations. If the trait provides a default implementation
with the attribute, then the attribute also applies to override
implementations.

[attributes.codegen.track_caller.extern]

When applied to a function in an `extern` block the attribute must also be
applied to any linked implementations, otherwise undefined behavior results.
When applied to a function which is made available to an `extern` block, the
declaration in the `extern` block must also have the attribute, otherwise
undefined behavior results.

[attributes.codegen.track_caller.behavior]

### Behavior

Applying the attribute to a function `f` allows code within `f` to get a hint
of the [`Location`](../core/panic/location/struct.Location.html) of the
“topmost” tracked call that led to `f`’s invocation. At the point of
observation, an implementation behaves as if it walks up the stack from `f`’s
frame to find the nearest frame of an _unattributed_ function `outer`, and it
returns the [`Location`](../core/panic/location/struct.Location.html) of the
tracked call in `outer`.

    
    
    #![allow(unused)]
    fn main() {
    #[track_caller]
    fn f() {
        println!("{}", std::panic::Location::caller());
    }
    }

> Note
>
> `core` provides
> [`core::panic::Location::caller`](../core/panic/location/struct.Location.html#method.caller)
> for observing caller locations. It wraps the
> [`core::intrinsics::caller_location`](../core/intrinsics/fn.caller_location.html)
> intrinsic implemented by `rustc`.

> Note
>
> Because the resulting `Location` is a hint, an implementation may halt its
> walk up the stack early. See Limitations for important caveats.

#### Examples

When `f` is called directly by `calls_f`, code in `f` observes its callsite
within `calls_f`:

    
    
    #![allow(unused)]
    fn main() {
    #[track_caller]
    fn f() {
        println!("{}", std::panic::Location::caller());
    }
    fn calls_f() {
        f(); // <-- f() prints this location
    }
    }

When `f` is called by another attributed function `g` which is in turn called
by `calls_g`, code in both `f` and `g` observes `g`’s callsite within
`calls_g`:

    
    
    #![allow(unused)]
    fn main() {
    #[track_caller]
    fn f() {
        println!("{}", std::panic::Location::caller());
    }
    #[track_caller]
    fn g() {
        println!("{}", std::panic::Location::caller());
        f();
    }
    
    fn calls_g() {
        g(); // <-- g() prints this location twice, once itself and once from f()
    }
    }

When `g` is called by another attributed function `h` which is in turn called
by `calls_h`, all code in `f`, `g`, and `h` observes `h`’s callsite within
`calls_h`:

    
    
    #![allow(unused)]
    fn main() {
    #[track_caller]
    fn f() {
        println!("{}", std::panic::Location::caller());
    }
    #[track_caller]
    fn g() {
        println!("{}", std::panic::Location::caller());
        f();
    }
    #[track_caller]
    fn h() {
        println!("{}", std::panic::Location::caller());
        g();
    }
    
    fn calls_h() {
        h(); // <-- prints this location three times, once itself, once from g(), once from f()
    }
    }

And so on.

[attributes.codegen.track_caller.limits]

### Limitations

[attributes.codegen.track_caller.hint]

This information is a hint and implementations are not required to preserve
it.

[attributes.codegen.track_caller.decay]

In particular, coercing a function with `#[track_caller]` to a function
pointer creates a shim which appears to observers to have been called at the
attributed function’s definition site, losing actual caller information across
virtual calls. A common example of this coercion is the creation of a trait
object whose methods are attributed.

> Note
>
> The aforementioned shim for function pointers is necessary because `rustc`
> implements `track_caller` in a codegen context by appending an implicit
> parameter to the function ABI, but this would be unsound for an indirect
> call because the parameter is not a part of the function’s type and a given
> function pointer type may or may not refer to a function with the attribute.
> The creation of a shim hides the implicit parameter from callers of the
> function pointer, preserving soundness.

[attributes.codegen.instruction_set]

## The `instruction_set` attribute

[attributes.codegen.instruction_set.intro]

The _`instruction_set` attribute_ specifies the instruction set that a
function will use during code generation. This allows mixing more than one
instruction set in a single program.

> Example
>  
>  
>     #[instruction_set(arm::a32)]
>     fn arm_code() {}
>  
>     #[instruction_set(arm::t32)]
>     fn thumb_code() {}

[attributes.codegen.instruction_set.syntax]

The `instruction_set` attribute uses the MetaListPaths syntax to specify a
single path consisting of the architecture family name and instruction set
name.

[attributes.codegen.instruction_set.allowed-positions]

The `instruction_set` attribute may only be applied to functions with bodies —
closures, async blocks, free functions, associated functions in an inherent
impl or trait impl, and associated functions in a trait definition when those
functions have a default definition .

> Note
>
> `rustc` ignores use in other positions but lints against it. This may become
> an error in the future.

> Note
>
> Though the attribute can be applied to closures and async blocks, the
> usefulness of this is limited as we do not yet support attributes on
> expressions.

[attributes.codegen.instruction_set.duplicates]

The `instruction_set` attribute may be used only once on a function.

[attributes.codegen.instruction_set.target-limits]

The `instruction_set` attribute may only be used with a target that supports
the given value.

[attributes.codegen.instruction_set.inline-asm]

When the `instruction_set` attribute is used, any inline assembly in the
function must use the specified instruction set instead of the target default.

[attributes.codegen.instruction_set.arm]

### `instruction_set` on ARM

When targeting the `ARMv4T` and `ARMv5te` architectures, the supported values
for `instruction_set` are:

  * `arm::a32` — Generate the function as A32 “ARM” code.
  * `arm::t32` — Generate the function as T32 “Thumb” code.

If the address of the function is taken as a function pointer, the low bit of
the address will depend on the selected instruction set:

  * For `arm::a32` (“ARM”), it will be 0.
  * For `arm::t32` (“Thumb”), it will be 1.

[attributes.limits]

# Limits

The following attributes affect compile-time limits.

[attributes.limits.recursion_limit]

## The `recursion_limit` attribute

[attributes.limits.recursion_limit.intro]

The _`recursion_limit` attribute_ may be applied at the crate level to set the
maximum depth for potentially infinitely-recursive compile-time operations
like macro expansion or auto-dereference.

[attributes.limits.recursion_limit.syntax]

It uses the MetaNameValueStr syntax to specify the recursion depth.

> Note
>
> The default in `rustc` is 128.
    
    
    #![allow(unused)]
    #![recursion_limit = "4"]
    
    fn main() {
    macro_rules! a {
        () => { a!(1); };
        (1) => { a!(2); };
        (2) => { a!(3); };
        (3) => { a!(4); };
        (4) => { };
    }
    
    // This fails to expand because it requires a recursion depth greater than 4.
    a!{}
    }
    
    
    #![allow(unused)]
    #![recursion_limit = "1"]
    
    fn main() {
    // This fails because it requires two recursive steps to auto-dereference.
    (|_: &u8| {})(&&&1);
    }

[attributes.limits.type_length_limit]

## The `type_length_limit` attribute

[attributes.limits.type_length_limit.intro]

The _`type_length_limit` attribute_ sets the maximum number of type
substitutions allowed when constructing a concrete type during
monomorphization.

> Note
>
> `rustc` only enforces the limit when the nightly `-Zenforce-type-length-
> limit` flag is active.
>
> For more information, see [Rust PR #127670](https://github.com/rust-
> lang/rust/pull/127670).

> Example
>  
>  
>     #![type_length_limit = "4"]
>  
>     fn f<T>(x: T) {}
>  
>     // This fails to compile because monomorphizing to
>     // `f::<((((i32,), i32), i32), i32)>` requires more
>     // than 4 type elements.
>     f(((((1,), 2), 3), 4));

> Note
>
> The default value in `rustc` is `1048576`.

[attributes.limits.type_length_limit.syntax]

The `type_length_limit` attribute uses the MetaNameValueStr syntax. The value
in the string must be a non-negative number.

[attributes.limits.type_length_limit.allowed-positions]

The `type_length_limit` attribute may only be applied to the crate root.

> Note
>
> `rustc` ignores use in other positions but lints against it. This may become
> an error in the future.

[attributes.limits.type_length_limit.duplicates]

Only the first use of `type_length_limit` on an item has effect.

> Note
>
> `rustc` lints against any use following the first. This may become an error
> in the future.

[attributes.type-system]

# Type system attributes

The following attributes are used for changing how a type can be used.

[attributes.type-system.non_exhaustive]

## The `non_exhaustive` attribute

[attributes.type-system.non_exhaustive.intro]

The _`non_exhaustive` attribute_ indicates that a type or variant may have
more fields or variants added in the future.

[attributes.type-system.non_exhaustive.allowed-positions]

It can be applied to `struct`s, `enum`s, and `enum` variants.

[attributes.type-system.non_exhaustive.syntax]

The `non_exhaustive` attribute uses the MetaWord syntax and thus does not take
any inputs.

[attributes.type-system.non_exhaustive.same-crate]

Within the defining crate, `non_exhaustive` has no effect.

    
    
    #![allow(unused)]
    fn main() {
    #[non_exhaustive]
    pub struct Config {
        pub window_width: u16,
        pub window_height: u16,
    }
    
    #[non_exhaustive]
    pub struct Token;
    
    #[non_exhaustive]
    pub struct Id(pub u64);
    
    #[non_exhaustive]
    pub enum Error {
        Message(String),
        Other,
    }
    
    pub enum Message {
        #[non_exhaustive] Send { from: u32, to: u32, contents: String },
        #[non_exhaustive] Reaction(u32),
        #[non_exhaustive] Quit,
    }
    
    // Non-exhaustive structs can be constructed as normal within the defining crate.
    let config = Config { window_width: 640, window_height: 480 };
    let token = Token;
    let id = Id(4);
    
    // Non-exhaustive structs can be matched on exhaustively within the defining crate.
    let Config { window_width, window_height } = config;
    let Token = token;
    let Id(id_number) = id;
    
    let error = Error::Other;
    let message = Message::Reaction(3);
    
    // Non-exhaustive enums can be matched on exhaustively within the defining crate.
    match error {
        Error::Message(ref s) => { },
        Error::Other => { },
    }
    
    match message {
        // Non-exhaustive variants can be matched on exhaustively within the defining crate.
        Message::Send { from, to, contents } => { },
        Message::Reaction(id) => { },
        Message::Quit => { },
    }
    }

[attributes.type-system.non_exhaustive.external-crate]

Outside of the defining crate, types annotated with `non_exhaustive` have
limitations that preserve backwards compatibility when new fields or variants
are added.

[attributes.type-system.non_exhaustive.construction]

Non-exhaustive types cannot be constructed outside of the defining crate:

  * Non-exhaustive variants (`struct` or `enum` variant) cannot be constructed with a StructExpression (including with functional update syntax).
  * The implicitly defined same-named constant of a unit-like struct, or the same-named constructor function of a tuple struct, has a visibility no greater than `pub(crate)`. That is, if the struct’s visibility is `pub`, then the constant or constructor’s visibility is `pub(crate)`, and otherwise the visibility of the two items is the same (as is the case without `#[non_exhaustive]`).
  * `enum` instances can be constructed.

The following examples of construction do not compile when outside the
defining crate:

    
    
    // These are types defined in an upstream crate that have been annotated as
    // `#[non_exhaustive]`.
    use upstream::{Config, Token, Id, Error, Message};
    
    // Cannot construct an instance of `Config`; if new fields were added in
    // a new version of `upstream` then this would fail to compile, so it is
    // disallowed.
    let config = Config { window_width: 640, window_height: 480 };
    
    // Cannot construct an instance of `Token`; if new fields were added, then
    // it would not be a unit-like struct any more, so the same-named constant
    // created by it being a unit-like struct is not public outside the crate;
    // this code fails to compile.
    let token = Token;
    
    // Cannot construct an instance of `Id`; if new fields were added, then
    // its constructor function signature would change, so its constructor
    // function is not public outside the crate; this code fails to compile.
    let id = Id(5);
    
    // Can construct an instance of `Error`; new variants being introduced would
    // not result in this failing to compile.
    let error = Error::Message("foo".to_string());
    
    // Cannot construct an instance of `Message::Send` or `Message::Reaction`;
    // if new fields were added in a new version of `upstream` then this would
    // fail to compile, so it is disallowed.
    let message = Message::Send { from: 0, to: 1, contents: "foo".to_string(), };
    let message = Message::Reaction(0);
    
    // Cannot construct an instance of `Message::Quit`; if this were converted to
    // a tuple enum variant `upstream`, this would fail to compile.
    let message = Message::Quit;

[attributes.type-system.non_exhaustive.match]

There are limitations when matching on non-exhaustive types outside of the
defining crate:

  * When pattern matching on a non-exhaustive variant (`struct` or `enum` variant), a StructPattern must be used which must include a `..`. A tuple enum variant’s constructor’s visibility is reduced to be no greater than `pub(crate)`.
  * When pattern matching on a non-exhaustive `enum`, matching on a variant does not contribute towards the exhaustiveness of the arms. The following examples of matching do not compile when outside the defining crate:

    
    
    // These are types defined in an upstream crate that have been annotated as
    // `#[non_exhaustive]`.
    use upstream::{Config, Token, Id, Error, Message};
    
    // Cannot match on a non-exhaustive enum without including a wildcard arm.
    match error {
      Error::Message(ref s) => { },
      Error::Other => { },
      // would compile with: `_ => {},`
    }
    
    // Cannot match on a non-exhaustive struct without a wildcard.
    if let Ok(Config { window_width, window_height }) = config {
        // would compile with: `..`
    }
    
    // Cannot match a non-exhaustive unit-like or tuple struct except by using
    // braced struct syntax with a wildcard.
    // This would compile as `let Token { .. } = token;`
    let Token = token;
    // This would compile as `let Id { 0: id_number, .. } = id;`
    let Id(id_number) = id;
    
    match message {
      // Cannot match on a non-exhaustive struct enum variant without including a wildcard.
      Message::Send { from, to, contents } => { },
      // Cannot match on a non-exhaustive tuple or unit enum variant.
      Message::Reaction(type) => { },
      Message::Quit => { },
    }

It’s also not allowed to use numeric casts (`as`) on enums that contain any
non-exhaustive variants.

For example, the following enum can be cast because it doesn’t contain any
non-exhaustive variants:

    
    
    #![allow(unused)]
    fn main() {
    #[non_exhaustive]
    pub enum Example {
        First,
        Second
    }
    }

However, if the enum contains even a single non-exhaustive variant, casting
will result in an error. Consider this modified version of the same enum:

    
    
    #![allow(unused)]
    fn main() {
    #[non_exhaustive]
    pub enum EnumWithNonExhaustiveVariants {
        First,
        #[non_exhaustive]
        Second
    }
    }
    
    
    use othercrate::EnumWithNonExhaustiveVariants;
    
    // Error: cannot cast an enum with a non-exhaustive variant when it's defined in another crate
    let _ = EnumWithNonExhaustiveVariants::First as u8;

Non-exhaustive types are always considered inhabited in downstream crates.

[attributes.debugger]

# Debugger attributes

The following attributes are used for enhancing the debugging experience when
using third-party debuggers like GDB or WinDbg.

[attributes.debugger.debugger_visualizer]

## The `debugger_visualizer` attribute

[attributes.debugger.debugger_visualizer.intro]

The _`debugger_visualizer` attribute_ can be used to embed a debugger
visualizer file into the debug information. This improves the debugger
experience when displaying values.

> Example
>  
>  
>     #![debugger_visualizer(natvis_file = "Example.natvis")]
>     #![debugger_visualizer(gdb_script_file = "example.py")]

[attributes.debugger.debugger_visualizer.syntax]

The `debugger_visualizer` attribute uses the MetaListNameValueStr syntax to
specify its inputs. One of the following keys must be specified:

  * `natvis_file`
  * `gdb_script_file`

[attributes.debugger.debugger_visualizer.allowed-positions]

The `debugger_visualizer` attribute may only be applied to a module or to the
crate root.

[attributes.debugger.debugger_visualizer.duplicates]

The `debugger_visualizer` attribute may be used any number of times on a form.
All specified visualizer files will be loaded.

[attributes.debugger.debugger_visualizer.natvis]

### Using `debugger_visualizer` with Natvis

[attributes.debugger.debugger_visualizer.natvis.intro]

Natvis is an XML-based framework for Microsoft debuggers (such as Visual
Studio and WinDbg) that uses declarative rules to customize the display of
types. For detailed information on the Natvis format, refer to Microsoft’s
[Natvis documentation](https://docs.microsoft.com/en-
us/visualstudio/debugger/create-custom-views-of-native-objects).

[attributes.debugger.debugger_visualizer.natvis.msvc]

This attribute only supports embedding Natvis files on `-windows-msvc`
targets.

[attributes.debugger.debugger_visualizer.natvis.path]

The path to the Natvis file is specified with the `natvis_file` key, which is
a path relative to the source file.

> Example
>  
>  
>     #![debugger_visualizer(natvis_file = "Rectangle.natvis")]
>  
>     struct FancyRect {
>         x: f32,
>         y: f32,
>         dx: f32,
>         dy: f32,
>     }
>  
>     fn main() {
>         let fancy_rect = FancyRect { x: 10.0, y: 10.0, dx: 5.0, dy: 5.0 };
>         println!("set breakpoint here");
>     }
>
> `Rectangle.natvis` contains:
>  
>  
>     <?xml version="1.0" encoding="utf-8"?>
>     <AutoVisualizer
> xmlns="http://schemas.microsoft.com/vstudio/debugger/natvis/2010">
>         <Type Name="foo::FancyRect">
>           <DisplayString>({x},{y}) + ({dx}, {dy})</DisplayString>
>           <Expand>
>             <Synthetic Name="LowerLeft">
>               <DisplayString>({x}, {y})</DisplayString>
>             </Synthetic>
>             <Synthetic Name="UpperLeft">
>               <DisplayString>({x}, {y + dy})</DisplayString>
>             </Synthetic>
>             <Synthetic Name="UpperRight">
>               <DisplayString>({x + dx}, {y + dy})</DisplayString>
>             </Synthetic>
>             <Synthetic Name="LowerRight">
>               <DisplayString>({x + dx}, {y})</DisplayString>
>             </Synthetic>
>           </Expand>
>         </Type>
>     </AutoVisualizer>
>  
>
> When viewed under WinDbg, the `fancy_rect` variable would be shown as
> follows:
>  
>  
>     > Variables:
>       > fancy_rect: (10.0, 10.0) + (5.0, 5.0)
>         > LowerLeft: (10.0, 10.0)
>         > UpperLeft: (10.0, 15.0)
>         > UpperRight: (15.0, 15.0)
>         > LowerRight: (15.0, 10.0)
>  

[attributes.debugger.debugger_visualizer.gdb]

### Using `debugger_visualizer` with GDB

[attributes.debugger.debugger_visualizer.gdb.pretty]

GDB supports the use of a structured Python script, called a _pretty printer_
, that describes how a type should be visualized in the debugger view. For
detailed information on pretty printers, refer to GDB’s [pretty printing
documentation](https://sourceware.org/gdb/onlinedocs/gdb/Pretty-
Printing.html).

> Note
>
> Embedded pretty printers are not automatically loaded when debugging a
> binary under GDB.
>
> There are two ways to enable auto-loading embedded pretty printers:
>
>   1. Launch GDB with extra arguments to explicitly add a directory or binary
> to the auto-load safe path: `gdb -iex "add-auto-load-safe-path safe-path
> path/to/binary" path/to/binary` For more information, see GDB’s [auto-
> loading
> documentation](https://sourceware.org/gdb/onlinedocs/gdb/Auto_002dloading-
> safe-path.html).
>   2. Create a file named `gdbinit` under `$HOME/.config/gdb` (you may need
> to create the directory if it doesn’t already exist). Add the following line
> to that file: `add-auto-load-safe-path path/to/binary`.
>

[attributes.debugger.debugger_visualizer.gdb.path]

These scripts are embedded using the `gdb_script_file` key, which is a path
relative to the source file.

> Example
>  
>  
>     #![debugger_visualizer(gdb_script_file = "printer.py")]
>  
>     struct Person {
>         name: String,
>         age: i32,
>     }
>  
>     fn main() {
>         let bob = Person { name: String::from("Bob"), age: 10 };
>         println!("set breakpoint here");
>     }
>
> `printer.py` contains:
>  
>  
>     import gdb
>  
>     class PersonPrinter:
>         "Print a Person"
>  
>         def __init__(self, val):
>             self.val = val
>             self.name = val["name"]
>             self.age = int(val["age"])
>  
>         def to_string(self):
>             return "{} is {} years old.".format(self.name, self.age)
>  
>     def lookup(val):
>         lookup_tag = val.type.tag
>         if lookup_tag is None:
>             return None
>         if "foo::Person" == lookup_tag:
>             return PersonPrinter(val)
>  
>         return None
>  
>     gdb.current_objfile().pretty_printers.append(lookup)
>  
>
> When the crate’s debug executable is passed into GDB1, `print bob` will
> display:
>  
>  
>     "Bob" is 10 years old.
>  

[attributes.debugger.collapse_debuginfo]

## The `collapse_debuginfo` attribute

[attributes.debugger.collapse_debuginfo.intro]

The _`collapse_debuginfo` attribute_ controls whether code locations from a
macro definition are collapsed into a single location associated with the
macro’s call site when generating debuginfo for code calling this macro.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #[collapse_debuginfo(yes)]
>     macro_rules! example {
>         () => {
>             println!("hello!");
>         };
>     }
>     }
>
> When using a debugger, invoking the `example` macro may appear as though it
> is calling a function. That is, when you step to the invocation site, it may
> show the macro invocation rather than the expanded code.

[attributes.debugger.collapse_debuginfo.syntax]

The syntax for the `collapse_debuginfo` attribute is:

**Syntax**  
CollapseDebuginfoAttribute → collapse_debuginfo ( CollapseDebuginfoOption )

CollapseDebuginfoOption →  
yes  
| no  
| external

Show Railroad

CollapseDebuginfoAttribute collapse_debuginfo ( CollapseDebuginfoOption )

CollapseDebuginfoOption yes no external

[attributes.debugger.collapse_debuginfo.allowed-positions]

The `collapse_debuginfo` attribute may only be applied to a `macro_rules`
definition.

[attributes.debugger.collapse_debuginfo.duplicates]

The `collapse_debuginfo` attribute may used only once on a macro.

[attributes.debugger.collapse_debuginfo.options]

The `collapse_debuginfo` attribute accepts these options:

  * `#[collapse_debuginfo(yes)]` — Code locations in debuginfo are collapsed.
  * `#[collapse_debuginfo(no)]` — Code locations in debuginfo are not collapsed.
  * `#[collapse_debuginfo(external)]` — Code locations in debuginfo are collapsed only if the macro comes from a different crate.

[attributes.debugger.collapse_debuginfo.default]

The `external` behavior is the default for macros that don’t have this
attribute unless they are built-in macros. For built-in macros the default is
`yes`.

> Note
>
> `rustc` has a [`-C collapse-macro-debuginfo`](../rustc/codegen-
> options/index.html#collapse-macro-debuginfo) CLI option to override both the
> default behavior and the values of any `#[collapse_debuginfo]` attributes.

* * *

  1. Note: This assumes you are using the `rust-gdb` script which configures pretty-printers for standard library types like `String`. ↩

[stmt-expr]

# Statements and expressions

Rust is _primarily_ an expression language. This means that most forms of
value-producing or effect-causing evaluation are directed by the uniform
syntax category of _expressions_. Each kind of expression can typically _nest_
within each other kind of expression, and rules for evaluation of expressions
involve specifying both the value produced by the expression and the order in
which its sub-expressions are themselves evaluated.

In contrast, statements serve _mostly_ to contain and explicitly sequence
expression evaluation.

[statement]

# Statements

[statement.syntax]

**Syntax**  
Statement →  
;  
| Item  
| LetStatement  
| ExpressionStatement  
| OuterAttribute* MacroInvocationSemi

Show Railroad

Statement ; Item LetStatement ExpressionStatement OuterAttribute
MacroInvocationSemi

[statement.intro]

A _statement_ is a component of a block, which is in turn a component of an
outer expression or function.

[statement.kind]

Rust has two kinds of statement: declaration statements and expression
statements.

[statement.decl]

## Declaration statements

A _declaration statement_ is one that introduces one or more _names_ into the
enclosing statement block. The declared names may denote new variables or new
items.

The two kinds of declaration statements are item declarations and `let`
statements.

[statement.item]

### Item declarations

[statement.item.intro]

An _item declaration statement_ has a syntactic form identical to an item
declaration within a module.

[statement.item.scope]

Declaring an item within a statement block restricts its scope to the block
containing the statement. The item is not given a canonical path nor are any
sub-items it may declare.

[statement.item.associated-scope]

The exception to this is that associated items defined by implementations are
still accessible in outer scopes as long as the item and, if applicable, trait
are accessible. It is otherwise identical in meaning to declaring the item
inside a module.

[statement.item.outer-generics]

There is no implicit capture of the containing function’s generic parameters,
parameters, and local variables. For example, `inner` may not access
`outer_var`.

    
    
    #![allow(unused)]
    fn main() {
    fn outer() {
      let outer_var = true;
    
      fn inner() { /* outer_var is not in scope here */ }
    
      inner();
    }
    }

[statement.let]

### `let` statements

[statement.let.syntax]

**Syntax**  
LetStatement →  
OuterAttribute* let PatternNoTopAlt ( : Type )?  
(  
= Expression  
| = Expressionexcept LazyBooleanExpression or end with a `}` else
BlockExpression  
)? ;

Show Railroad

LetStatement OuterAttribute let PatternNoTopAlt : Type = Expression = except
LazyBooleanExpression or end with a `}` Expression else BlockExpression ;

[statement.let.intro]

A _`let` statement_ introduces a new set of variables, given by a pattern. The
pattern is followed optionally by a type annotation and then either ends, or
is followed by an initializer expression plus an optional `else` block.

[statement.let.inference]

When no type annotation is given, the compiler will infer the type, or signal
an error if insufficient type information is available for definite inference.

[statement.let.scope]

Any variables introduced by a variable declaration are visible from the point
of declaration until the end of the enclosing block scope, except when they
are shadowed by another variable declaration.

[statement.let.constraint]

If an `else` block is not present, the pattern must be irrefutable. If an
`else` block is present, the pattern may be refutable.

[statement.let.behavior]

If the pattern does not match (this requires it to be refutable), the `else`
block is executed. The `else` block must always diverge (evaluate to the never
type).

    
    
    #![allow(unused)]
    fn main() {
    let (mut v, w) = (vec![1, 2, 3], 42); // The bindings may be mut or const
    let Some(t) = v.pop() else { // Refutable patterns require an else block
        panic!(); // The else block must diverge
    };
    let [u, v] = [v[0], v[1]] else { // This pattern is irrefutable, so the compiler
                                     // will lint as the else block is redundant.
        panic!();
    };
    }

[statement.expr]

## Expression statements

[statement.expr.syntax]

**Syntax**  
ExpressionStatement →  
ExpressionWithoutBlock ;  
| ExpressionWithBlock ;?

Show Railroad

ExpressionStatement ExpressionWithoutBlock ; ExpressionWithBlock ;

[statement.expr.intro]

An _expression statement_ is one that evaluates an expression and ignores its
result. As a rule, an expression statement’s purpose is to trigger the effects
of evaluating its expression.

[statement.expr.restriction-semicolon]

An expression that consists of only a block expression or control flow
expression, if used in a context where a statement is permitted, can omit the
trailing semicolon. This can cause an ambiguity between it being parsed as a
standalone statement and as a part of another expression; in this case, it is
parsed as a statement.

[statement.expr.constraint-block]

The type of ExpressionWithBlock expressions when used as statements must be
the unit type.

    
    
    #![allow(unused)]
    fn main() {
    let mut v = vec![1, 2, 3];
    v.pop();          // Ignore the element returned from pop
    if v.is_empty() {
        v.push(5);
    } else {
        v.remove(0);
    }                 // Semicolon can be omitted.
    [1];              // Separate expression statement, not an indexing expression.
    }

When the trailing semicolon is omitted, the result must be type `()`.

    
    
    #![allow(unused)]
    fn main() {
    // bad: the block's type is i32, not ()
    // Error: expected `()` because of default return type
    // if true {
    //   1
    // }
    
    // good: the block's type is i32
    if true {
      1
    } else {
      2
    };
    }

[statement.attribute]

## Attributes on statements

Statements accept outer attributes. The attributes that have meaning on a
statement are `cfg`, and the lint check attributes.

[expr]

# Expressions

[expr.syntax]

**Syntax**  
Expression →  
ExpressionWithoutBlock  
| ExpressionWithBlock

ExpressionWithoutBlock →  
OuterAttribute*  
(  
LiteralExpression  
| PathExpression  
| OperatorExpression  
| GroupedExpression  
| ArrayExpression  
| AwaitExpression  
| IndexExpression  
| TupleExpression  
| TupleIndexingExpression  
| StructExpression  
| CallExpression  
| MethodCallExpression  
| FieldExpression  
| ClosureExpression  
| AsyncBlockExpression  
| ContinueExpression  
| BreakExpression  
| RangeExpression  
| ReturnExpression  
| UnderscoreExpression  
| MacroInvocation  
)

ExpressionWithBlock →  
OuterAttribute*  
(  
BlockExpression  
| ConstBlockExpression  
| UnsafeBlockExpression  
| LoopExpression  
| IfExpression  
| MatchExpression  
)

Show Railroad

Expression ExpressionWithoutBlock ExpressionWithBlock

ExpressionWithoutBlock OuterAttribute LiteralExpression PathExpression
OperatorExpression GroupedExpression ArrayExpression AwaitExpression
IndexExpression TupleExpression TupleIndexingExpression StructExpression
CallExpression MethodCallExpression FieldExpression ClosureExpression
AsyncBlockExpression ContinueExpression BreakExpression RangeExpression
ReturnExpression UnderscoreExpression MacroInvocation

ExpressionWithBlock OuterAttribute BlockExpression ConstBlockExpression
UnsafeBlockExpression LoopExpression IfExpression MatchExpression

[expr.intro]

An expression may have two roles: it always produces a _value_ , and it may
have _effects_ (otherwise known as “side effects”).

[expr.evaluation]

An expression _evaluates to_ a value, and has effects during _evaluation_.

[expr.operands]

Many expressions contain sub-expressions, called the _operands_ of the
expression.

[expr.behavior]

The meaning of each kind of expression dictates several things:

  * Whether or not to evaluate the operands when evaluating the expression
  * The order in which to evaluate the operands
  * How to combine the operands’ values to obtain the value of the expression

[expr.structure]

In this way, the structure of expressions dictates the structure of execution.
Blocks are just another kind of expression, so blocks, statements,
expressions, and blocks again can recursively nest inside each other to an
arbitrary depth.

> Note
>
> We give names to the operands of expressions so that we may discuss them,
> but these names are not stable and may be changed.

[expr.precedence]

## Expression precedence

The precedence of Rust operators and expressions is ordered as follows, going
from strong to weak. Binary Operators at the same precedence level are grouped
in the order given by their associativity.

Operator/Expression| Associativity  
---|---  
Paths|  
Method calls|  
Field expressions| left to right  
Function calls, array indexing|  
`?`|  
Unary `-` `!` `*` borrow|  
`as`| left to right  
`*` `/` `%`| left to right  
`+` `-`| left to right  
`<<` `>>`| left to right  
`&`| left to right  
`^`| left to right  
`|`| left to right  
`==` `!=` `<` `>` `<=` `>=`| Require parentheses  
`&&`| left to right  
`||`| left to right  
`..` `..=`| Require parentheses  
`=` `+=` `-=` `*=` `/=` `%=`  
`&=` `|=` `^=` `<<=` `>>=`| right to left  
`return` `break` closures|  
  
[expr.operand-order]

## Evaluation order of operands

[expr.operand-order.default]

The following list of expressions all evaluate their operands the same way, as
described after the list. Other expressions either don’t take operands or
evaluate them conditionally as described on their respective pages.

  * Dereference expression
  * Error propagation expression
  * Negation expression
  * Arithmetic and logical binary operators
  * Comparison operators
  * Type cast expression
  * Grouped expression
  * Array expression
  * Await expression
  * Index expression
  * Tuple expression
  * Tuple index expression
  * Struct expression
  * Call expression
  * Method call expression
  * Field expression
  * Break expression
  * Range expression
  * Return expression

[expr.operand-order.operands-before-primary]

The operands of these expressions are evaluated prior to applying the effects
of the expression. Expressions taking multiple operands are evaluated left to
right as written in the source code.

> Note
>
> Which subexpressions are the operands of an expression is determined by
> expression precedence as per the previous section.

For example, the two `next` method calls will always be called in the same
order:

    
    
    #![allow(unused)]
    fn main() {
    // Using vec instead of array to avoid references
    // since there is no stable owned array iterator
    // at the time this example was written.
    let mut one_two = vec![1, 2].into_iter();
    assert_eq!(
        (1, 2),
        (one_two.next().unwrap(), one_two.next().unwrap())
    );
    }

> Note
>
> Since this is applied recursively, these expressions are also evaluated from
> innermost to outermost, ignoring siblings until there are no inner
> subexpressions.

[expr.place-value]

## Place expressions and value expressions

[expr.place-value.intro]

Expressions are divided into two main categories: place expressions and value
expressions; there is also a third, minor category of expressions called
assignee expressions. Within each expression, operands may likewise occur in
either place context or value context. The evaluation of an expression depends
both on its own category and the context it occurs within.

[expr.place-value.place-memory-location]

A _place expression_ is an expression that represents a memory location.

[expr.place-value.place-expr-kinds]

These expressions are paths which refer to local variables, static variables,
dereferences (`*expr`), array indexing expressions (`expr[expr]`), field
references (`expr.f`) and parenthesized place expressions.

[expr.place-value.value-expr-kinds]

All other expressions are value expressions.

[expr.place-value.value-result]

A _value expression_ is an expression that represents an actual value.

[expr.place-value.place-context]

The following contexts are _place expression_ contexts:

  * The left operand of a compound assignment expression.
  * The operand of a unary borrow, raw borrow or dereference operator.
  * The operand of a field expression.
  * The indexed operand of an array indexing expression.
  * The operand of any implicit borrow.
  * The initializer of a let statement.
  * The scrutinee of an `if let`, `match`, or `while let` expression.
  * The base of a functional update struct expression.

> Note
>
> Historically, place expressions were called _lvalues_ and value expressions
> were called _rvalues_.

[expr.place-value.assignee]

An _assignee expression_ is an expression that appears in the left operand of
an assignment expression. Explicitly, the assignee expressions are:

  * Place expressions.
  * Underscores.
  * Tuples of assignee expressions.
  * Slices of assignee expressions.
  * Tuple structs of assignee expressions.
  * Structs of assignee expressions (with optionally named fields).
  * Unit structs

[expr.place-value.parenthesis]

Arbitrary parenthesisation is permitted inside assignee expressions.

[expr.move]

### Moved and copied types

[expr.move.intro]

When a place expression is evaluated in a value expression context, or is
bound by value in a pattern, it denotes the value held _in_ that memory
location.

[expr.move.copy]

If the type of that value implements `Copy`, then the value will be copied.

[expr.move.requires-sized]

In the remaining situations, if that type is `Sized`, then it may be possible
to move the value.

[expr.move.movable-place]

Only the following place expressions may be moved out of:

  * Variables which are not currently borrowed.
  * Temporary values.
  * Fields of a place expression which can be moved out of and don’t implement `Drop`.
  * The result of dereferencing an expression with type [`Box<T>`](../alloc/boxed/struct.Box.html) and that can also be moved out of.

[expr.move.deinitialization]

After moving out of a place expression that evaluates to a local variable, the
location is deinitialized and cannot be read from again until it is
reinitialized.

[expr.move.place-invalid]

In all other cases, trying to use a place expression in a value expression
context is an error.

[expr.mut]

### Mutability

[expr.mut.intro]

For a place expression to be assigned to, mutably borrowed, implicitly mutably
borrowed, or bound to a pattern containing `ref mut`, it must be _mutable_. We
call these _mutable place expressions_. In contrast, other place expressions
are called _immutable place expressions_.

[expr.mut.valid-places]

The following expressions can be mutable place expression contexts:

  * Mutable variables which are not currently borrowed.
  * Mutable `static` items.
  * Temporary values.
  * Fields: this evaluates the subexpression in a mutable place expression context.
  * Dereferences of a `*mut T` pointer.
  * Dereference of a variable, or field of a variable, with type `&mut T`. Note: This is an exception to the requirement of the next rule.
  * Dereferences of a type that implements `DerefMut`: this then requires that the value being dereferenced is evaluated in a mutable place expression context.
  * Array indexing of a type that implements `IndexMut`: this then evaluates the value being indexed, but not the index, in mutable place expression context.

[expr.temporary]

### Temporaries

When using a value expression in most place expression contexts, a temporary
unnamed memory location is created and initialized to that value. The
expression evaluates to that location instead, except if promoted to a
`static`. The drop scope of the temporary is usually the end of the enclosing
statement.

[expr.super-macros]

### Super macros

[expr.super-macros.intro]

Certain built-in macros may create temporaries whose scopes may be extended.
These temporaries are _super temporaries_ and these macros are _super macros_.
Invocations of these macros are _super macro call expressions_. Arguments to
these macros may be _super operands_.

> Note
>
> When a super macro call expression is an extending expression, its super
> operands are extending expressions and the scopes of the super temporaries
> are extended. See destructors.scope.lifetime-extension.exprs.

[expr.super-macros.format_args]

#### `format_args!`

[expr.super-macros.format_args.super-operands]

Except for the format string argument, all arguments passed to
[`format_args!`](../core/macro.format_args.html) are _super operands_.

    
    
    #![allow(unused)]
    fn main() {
    fn temp() -> String { String::from("") }
    // Due to the call being an extending expression and the argument
    // being a super operand, the inner block is an extending expression,
    // so the scope of the temporary created in its trailing expression
    // is extended.
    let _ = format_args!("{}", { &temp() }); // OK
    }

[expr.super-macros.format_args.super-temporaries]

The super operands of [`format_args!`](../core/macro.format_args.html) are
implicitly borrowed and are therefore place expression contexts. When a value
expression is passed as an argument, it creates a _super temporary_.

    
    
    #![allow(unused)]
    fn main() {
    fn temp() -> String { String::from("") }
    let x = format_args!("{}", temp());
    x; // <-- The temporary is extended, allowing use here.
    }

The expansion of a call to [`format_args!`](../core/macro.format_args.html)
sometimes creates other internal _super temporaries_.

    
    
    #![allow(unused)]
    fn main() {
    let x = {
        // This call creates an internal temporary.
        let x = format_args!("{:?}", 0);
        x // <-- The temporary is extended, allowing its use here.
    }; // <-- The temporary is dropped here.
    x; // ERROR
    }
    
    
    #![allow(unused)]
    fn main() {
    // This call doesn't create an internal temporary.
    let x = { let x = format_args!("{}", 0); x };
    x; // OK
    }

> Note
>
> The details of when [`format_args!`](../core/macro.format_args.html) does or
> does not create internal temporaries are currently unspecified.

[expr.super-macros.pin]

#### `pin!`

[expr.super-macros.pin.super-operands]

The argument to [`pin!`](../core/pin/macro.pin.html) is a _super operand_.

    
    
    #![allow(unused)]
    fn main() {
    use core::pin::pin;
    fn temp() {}
    // As above for `format_args!`.
    let _ = pin!({ &temp() }); // OK
    }

[expr.super-macros.pin.super-temporaries]

The argument to [`pin!`](../core/pin/macro.pin.html) is a value expression
context and creates a _super temporary_.

    
    
    #![allow(unused)]
    fn main() {
    use core::pin::pin;
    fn temp() {}
    // The argument is evaluated into a super temporary.
    let x = pin!(temp());
    // The temporary is extended, allowing its use here.
    x; // OK
    }

[expr.implicit-borrow]

### Implicit borrows

[expr.implicit-borrow-intro]

Certain expressions will treat an expression as a place expression by
implicitly borrowing it. For example, it is possible to compare two unsized
slices for equality directly, because the `==` operator implicitly borrows its
operands:

    
    
    #![allow(unused)]
    fn main() {
    let c = [1, 2, 3];
    let d = vec![1, 2, 3];
    let a: &[i32];
    let b: &[i32];
    a = &c;
    b = &d;
    // ...
    *a == *b;
    // Equivalent form:
    ::std::cmp::PartialEq::eq(&*a, &*b);
    }

[expr.implicit-borrow.application]

Implicit borrows may be taken in the following expressions:

  * Left operand in method-call expressions.
  * Left operand in field expressions.
  * Left operand in call expressions.
  * Left operand in array indexing expressions.
  * Operand of the dereference operator (`*`).
  * Operands of comparison.
  * Left operands of the compound assignment.
  * Arguments to [`format_args!`](../core/macro.format_args.html) except the format string.

[expr.overload]

## Overloading traits

Many of the following operators and expressions can also be overloaded for
other types using traits in `std::ops` or `std::cmp`. These traits also exist
in `core::ops` and `core::cmp` with the same names.

[expr.attr]

## Expression attributes

[expr.attr.restriction]

Outer attributes before an expression are allowed only in a few specific
cases:

  * Before an expression used as a statement.
  * Elements of array expressions, tuple expressions, call expressions, and tuple-style struct expressions.
  * The tail expression of block expressions.

[expr.attr.never-before]

They are never allowed before:

  * Range expressions.
  * Binary operator expressions (ArithmeticOrLogicalExpression, ComparisonExpression, LazyBooleanExpression, TypeCastExpression, AssignmentExpression, CompoundAssignmentExpression).

[expr.literal]

# Literal expressions

[expr.literal.syntax]

**Syntax**  
LiteralExpression →  
CHAR_LITERAL  
| STRING_LITERAL  
| RAW_STRING_LITERAL  
| BYTE_LITERAL  
| BYTE_STRING_LITERAL  
| RAW_BYTE_STRING_LITERAL  
| C_STRING_LITERAL  
| RAW_C_STRING_LITERAL  
| INTEGER_LITERAL  
| FLOAT_LITERAL  
| true  
| false

Show Railroad

LiteralExpression CHAR_LITERAL STRING_LITERAL RAW_STRING_LITERAL BYTE_LITERAL
BYTE_STRING_LITERAL RAW_BYTE_STRING_LITERAL C_STRING_LITERAL
RAW_C_STRING_LITERAL INTEGER_LITERAL FLOAT_LITERAL true false

[expr.literal.intro]

A _literal expression_ is an expression consisting of a single token, rather
than a sequence of tokens, that immediately and directly denotes the value it
evaluates to, rather than referring to it by name or some other evaluation
rule.

[expr.literal.const-expr]

A literal is a form of constant expression, so is evaluated (primarily) at
compile time.

[expr.literal.literal-token]

Each of the lexical literal forms described earlier can make up a literal
expression, as can the keywords `true` and `false`.

    
    
    #![allow(unused)]
    fn main() {
    "hello";   // string type
    '5';       // character type
    5;         // integer type
    }

[expr.literal.string-representation]

In the descriptions below, the _string representation_ of a token is the
sequence of characters from the input which matched the token’s production in
a _Lexer_ grammar snippet.

> Note
>
> This string representation never includes a character `U+000D` (CR)
> immediately followed by `U+000A` (LF): this pair would have been previously
> transformed into a single `U+000A` (LF).

[expr.literal.escape]

## Escapes

[expr.literal.escape.intro]

The descriptions of textual literal expressions below make use of several
forms of _escape_.

[expr.literal.escape.sequence]

Each form of escape is characterised by:

  * an _escape sequence_ : a sequence of characters, which always begins with `U+005C` (`\`)
  * an _escaped value_ : either a single character or an empty sequence of characters

In the definitions of escapes below:

  * An _octal digit_ is any of the characters in the range [`0`-`7`].
  * A _hexadecimal digit_ is any of the characters in the ranges [`0`-`9`], [`a`-`f`], or [`A`-`F`].

[expr.literal.escape.simple]

### Simple escapes

Each sequence of characters occurring in the first column of the following
table is an escape sequence.

In each case, the escaped value is the character given in the corresponding
entry in the second column.

Escape sequence| Escaped value  
---|---  
`\0`| U+0000 (NUL)  
`\t`| U+0009 (HT)  
`\n`| U+000A (LF)  
`\r`| U+000D (CR)  
`\"`| U+0022 (QUOTATION MARK)  
`\'`| U+0027 (APOSTROPHE)  
`\\`| U+005C (REVERSE SOLIDUS)  
  
[expr.literal.escape.hex-octet]

### 8-bit escapes

The escape sequence consists of `\x` followed by two hexadecimal digits.

The escaped value is the character whose [Unicode scalar
value](http://www.unicode.org/glossary/#unicode_scalar_value) is the result of
interpreting the final two characters in the escape sequence as a hexadecimal
integer, as if by
[`u8::from_str_radix`](../std/primitive.u8.html#method.from_str_radix) with
radix 16.

> Note
>
> The escaped value therefore has a [Unicode scalar
> value](http://www.unicode.org/glossary/#unicode_scalar_value) in the range
> of `u8`.

[expr.literal.escape.hex-ascii]

### 7-bit escapes

The escape sequence consists of `\x` followed by an octal digit then a
hexadecimal digit.

The escaped value is the character whose [Unicode scalar
value](http://www.unicode.org/glossary/#unicode_scalar_value) is the result of
interpreting the final two characters in the escape sequence as a hexadecimal
integer, as if by
[`u8::from_str_radix`](../std/primitive.u8.html#method.from_str_radix) with
radix 16.

[expr.literal.escape.unicode]

### Unicode escapes

The escape sequence consists of `\u{`, followed by a sequence of characters
each of which is a hexadecimal digit or `_`, followed by `}`.

The escaped value is the character whose [Unicode scalar
value](http://www.unicode.org/glossary/#unicode_scalar_value) is the result of
interpreting the hexadecimal digits contained in the escape sequence as a
hexadecimal integer, as if by
[`u32::from_str_radix`](../std/primitive.u32.html#method.from_str_radix) with
radix 16.

> Note
>
> The permitted forms of a CHAR_LITERAL or STRING_LITERAL token ensure that
> there is such a character.

[expr.literal.continuation]

### String continuation escapes

The escape sequence consists of `\` followed immediately by `U+000A` (LF), and
all following whitespace characters before the next non-whitespace character.
For this purpose, the whitespace characters are `U+0009` (HT), `U+000A` (LF),
`U+000D` (CR), and `U+0020` (SPACE).

The escaped value is an empty sequence of characters.

> Note
>
> The effect of this form of escape is that a string continuation skips
> following whitespace, including additional newlines. Thus `a`, `b` and `c`
> are equal:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     let a = "foobar";
>     let b = "foo\
>              bar";
>     let c = "foo\
>  
>          bar";
>  
>     assert_eq!(a, b);
>     assert_eq!(b, c);
>     }
>
> Skipping additional newlines (as in example c) is potentially confusing and
> unexpected. This behavior may be adjusted in the future. Until a decision is
> made, it is recommended to avoid relying on skipping multiple newlines with
> line continuations. See [this issue](https://github.com/rust-
> lang/reference/pull/1042) for more information.

[expr.literal.char]

## Character literal expressions

[expr.literal.char.intro]

A character literal expression consists of a single CHAR_LITERAL token.

[expr.literal.char.type]

The expression’s type is the primitive `char` type.

[expr.literal.char.no-suffix]

The token must not have a suffix.

[expr.literal.char.literal-content]

The token’s _literal content_ is the sequence of characters following the
first `U+0027` (`'`) and preceding the last `U+0027` (`'`) in the string
representation of the token.

[expr.literal.char.represented]

The literal expression’s _represented character_ is derived from the literal
content as follows:

[expr.literal.char.escape]

  * If the literal content is one of the following forms of escape sequence, the represented character is the escape sequence’s escaped value: 
    * Simple escapes
    * 7-bit escapes
    * Unicode escapes

[expr.literal.char.single]

  * Otherwise the represented character is the single character that makes up the literal content.

[expr.literal.char.result]

The expression’s value is the `char` corresponding to the represented
character’s [Unicode scalar
value](http://www.unicode.org/glossary/#unicode_scalar_value).

> Note
>
> The permitted forms of a CHAR_LITERAL token ensure that these rules always
> produce a single character.

Examples of character literal expressions:

    
    
    #![allow(unused)]
    fn main() {
    'R';                               // R
    '\'';                              // '
    '\x52';                            // R
    '\u{00E6}';                        // LATIN SMALL LETTER AE (U+00E6)
    }

[expr.literal.string]

## String literal expressions

[expr.literal.string.intro]

A string literal expression consists of a single STRING_LITERAL or
RAW_STRING_LITERAL token.

[expr.literal.string.type]

The expression’s type is a shared reference (with `static` lifetime) to the
primitive `str` type. That is, the type is `&'static str`.

[expr.literal.string.no-suffix]

The token must not have a suffix.

[expr.literal.string.literal-content]

The token’s _literal content_ is the sequence of characters following the
first `U+0022` (`"`) and preceding the last `U+0022` (`"`) in the string
representation of the token.

[expr.literal.string.represented]

The literal expression’s _represented string_ is a sequence of characters
derived from the literal content as follows:

[expr.literal.string.escape]

  * If the token is a STRING_LITERAL, each escape sequence of any of the following forms occurring in the literal content is replaced by the escape sequence’s escaped value.

    * Simple escapes
    * 7-bit escapes
    * Unicode escapes
    * String continuation escapes

These replacements take place in left-to-right order. For example, the token
`"\\x41"` is converted to the characters `\` `x` `4` `1`.

[expr.literal.string.raw]

  * If the token is a RAW_STRING_LITERAL, the represented string is identical to the literal content.

[expr.literal.string.result]

The expression’s value is a reference to a statically allocated `str`
containing the UTF-8 encoding of the represented string.

Examples of string literal expressions:

    
    
    #![allow(unused)]
    fn main() {
    "foo"; r"foo";                     // foo
    "\"foo\""; r#""foo""#;             // "foo"
    
    "foo #\"# bar";
    r##"foo #"# bar"##;                // foo #"# bar
    
    "\x52"; "R"; r"R";                 // R
    "\\x52"; r"\x52";                  // \x52
    }

[expr.literal.byte-char]

## Byte literal expressions

[expr.literal.byte-char.intro]

A byte literal expression consists of a single BYTE_LITERAL token.

[expr.literal.byte-char.literal]

The expression’s type is the primitive `u8` type.

[expr.literal.byte-char.no-suffix]

The token must not have a suffix.

[expr.literal.byte-char.literal-content]

The token’s _literal content_ is the sequence of characters following the
first `U+0027` (`'`) and preceding the last `U+0027` (`'`) in the string
representation of the token.

[expr.literal.byte-char.represented]

The literal expression’s _represented character_ is derived from the literal
content as follows:

[expr.literal.byte-char.escape]

  * If the literal content is one of the following forms of escape sequence, the represented character is the escape sequence’s escaped value: 
    * Simple escapes
    * 8-bit escapes

[expr.literal.byte-char.single]

  * Otherwise the represented character is the single character that makes up the literal content.

[expr.literal.byte-char.result]

The expression’s value is the represented character’s [Unicode scalar
value](http://www.unicode.org/glossary/#unicode_scalar_value).

> Note
>
> The permitted forms of a BYTE_LITERAL token ensure that these rules always
> produce a single character, whose Unicode scalar value is in the range of
> `u8`.

Examples of byte literal expressions:

    
    
    #![allow(unused)]
    fn main() {
    b'R';                              // 82
    b'\'';                             // 39
    b'\x52';                           // 82
    b'\xA0';                           // 160
    }

[expr.literal.byte-string]

## Byte string literal expressions

[expr.literal.byte-string.intro]

A byte string literal expression consists of a single BYTE_STRING_LITERAL or
RAW_BYTE_STRING_LITERAL token.

[expr.literal.byte-string.type]

The expression’s type is a shared reference (with `static` lifetime) to an
array whose element type is `u8`. That is, the type is `&'static [u8; N]`,
where `N` is the number of bytes in the represented string described below.

[expr.literal.byte-string.no-suffix]

The token must not have a suffix.

[expr.literal.byte-string.literal-content]

The token’s _literal content_ is the sequence of characters following the
first `U+0022` (`"`) and preceding the last `U+0022` (`"`) in the string
representation of the token.

[expr.literal.byte-string.represented]

The literal expression’s _represented string_ is a sequence of characters
derived from the literal content as follows:

[expr.literal.byte-string.escape]

  * If the token is a BYTE_STRING_LITERAL, each escape sequence of any of the following forms occurring in the literal content is replaced by the escape sequence’s escaped value.

    * Simple escapes
    * 8-bit escapes
    * String continuation escapes

These replacements take place in left-to-right order. For example, the token
`b"\\x41"` is converted to the characters `\` `x` `4` `1`.

[expr.literal.byte-string.raw]

  * If the token is a RAW_BYTE_STRING_LITERAL, the represented string is identical to the literal content.

[expr.literal.byte-string.result]

The expression’s value is a reference to a statically allocated array
containing the [Unicode scalar
values](http://www.unicode.org/glossary/#unicode_scalar_value) of the
characters in the represented string, in the same order.

> Note
>
> The permitted forms of BYTE_STRING_LITERAL and RAW_BYTE_STRING_LITERAL
> tokens ensure that these rules always produce array element values in the
> range of `u8`.

Examples of byte string literal expressions:

    
    
    #![allow(unused)]
    fn main() {
    b"foo"; br"foo";                     // foo
    b"\"foo\""; br#""foo""#;             // "foo"
    
    b"foo #\"# bar";
    br##"foo #"# bar"##;                 // foo #"# bar
    
    b"\x52"; b"R"; br"R";                // R
    b"\\x52"; br"\x52";                  // \x52
    }

[expr.literal.c-string]

## C string literal expressions

[expr.literal.c-string.intro]

A C string literal expression consists of a single C_STRING_LITERAL or
RAW_C_STRING_LITERAL token.

[expr.literal.c-string.type]

The expression’s type is a shared reference (with `static` lifetime) to the
standard library [CStr](../core/ffi/c_str/struct.CStr.html) type. That is, the
type is `&'static core::ffi::CStr`.

[expr.literal.c-string.no-suffix]

The token must not have a suffix.

[expr.literal.c-string.literal-content]

The token’s _literal content_ is the sequence of characters following the
first `"` and preceding the last `"` in the string representation of the
token.

[expr.literal.c-string.represented]

The literal expression’s _represented bytes_ are a sequence of bytes derived
from the literal content as follows:

[expr.literal.c-string.escape]

  * If the token is a C_STRING_LITERAL, the literal content is treated as a sequence of items, each of which is either a single Unicode character other than `\` or an escape. The sequence of items is converted to a sequence of bytes as follows: 
    * Each single Unicode character contributes its UTF-8 representation.
    * Each simple escape contributes the [Unicode scalar value](http://www.unicode.org/glossary/#unicode_scalar_value) of its escaped value.
    * Each 8-bit escape contributes a single byte containing the [Unicode scalar value](http://www.unicode.org/glossary/#unicode_scalar_value) of its escaped value.
    * Each unicode escape contributes the UTF-8 representation of its escaped value.
    * Each string continuation escape contributes no bytes.

[expr.literal.c-string.raw]

  * If the token is a RAW_C_STRING_LITERAL, the represented bytes are the UTF-8 encoding of the literal content.

> Note
>
> The permitted forms of C_STRING_LITERAL and RAW_C_STRING_LITERAL tokens
> ensure that the represented bytes never include a null byte.

[expr.literal.c-string.result]

The expression’s value is a reference to a statically allocated
[CStr](../core/ffi/c_str/struct.CStr.html) whose array of bytes contains the
represented bytes followed by a null byte.

Examples of C string literal expressions:

    
    
    #![allow(unused)]
    fn main() {
    c"foo"; cr"foo";                     // foo
    c"\"foo\""; cr#""foo""#;             // "foo"
    
    c"foo #\"# bar";
    cr##"foo #"# bar"##;                 // foo #"# bar
    
    c"\x52"; c"R"; cr"R";                // R
    c"\\x52"; cr"\x52";                  // \x52
    
    c"æ";                                // LATIN SMALL LETTER AE (U+00E6)
    c"\u{00E6}";                         // LATIN SMALL LETTER AE (U+00E6)
    c"\xC3\xA6";                         // LATIN SMALL LETTER AE (U+00E6)
    
    c"\xE6".to_bytes();                  // [230]
    c"\u{00E6}".to_bytes();              // [195, 166]
    }

[expr.literal.int]

## Integer literal expressions

[expr.literal.int.intro]

An integer literal expression consists of a single INTEGER_LITERAL token.

[expr.literal.int.suffix]

If the token has a suffix, the suffix must be the name of one of the primitive
integer types: `u8`, `i8`, `u16`, `i16`, `u32`, `i32`, `u64`, `i64`, `u128`,
`i128`, `usize`, or `isize`, and the expression has that type.

[expr.literal.int.infer]

If the token has no suffix, the expression’s type is determined by type
inference:

[expr.literal.int.inference-unique-type]

  * If an integer type can be _uniquely_ determined from the surrounding program context, the expression has that type.

[expr.literal.int.inference-default]

  * If the program context under-constrains the type, it defaults to the signed 32-bit integer `i32`.

[expr.literal.int.inference-error]

  * If the program context over-constrains the type, it is considered a static type error.

Examples of integer literal expressions:

    
    
    #![allow(unused)]
    fn main() {
    123;                               // type i32
    123i32;                            // type i32
    123u32;                            // type u32
    123_u32;                           // type u32
    let a: u64 = 123;                  // type u64
    
    0xff;                              // type i32
    0xff_u8;                           // type u8
    
    0o70;                              // type i32
    0o70_i16;                          // type i16
    
    0b1111_1111_1001_0000;             // type i32
    0b1111_1111_1001_0000i64;          // type i64
    
    0usize;                            // type usize
    }

[expr.literal.int.representation]

The value of the expression is determined from the string representation of
the token as follows:

[expr.literal.int.radix]

  * An integer radix is chosen by inspecting the first two characters of the string, as follows:

    * `0b` indicates radix 2
    * `0o` indicates radix 8
    * `0x` indicates radix 16
    * otherwise the radix is 10.

[expr.literal.int.radix-prefix-stripped]

  * If the radix is not 10, the first two characters are removed from the string.

[expr.literal.int.type-suffix-stripped]

  * Any suffix is removed from the string.

[expr.literal.int.separators-stripped]

  * Any underscores are removed from the string.

[expr.literal.int.u128-value]

  * The string is converted to a `u128` value as if by [`u128::from_str_radix`](../std/primitive.u128.html#method.from_str_radix) with the chosen radix. If the value does not fit in `u128`, it is a compiler error.

[expr.literal.int.cast]

  * The `u128` value is converted to the expression’s type via a numeric cast.

> Note
>
> The final cast will truncate the value of the literal if it does not fit in
> the expression’s type. `rustc` includes a lint check named
> `overflowing_literals`, defaulting to `deny`, which rejects expressions
> where this occurs.

> Note
>
> `-1i8`, for example, is an application of the negation operator to the
> literal expression `1i8`, not a single integer literal expression. See
> Overflow for notes on representing the most negative value for a signed
> type.

[expr.literal.float]

## Floating-point literal expressions

[expr.literal.float.intro]

A floating-point literal expression has one of two forms:

  * a single FLOAT_LITERAL token
  * a single INTEGER_LITERAL token which has a suffix and no radix indicator

[expr.literal.float.suffix]

If the token has a suffix, the suffix must be the name of one of the primitive
floating-point types: `f32` or `f64`, and the expression has that type.

[expr.literal.float.infer]

If the token has no suffix, the expression’s type is determined by type
inference:

[expr.literal.float.inference-unique-type]

  * If a floating-point type can be _uniquely_ determined from the surrounding program context, the expression has that type.

[expr.literal.float.inference-default]

  * If the program context under-constrains the type, it defaults to `f64`.

[expr.literal.float.inference-error]

  * If the program context over-constrains the type, it is considered a static type error.

Examples of floating-point literal expressions:

    
    
    #![allow(unused)]
    fn main() {
    123.0f64;        // type f64
    0.1f64;          // type f64
    0.1f32;          // type f32
    12E+99_f64;      // type f64
    5f32;            // type f32
    let x: f64 = 2.; // type f64
    }

[expr.literal.float.result]

The value of the expression is determined from the string representation of
the token as follows:

[expr.literal.float.type-suffix-stripped]

  * Any suffix is removed from the string.

[expr.literal.float.separators-stripped]

  * Any underscores are removed from the string.

[expr.literal.float.value]

  * The string is converted to the expression’s type as if by [`f32::from_str`](../core/primitive.f32.html#method.from_str) or [`f64::from_str`](../core/primitive.f64.html#method.from_str).

> Note
>
> `-1.0`, for example, is an application of the negation operator to the
> literal expression `1.0`, not a single floating-point literal expression.

> Note
>
> `inf` and `NaN` are not literal tokens. The
> [`f32::INFINITY`](../std/primitive.f32.html#associatedconstant.INFINITY),
> [`f64::INFINITY`](../std/primitive.f64.html#associatedconstant.INFINITY),
> [`f32::NAN`](../std/primitive.f32.html#associatedconstant.NAN), and
> [`f64::NAN`](../std/primitive.f64.html#associatedconstant.NAN) constants can
> be used instead of literal expressions. In `rustc`, a literal large enough
> to be evaluated as infinite will trigger the `overflowing_literals` lint
> check.

[expr.literal.bool]

## Boolean literal expressions

[expr.literal.bool.intro]

A boolean literal expression consists of one of the keywords `true` or
`false`.

[expr.literal.bool.result]

The expression’s type is the primitive boolean type, and its value is:

  * true if the keyword is `true`
  * false if the keyword is `false`

[expr.path]

# Path expressions

[expr.path.syntax]

**Syntax**  
PathExpression →  
PathInExpression  
| QualifiedPathInExpression

Show Railroad

PathExpression PathInExpression QualifiedPathInExpression

[expr.path.intro]

A path used as an expression context denotes either a local variable or an
item.

[expr.path.place]

Path expressions that resolve to local or static variables are place
expressions; other paths are value expressions.

[expr.path.safety]

Using a `static mut` variable requires an `unsafe` block.

    
    
    #![allow(unused)]
    fn main() {
    mod globals {
        pub static STATIC_VAR: i32 = 5;
        pub static mut STATIC_MUT_VAR: i32 = 7;
    }
    let local_var = 3;
    local_var;
    globals::STATIC_VAR;
    unsafe { globals::STATIC_MUT_VAR };
    let some_constructor = Some::<i32>;
    let push_integer = Vec::<i32>::push;
    let slice_reverse = <[i32]>::reverse;
    }

[expr.path.const]

Evaluation of associated constants is handled the same way as `const` blocks.

[expr.block]

# Block expressions

[expr.block.syntax]

**Syntax**  
BlockExpression →  
{  
InnerAttribute*  
Statements?  
}

Statements →  
Statement+  
| Statement+ ExpressionWithoutBlock  
| ExpressionWithoutBlock

Show Railroad

BlockExpression { InnerAttribute Statements }

Statements Statement Statement ExpressionWithoutBlock ExpressionWithoutBlock

[expr.block.intro]

A _block expression_ , or _block_ , is a control flow expression and anonymous
namespace scope for items and variable declarations.

[expr.block.sequential-evaluation]

As a control flow expression, a block sequentially executes its component non-
item declaration statements and then its final optional expression.

[expr.block.namespace]

As an anonymous namespace scope, item declarations are only in scope inside
the block itself and variables declared by `let` statements are in scope from
the next statement until the end of the block. See the scopes chapter for more
details.

[expr.block.inner-attributes]

The syntax for a block is `{`, then any inner attributes, then any number of
statements, then an optional expression, called the final operand, and finally
a `}`.

[expr.block.statements]

Statements are usually required to be followed by a semicolon, with two
exceptions:

  1. Item declaration statements do not need to be followed by a semicolon.
  2. Expression statements usually require a following semicolon except if its outer expression is a flow control expression.

[expr.block.null-statement]

Furthermore, extra semicolons between statements are allowed, but these
semicolons do not affect semantics.

[expr.block.evaluation]

When evaluating a block expression, each statement, except for item
declaration statements, is executed sequentially.

[expr.block.result]

Then the final operand is executed, if given.

[expr.block.type]

The type of a block is the type of the final operand, or `()` if the final
operand is omitted.

    
    
    #![allow(unused)]
    fn main() {
    fn fn_call() {}
    let _: () = {
        fn_call();
    };
    
    let five: i32 = {
        fn_call();
        5
    };
    
    assert_eq!(5, five);
    }

> Note
>
> As a control flow expression, if a block expression is the outer expression
> of an expression statement, the expected type is `()` unless it is followed
> immediately by a semicolon.

[expr.block.value]

Blocks are always value expressions and evaluate the last operand in value
expression context.

> Note
>
> This can be used to force moving a value if really needed. For example, the
> following example fails on the call to `consume_self` because the struct was
> moved out of `s` in the block expression.
>  
>  
>     #![allow(unused)]
>     fn main() {
>     struct Struct;
>  
>     impl Struct {
>         fn consume_self(self) {}
>         fn borrow_self(&self) {}
>     }
>  
>     fn move_by_block_expression() {
>         let s = Struct;
>  
>         // Move the value out of `s` in the block expression.
>         (&{ s }).borrow_self();
>  
>         // Fails to execute because `s` is moved out of.
>         s.consume_self();
>     }
>     }

[expr.block.async]

## `async` blocks

[expr.block.async.syntax]

**Syntax**  
AsyncBlockExpression → async move? BlockExpression

Show Railroad

AsyncBlockExpression async move BlockExpression

[expr.block.async.intro]

An _async block_ is a variant of a block expression which evaluates to a
future.

[expr.block.async.future-result]

The final expression of the block, if present, determines the result value of
the future.

[expr.block.async.anonymous-type]

Executing an async block is similar to executing a closure expression: its
immediate effect is to produce and return an anonymous type.

[expr.block.async.future]

Whereas closures return a type that implements one or more of the
[`std::ops::Fn`](../core/ops/function/trait.Fn.html) traits, however, the type
returned for an async block implements the
[`std::future::Future`](../core/future/future/trait.Future.html) trait.

[expr.block.async.layout-unspecified]

The actual data format for this type is unspecified.

> Note
>
> The future type that rustc generates is roughly equivalent to an enum with
> one variant per `await` point, where each variant stores the data needed to
> resume from its corresponding point.

[expr.block.async.edition2018]

> 2018 Edition differences
>
> Async blocks are only available beginning with Rust 2018.

[expr.block.async.capture]

### Capture modes

Async blocks capture variables from their environment using the same capture
modes as closures. Like closures, when written `async { .. }` the capture mode
for each variable will be inferred from the content of the block. `async move
{ .. }` blocks however will move all referenced variables into the resulting
future.

[expr.block.async.context]

### Async context

Because async blocks construct a future, they define an **async context**
which can in turn contain `await` expressions. Async contexts are established
by async blocks as well as the bodies of async functions, whose semantics are
defined in terms of async blocks.

[expr.block.async.function]

### Control-flow operators

[expr.block.async.function.intro]

Async blocks act like a function boundary, much like closures.

[expr.block.async.function.return-try]

Therefore, the `?` operator and `return` expressions both affect the output of
the future, not the enclosing function or other context. That is, `return
<expr>` from within an async block will return the result of `<expr>` as the
output of the future. Similarly, if `<expr>?` propagates an error, that error
is propagated as the result of the future.

[expr.block.async.function.control-flow]

Finally, the `break` and `continue` keywords cannot be used to branch out from
an async block. Therefore the following is illegal:

    
    
    #![allow(unused)]
    fn main() {
    loop {
        async move {
            break; // error[E0267]: `break` inside of an `async` block
        }
    }
    }

[expr.block.const]

## `const` blocks

[expr.block.const.syntax]

**Syntax**  
ConstBlockExpression → const BlockExpression

Show Railroad

ConstBlockExpression const BlockExpression

[expr.block.const.intro]

A _const block_ is a variant of a block expression whose body evaluates at
compile-time instead of at runtime.

[expr.block.const.context]

Const blocks allows you to define a constant value without having to define
new constant items, and thus they are also sometimes referred as _inline
consts_. It also supports type inference so there is no need to specify the
type, unlike constant items.

[expr.block.const.generic-params]

Const blocks have the ability to reference generic parameters in scope, unlike
free constant items. They are desugared to constant items with generic
parameters in scope (similar to associated constants, but without a trait or
type they are associated with). For example, this code:

    
    
    #![allow(unused)]
    fn main() {
    fn foo<T>() -> usize {
        const { std::mem::size_of::<T>() + 1 }
    }
    }

is equivalent to:

    
    
    #![allow(unused)]
    fn main() {
    fn foo<T>() -> usize {
        {
            struct Const<T>(T);
            impl<T> Const<T> {
                const CONST: usize = std::mem::size_of::<T>() + 1;
            }
            Const::<T>::CONST
        }
    }
    }

[expr.block.const.evaluation]

If the const block expression is executed at runtime, then the constant is
guaranteed to be evaluated, even if its return value is ignored:

    
    
    #![allow(unused)]
    fn main() {
    fn foo<T>() -> usize {
        // If this code ever gets executed, then the assertion has definitely
        // been evaluated at compile-time.
        const { assert!(std::mem::size_of::<T>() > 0); }
        // Here we can have unsafe code relying on the type being non-zero-sized.
        /* ... */
        42
    }
    }

[expr.block.const.not-executed]

If the const block expression is not executed at runtime, it may or may not be
evaluated:

    
    
    #![allow(unused)]
    fn main() {
    if false {
        // The panic may or may not occur when the program is built.
        const { panic!(); }
    }
    }

[expr.block.unsafe]

## `unsafe` blocks

[expr.block.unsafe.syntax]

**Syntax**  
UnsafeBlockExpression → unsafe BlockExpression

Show Railroad

UnsafeBlockExpression unsafe BlockExpression

[expr.block.unsafe.intro]

_See`unsafe` blocks for more information on when to use `unsafe`_.

A block of code can be prefixed with the `unsafe` keyword to permit unsafe
operations. Examples:

    
    
    #![allow(unused)]
    fn main() {
    unsafe {
        let b = [13u8, 17u8];
        let a = &b[0] as *const u8;
        assert_eq!(*a, 13);
        assert_eq!(*a.offset(1), 17);
    }
    
    unsafe fn an_unsafe_fn() -> i32 { 10 }
    let a = unsafe { an_unsafe_fn() };
    }

[expr.block.label]

## Labeled block expressions

Labeled block expressions are documented in the Loops and other breakable
expressions section.

[expr.block.attributes]

## Attributes on block expressions

[expr.block.attributes.inner-attributes]

Inner attributes are allowed directly after the opening brace of a block
expression in the following situations:

  * Function and method bodies.
  * Loop bodies (`loop`, `while`, and `for`).
  * Block expressions used as a statement.
  * Block expressions as elements of array expressions, tuple expressions, call expressions, and tuple-style struct expressions.
  * A block expression as the tail expression of another block expression.

[expr.block.attributes.valid]

The attributes that have meaning on a block expression are `cfg` and the lint
check attributes.

For example, this function returns `true` on unix platforms and `false` on
other platforms.

    
    
    #![allow(unused)]
    fn main() {
    fn is_unix_platform() -> bool {
        #[cfg(unix)] { true }
        #[cfg(not(unix))] { false }
    }
    }

[expr.operator]

# Operator expressions

[expr.operator.syntax]

**Syntax**  
OperatorExpression →  
BorrowExpression  
| DereferenceExpression  
| TryPropagationExpression  
| NegationExpression  
| ArithmeticOrLogicalExpression  
| ComparisonExpression  
| LazyBooleanExpression  
| TypeCastExpression  
| AssignmentExpression  
| CompoundAssignmentExpression

Show Railroad

OperatorExpression BorrowExpression DereferenceExpression
TryPropagationExpression NegationExpression ArithmeticOrLogicalExpression
ComparisonExpression LazyBooleanExpression TypeCastExpression
AssignmentExpression CompoundAssignmentExpression

[expr.operator.intro]

Operators are defined for built in types by the Rust language.

[expr.operator.trait]

Many of the following operators can also be overloaded using traits in
`std::ops` or `std::cmp`.

[expr.operator.int-overflow]

## Overflow

[expr.operator.int-overflow.intro]

Integer operators will panic when they overflow when compiled in debug mode.
The `-C debug-assertions` and `-C overflow-checks` compiler flags can be used
to control this more directly. The following things are considered to be
overflow:

[expr.operator.int-overflow.binary-arith]

  * When `+`, `*` or binary `-` create a value greater than the maximum value, or less than the minimum value that can be stored.

[expr.operator.int-overflow.unary-neg]

  * Applying unary `-` to the most negative value of any signed integer type, unless the operand is a literal expression (or a literal expression standing alone inside one or more grouped expressions).

[expr.operator.int-overflow.div]

  * Using `/` or `%`, where the left-hand argument is the smallest integer of a signed integer type and the right-hand argument is `-1`. These checks occur even when `-C overflow-checks` is disabled, for legacy reasons.

[expr.operator.int-overflow.shift]

  * Using `<<` or `>>` where the right-hand argument is greater than or equal to the number of bits in the type of the left-hand argument, or is negative.

> Note
>
> The exception for literal expressions behind unary `-` means that forms such
> as `-128_i8` or `let j: i8 = -(128)` never cause a panic and have the
> expected value of -128.
>
> In these cases, the literal expression already has the most negative value
> for its type (for example, `128_i8` has the value -128) because integer
> literals are truncated to their type per the description in Integer literal
> expressions.
>
> Negation of these most negative values leaves the value unchanged due to
> two’s complement overflow conventions.
>
> In `rustc`, these most negative expressions are also ignored by the
> `overflowing_literals` lint check.

[expr.operator.borrow]

## Borrow operators

[expr.operator.borrow.syntax]

**Syntax**  
BorrowExpression →  
( & | && ) Expression   
| ( & | && ) mut Expression   
| ( & | && ) raw const Expression   
| ( & | && ) raw mut Expression

Show Railroad

BorrowExpression & && Expression & && mut Expression & && raw const Expression
& && raw mut Expression

[expr.operator.borrow.intro]

The `&` (shared borrow) and `&mut` (mutable borrow) operators are unary prefix
operators.

[expr.operator.borrow.result]

When applied to a place expression, this expressions produces a reference
(pointer) to the location that the value refers to.

[expr.operator.borrow.lifetime]

The memory location is also placed into a borrowed state for the duration of
the reference. For a shared borrow (`&`), this implies that the place may not
be mutated, but it may be read or shared again. For a mutable borrow (`&mut`),
the place may not be accessed in any way until the borrow expires.

[expr.operator.borrow.mut]

`&mut` evaluates its operand in a mutable place expression context.

[expr.operator.borrow.temporary]

If the `&` or `&mut` operators are applied to a value expression, then a
temporary value is created.

These operators cannot be overloaded.

    
    
    #![allow(unused)]
    fn main() {
    {
        // a temporary with value 7 is created that lasts for this scope.
        let shared_reference = &7;
    }
    let mut array = [-2, 3, 9];
    {
        // Mutably borrows `array` for this scope.
        // `array` may only be used through `mutable_reference`.
        let mutable_reference = &mut array;
    }
    }

[expr.borrow.and-and-syntax]

Even though `&&` is a single token (the lazy ‘and’ operator), when used in the
context of borrow expressions it works as two borrows:

    
    
    #![allow(unused)]
    fn main() {
    // same meanings:
    let a = &&  10;
    let a = & & 10;
    
    // same meanings:
    let a = &&&&  mut 10;
    let a = && && mut 10;
    let a = & & & & mut 10;
    }

[expr.borrow.raw]

### Raw borrow operators

[expr.borrow.raw.intro]

`&raw const` and `&raw mut` are the _raw borrow operators_.

[expr.borrow.raw.place]

The operand expression of these operators is evaluated in place expression
context.

[expr.borrow.raw.result]

`&raw const expr` then creates a const raw pointer of type `*const T` to the
given place, and `&raw mut expr` creates a mutable raw pointer of type `*mut
T`.

[expr.borrow.raw.invalid-ref]

The raw borrow operators must be used instead of a borrow operator whenever
the place expression could evaluate to a place that is not properly aligned or
does not store a valid value as determined by its type, or whenever creating a
reference would introduce incorrect aliasing assumptions. In those situations,
using a borrow operator would cause undefined behavior by creating an invalid
reference, but a raw pointer may still be constructed.

The following is an example of creating a raw pointer to an unaligned place
through a `packed` struct:

    
    
    #![allow(unused)]
    fn main() {
    #[repr(packed)]
    struct Packed {
        f1: u8,
        f2: u16,
    }
    
    let packed = Packed { f1: 1, f2: 2 };
    // `&packed.f2` would create an unaligned reference, and thus be undefined behavior!
    let raw_f2 = &raw const packed.f2;
    assert_eq!(unsafe { raw_f2.read_unaligned() }, 2);
    }

The following is an example of creating a raw pointer to a place that does not
contain a valid value:

    
    
    #![allow(unused)]
    fn main() {
    use std::mem::MaybeUninit;
    
    struct Demo {
        field: bool,
    }
    
    let mut uninit = MaybeUninit::<Demo>::uninit();
    // `&uninit.as_mut().field` would create a reference to an uninitialized `bool`,
    // and thus be undefined behavior!
    let f1_ptr = unsafe { &raw mut (*uninit.as_mut_ptr()).field };
    unsafe { f1_ptr.write(true); }
    let init = unsafe { uninit.assume_init() };
    }

[expr.deref]

## The dereference operator

[expr.deref.syntax]

**Syntax**  
DereferenceExpression → * Expression

Show Railroad

DereferenceExpression * Expression

[expr.deref.intro]

The `*` (dereference) operator is also a unary prefix operator.

[expr.deref.result]

When applied to a pointer it denotes the pointed-to location.

[expr.deref.mut]

If the expression is of type `&mut T` or `*mut T`, and is either a local
variable, a (nested) field of a local variable or is a mutable place
expression, then the resulting memory location can be assigned to.

[expr.deref.safety]

Dereferencing a raw pointer requires `unsafe`.

[expr.deref.traits]

On non-pointer types `*x` is equivalent to `*std::ops::Deref::deref(&x)` in an
immutable place expression context and `*std::ops::DerefMut::deref_mut(&mut
x)` in a mutable place expression context.

    
    
    #![allow(unused)]
    fn main() {
    let x = &7;
    assert_eq!(*x, 7);
    let y = &mut 9;
    *y = 11;
    assert_eq!(*y, 11);
    }

[expr.try]

## The try propagation expression

[expr.try.syntax]

**Syntax**  
TryPropagationExpression → Expression ?

Show Railroad

TryPropagationExpression Expression ?

[expr.try.intro]

The try propagation expression uses the value of the inner expression and the
[`Try`](../core/ops/try_trait/trait.Try.html) trait to decide whether to
produce a value, and if so, what value to produce, or whether to return a
value to the caller, and if so, what value to return.

> Example
>  
>  
>     #![allow(unused)]
>     fn main() {
>     use std::num::ParseIntError;
>     fn try_to_parse() -> Result<i32, ParseIntError> {
>         let x: i32 = "123".parse()?; // `x` is `123`.
>         let y: i32 = "24a".parse()?; // Returns an `Err()` immediately.
>         Ok(x + y)                    // Doesn't run.
>     }
>  
>     let res = try_to_parse();
>     println!("{res:?}");
>     assert!(res.is_err())
>     }
>  
>  
>     #![allow(unused)]
>     fn main() {
>     fn try_option_some() -> Option<u8> {
>         let val = Some(1)?;
>         Some(val)
>     }
>     assert_eq!(try_option_some(), Some(1));
>  
>     fn try_option_none() -> Option<u8> {
>         let val = None?;
>         Some(val)
>     }
>     assert_eq!(try_option_none(), None);
>     }
>  
>  
>     use std::ops::ControlFlow;
>  
>     pub struct TreeNode<T> {
>         value: T,
>         left: Option<Box<TreeNode<T>>>,
>         right: Option<Box<TreeNode<T>>>,
>     }
>  
>     impl<T> TreeNode<T> {
>         pub fn traverse_inorder<B>(&self, f: &mut impl FnMut(&T) ->
> ControlFlow<B>) -> ControlFlow<B> {
>             if let Some(left) = &self.left {
>                 left.traverse_inorder(f)?;
>             }
>             f(&self.value)?;
>             if let Some(right) = &self.right {
>                 right.traverse_inorder(f)?;
>             }
>             ControlFlow::Continue(())
>         }
>     }
>  
>     fn main() {
>         let n = TreeNode {
>             value: 1,
>             left: Some(Box::new(TreeNode{value: 2, left: None, right:
> None})),
>             right: None,
>         };
>         let v = n.traverse_inorder(&mut |t| {
>             if *t == 2 {
>                 ControlFlow::Break("found")
>             } else {
>                 ControlFlow::Continue(())
>             }
>         });
>         assert_eq!(v, ControlFlow::Break("found"));
>     }

> Note
>
> The [`Try`](../core/ops/try_trait/trait.Try.html) trait is currently
> unstable, and thus cannot be implemented for user types.
>
> The try propagation expression is currently roughly equivalent to:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     #![ feature(try_trait_v2) ]
>     fn example() -> Result<(), ()> {
>     let expr = Ok(());
>     match core::ops::Try::branch(expr) {
>         core::ops::ControlFlow::Continue(val) => val,
>         core::ops::ControlFlow::Break(residual) =>
>             return core::ops::FromResidual::from_residual(residual),
>     }
>     Ok(())
>     }
>     }

> Note
>
> The try propagation operator is sometimes called _the question mark
> operator_ , _the`?` operator_, or _the try operator_.

[expr.try.restricted-types]

The try propagation operator can be applied to expressions with the type of:

  * [`Result<T, E>`](../core/result/enum.Result.html)
    * `Result::Ok(val)` evaluates to `val`.
    * `Result::Err(e)` returns `Result::Err(From::from(e))`.
  * [`Option<T>`](../core/option/enum.Option.html)
    * `Option::Some(val)` evaluates to `val`.
    * `Option::None` returns `Option::None`.
  * [`ControlFlow<B, C>`](../core/ops/control_flow/enum.ControlFlow.html)
    * `ControlFlow::Continue(c)` evaluates to `c`.
    * `ControlFlow::Break(b)` returns `ControlFlow::Break(b)`.
  * [`Poll<Result<T, E>>`](../core/task/poll/enum.Poll.html)
    * `Poll::Ready(Ok(val))` evaluates to `Poll::Ready(val)`.
    * `Poll::Ready(Err(e))` returns `Poll::Ready(Err(From::from(e)))`.
    * `Poll::Pending` evaluates to `Poll::Pending`.
  * [`Poll<Option<Result<T, E>>>`](../core/task/poll/enum.Poll.html)
    * `Poll::Ready(Some(Ok(val)))` evaluates to `Poll::Ready(Some(val))`.
    * `Poll::Ready(Some(Err(e)))` returns `Poll::Ready(Some(Err(From::from(e))))`.
    * `Poll::Ready(None)` evaluates to `Poll::Ready(None)`.
    * `Poll::Pending` evaluates to `Poll::Pending`.

[expr.negate]

## Negation operators

[expr.negate.syntax]

**Syntax**  
NegationExpression →  
- Expression   
| ! Expression

Show Railroad

NegationExpression - Expression ! Expression

[expr.negate.intro]

These are the last two unary operators.

[expr.negate.results]

This table summarizes the behavior of them on primitive types and which traits
are used to overload these operators for other types. Remember that signed
integers are always represented using two’s complement. The operands of all of
these operators are evaluated in value expression context so are moved or
copied.

Symbol| Integer| `bool`| Floating Point| Overloading Trait  
---|---|---|---|---  
`-`| Negation*| | Negation| `std::ops::Neg`  
`!`| Bitwise NOT| Logical NOT| | `std::ops::Not`  
  
* Only for signed integer types.

Here are some example of these operators

    
    
    #![allow(unused)]
    fn main() {
    let x = 6;
    assert_eq!(-x, -6);
    assert_eq!(!x, -7);
    assert_eq!(true, !false);
    }

[expr.arith-logic]

## Arithmetic and logical binary operators

[expr.arith-logic.syntax]

**Syntax**  
ArithmeticOrLogicalExpression →  
Expression + Expression  
| Expression - Expression  
| Expression * Expression  
| Expression / Expression  
| Expression % Expression  
| Expression & Expression  
| Expression | Expression   
| Expression ^ Expression  
| Expression << Expression  
| Expression >> Expression

Show Railroad

ArithmeticOrLogicalExpression Expression + Expression Expression - Expression Expression * Expression Expression / Expression Expression % Expression Expression & Expression Expression | Expression Expression ^ Expression Expression << Expression Expression >> Expression

[expr.arith-logic.intro]

Binary operators expressions are all written with infix notation.

[expr.arith-logic.behavior]

This table summarizes the behavior of arithmetic and logical binary operators
on primitive types and which traits are used to overload these operators for
other types. Remember that signed integers are always represented using two’s
complement. The operands of all of these operators are evaluated in value
expression context so are moved or copied.

Symbol| Integer| `bool`| Floating Point| Overloading Trait| Overloading
Compound Assignment Trait  
---|---|---|---|---|---  
`+`| Addition| | Addition| `std::ops::Add`| `std::ops::AddAssign`  
`-`| Subtraction| | Subtraction| `std::ops::Sub`| `std::ops::SubAssign`  
`*`| Multiplication| | Multiplication| `std::ops::Mul`| `std::ops::MulAssign`  
`/`| Division*†| | Division| `std::ops::Div`| `std::ops::DivAssign`  
`%`| Remainder**†| | Remainder| `std::ops::Rem`| `std::ops::RemAssign`  
`&`| Bitwise AND| Logical AND| | `std::ops::BitAnd`| `std::ops::BitAndAssign`  
`|`| Bitwise OR| Logical OR| | `std::ops::BitOr`| `std::ops::BitOrAssign`  
`^`| Bitwise XOR| Logical XOR| | `std::ops::BitXor`| `std::ops::BitXorAssign`  
`<<`| Left Shift| | | `std::ops::Shl`| `std::ops::ShlAssign`  
`>>`| Right Shift***| | | `std::ops::Shr`| `std::ops::ShrAssign`  
  
* Integer division rounds towards zero.

** Rust uses a remainder defined with [truncating
division](https://en.wikipedia.org/wiki/Modulo_operation#Variants_of_the_definition).
Given `remainder = dividend % divisor`, the remainder will have the same sign
as the dividend.

*** Arithmetic right shift on signed integer types, logical right shift on
unsigned integer types.

† For integer types, division by zero panics.

Here are examples of these operators being used.

    
    
    #![allow(unused)]
    fn main() {
    assert_eq!(3 + 6, 9);
    assert_eq!(5.5 - 1.25, 4.25);
    assert_eq!(-5 * 14, -70);
    assert_eq!(14 / 3, 4);
    assert_eq!(100 % 7, 2);
    assert_eq!(0b1010 & 0b1100, 0b1000);
    assert_eq!(0b1010 | 0b1100, 0b1110);
    assert_eq!(0b1010 ^ 0b1100, 0b110);
    assert_eq!(13 << 3, 104);
    assert_eq!(-10 >> 2, -3);
    }

[expr.cmp]

## Comparison operators

[expr.cmp.syntax]

**Syntax**  
ComparisonExpression →  
Expression == Expression  
| Expression != Expression  
| Expression > Expression  
| Expression < Expression  
| Expression >= Expression  
| Expression <= Expression

Show Railroad

ComparisonExpression Expression == Expression Expression != Expression
Expression > Expression Expression < Expression Expression >= Expression
Expression <= Expression

[expr.cmp.intro]

Comparison operators are also defined both for primitive types and many types
in the standard library.

[expr.cmp.paren-chaining]

Parentheses are required when chaining comparison operators. For example, the
expression `a == b == c` is invalid and may be written as `(a == b) == c`.

[expr.cmp.trait]

Unlike arithmetic and logical operators, the traits for overloading these
operators are used more generally to show how a type may be compared and will
likely be assumed to define actual comparisons by functions that use these
traits as bounds. Many functions and macros in the standard library can then
use that assumption (although not to ensure safety).

[expr.cmp.place]

Unlike the arithmetic and logical operators above, these operators implicitly
take shared borrows of their operands, evaluating them in place expression
context:

    
    
    #![allow(unused)]
    fn main() {
    let a = 1;
    let b = 1;
    a == b;
    // is equivalent to
    ::std::cmp::PartialEq::eq(&a, &b);
    }

This means that the operands don’t have to be moved out of.

[expr.cmp.behavior]

Symbol| Meaning| Overloading method  
---|---|---  
`==`| Equal| `std::cmp::PartialEq::eq`  
`!=`| Not equal| `std::cmp::PartialEq::ne`  
`>`| Greater than| `std::cmp::PartialOrd::gt`  
`<`| Less than| `std::cmp::PartialOrd::lt`  
`>=`| Greater than or equal to| `std::cmp::PartialOrd::ge`  
`<=`| Less than or equal to| `std::cmp::PartialOrd::le`  
  
Here are examples of the comparison operators being used.

    
    
    #![allow(unused)]
    fn main() {
    assert!(123 == 123);
    assert!(23 != -12);
    assert!(12.5 > 12.2);
    assert!([1, 2, 3] < [1, 3, 4]);
    assert!('A' <= 'B');
    assert!("World" >= "Hello");
    }

[expr.bool-logic]

## Lazy boolean operators

[expr.bool-logic.syntax]

**Syntax**  
LazyBooleanExpression →  
Expression || Expression  
| Expression && Expression

Show Railroad

LazyBooleanExpression Expression || Expression Expression && Expression

[expr.bool-logic.intro]

The operators `||` and `&&` may be applied to operands of boolean type. The
`||` operator denotes logical ‘or’, and the `&&` operator denotes logical
‘and’.

[expr.bool-logic.conditional-evaluation]

They differ from `|` and `&` in that the right-hand operand is only evaluated
when the left-hand operand does not already determine the result of the
expression. That is, `||` only evaluates its right-hand operand when the left-
hand operand evaluates to `false`, and `&&` only when it evaluates to `true`.

    
    
    #![allow(unused)]
    fn main() {
    let x = false || true; // true
    let y = false && panic!(); // false, doesn't evaluate `panic!()`
    }

[expr.as]

## Type cast expressions

[expr.as.syntax]

**Syntax**  
TypeCastExpression → Expression as TypeNoBounds

Show Railroad

TypeCastExpression Expression as TypeNoBounds

[expr.as.intro]

A type cast expression is denoted with the binary operator `as`.

[expr.as.result]

Executing an `as` expression casts the value on the left-hand side to the type
on the right-hand side.

An example of an `as` expression:

    
    
    #![allow(unused)]
    fn main() {
    fn sum(values: &[f64]) -> f64 { 0.0 }
    fn len(values: &[f64]) -> i32 { 0 }
    fn average(values: &[f64]) -> f64 {
        let sum: f64 = sum(values);
        let size: f64 = len(values) as f64;
        sum / size
    }
    }

[expr.as.coercions]

`as` can be used to explicitly perform coercions, as well as the following
additional casts. Any cast that does not fit either a coercion rule or an
entry in the table is a compiler error. Here `*T` means either `*const T` or
`*mut T`. `m` stands for optional `mut` in reference types and `mut` or
`const` in pointer types.

Type of `e`| `U`| Cast performed by `e as U`  
---|---|---  
Integer or Float type| Integer or Float type| Numeric cast  
Enumeration| Integer type| Enum cast  
`bool` or `char`| Integer type| Primitive to integer cast  
`u8`| `char`| `u8` to `char` cast  
`*T`| `*V` 1| Pointer to pointer cast  
`*T` where `T: Sized`| Integer type| Pointer to address cast  
Integer type| `*V` where `V: Sized`| Address to pointer cast  
`&m₁ [T; n]`| `*m₂ T` 2| Array to pointer cast  
`*m₁ [T; n]`| `*m₂ T` 2| Array to pointer cast  
Function item| Function pointer| Function item to function pointer cast  
Function item| `*V` where `V: Sized`| Function item to pointer cast  
Function item| Integer| Function item to address cast  
Function pointer| `*V` where `V: Sized`| Function pointer to pointer cast  
Function pointer| Integer| Function pointer to address cast  
Closure 3| Function pointer| Closure to function pointer cast  
  
### Semantics

[expr.as.numeric]

#### Numeric cast

[expr.as.numeric.int-same-size]

  * Casting between two integers of the same size (e.g. i32 -> u32) is a no-op (Rust uses 2’s complement for negative values of fixed integers)
        
        #![allow(unused)]
        fn main() {
        assert_eq!(42i8 as u8, 42u8);
        assert_eq!(-1i8 as u8, 255u8);
        assert_eq!(255u8 as i8, -1i8);
        assert_eq!(-1i16 as u16, 65535u16);
        }

[expr.as.numeric.int-truncation]

  * Casting from a larger integer to a smaller integer (e.g. u32 -> u8) will truncate
        
        #![allow(unused)]
        fn main() {
        assert_eq!(42u16 as u8, 42u8);
        assert_eq!(1234u16 as u8, 210u8);
        assert_eq!(0xabcdu16 as u8, 0xcdu8);
        
        assert_eq!(-42i16 as i8, -42i8);
        assert_eq!(1234u16 as i8, -46i8);
        assert_eq!(0xabcdi32 as i8, -51i8);
        }

[expr.as.numeric.int-extension]

  * Casting from a smaller integer to a larger integer (e.g. u8 -> u32) will

    * zero-extend if the source is unsigned
    * sign-extend if the source is signed
    
    #![allow(unused)]
    fn main() {
    assert_eq!(42i8 as i16, 42i16);
    assert_eq!(-17i8 as i16, -17i16);
    assert_eq!(0b1000_1010u8 as u16, 0b0000_0000_1000_1010u16, "Zero-extend");
    assert_eq!(0b0000_1010i8 as i16, 0b0000_0000_0000_1010i16, "Sign-extend 0");
    assert_eq!(0b1000_1010u8 as i8 as i16, 0b1111_1111_1000_1010u16 as i16, "Sign-extend 1");
    }

[expr.as.numeric.float-as-int]

  * Casting from a float to an integer will round the float towards zero

    * `NaN` will return `0`
    * Values larger than the maximum integer value, including `INFINITY`, will saturate to the maximum value of the integer type.
    * Values smaller than the minimum integer value, including `NEG_INFINITY`, will saturate to the minimum value of the integer type.
    
    #![allow(unused)]
    fn main() {
    assert_eq!(42.9f32 as i32, 42);
    assert_eq!(-42.9f32 as i32, -42);
    assert_eq!(42_000_000f32 as i32, 42_000_000);
    assert_eq!(std::f32::NAN as i32, 0);
    assert_eq!(1_000_000_000_000_000f32 as i32, 0x7fffffffi32);
    assert_eq!(std::f32::NEG_INFINITY as i32, -0x80000000i32);
    }

[expr.as.numeric.int-as-float]

  * Casting from an integer to float will produce the closest possible float *

    * if necessary, rounding is according to `roundTiesToEven` mode ***
    * on overflow, infinity (of the same sign as the input) is produced
    * note: with the current set of numeric types, overflow can only happen on `u128 as f32` for values greater or equal to `f32::MAX + (0.5 ULP)`
    
    #![allow(unused)]
    fn main() {
    assert_eq!(1337i32 as f32, 1337f32);
    assert_eq!(123_456_789i32 as f32, 123_456_790f32, "Rounded");
    assert_eq!(0xffffffff_ffffffff_ffffffff_ffffffff_u128 as f32, std::f32::INFINITY);
    }

[expr.as.numeric.float-widening]

  * Casting from an f32 to an f64 is perfect and lossless
        
        #![allow(unused)]
        fn main() {
        assert_eq!(1_234.5f32 as f64, 1_234.5f64);
        assert_eq!(std::f32::INFINITY as f64, std::f64::INFINITY);
        assert!((std::f32::NAN as f64).is_nan());
        }

[expr.as.numeric.float-narrowing]

  * Casting from an f64 to an f32 will produce the closest possible f32 **

    * if necessary, rounding is according to `roundTiesToEven` mode ***
    * on overflow, infinity (of the same sign as the input) is produced
    
    #![allow(unused)]
    fn main() {
    assert_eq!(1_234.5f64 as f32, 1_234.5f32);
    assert_eq!(1_234_567_891.123f64 as f32, 1_234_567_890f32, "Rounded");
    assert_eq!(std::f64::INFINITY as f32, std::f32::INFINITY);
    assert!((std::f64::NAN as f32).is_nan());
    }

* if integer-to-float casts with this rounding mode and overflow behavior are not supported natively by the hardware, these casts will likely be slower than expected.

** if f64-to-f32 casts with this rounding mode and overflow behavior are not
supported natively by the hardware, these casts will likely be slower than
expected.

*** as defined in IEEE 754-2008 §4.3.1: pick the nearest floating point
number, preferring the one with an even least significant digit if exactly
halfway between two floating point numbers.

[expr.as.enum]

#### Enum cast

[expr.as.enum.discriminant]

Casts an enum to its discriminant, then uses a numeric cast if needed. Casting
is limited to the following kinds of enumerations:

  * Unit-only enums
  * Field-less enums without explicit discriminants, or where only unit-variants have explicit discriminants

    
    
    #![allow(unused)]
    fn main() {
    enum Enum { A, B, C }
    assert_eq!(Enum::A as i32, 0);
    assert_eq!(Enum::B as i32, 1);
    assert_eq!(Enum::C as i32, 2);
    }

[expr.as.enum.no-drop]

Casting is not allowed if the enum implements
[`Drop`](../core/ops/drop/trait.Drop.html).

[expr.as.bool-char-as-int]

#### Primitive to integer cast

  * `false` casts to `0`, `true` casts to `1`
  * `char` casts to the value of the code point, then uses a numeric cast if needed.

    
    
    #![allow(unused)]
    fn main() {
    assert_eq!(false as i32, 0);
    assert_eq!(true as i32, 1);
    assert_eq!('A' as i32, 65);
    assert_eq!('Ö' as i32, 214);
    }

[expr.as.u8-as-char]

#### `u8` to `char` cast

Casts to the `char` with the corresponding code point.

    
    
    #![allow(unused)]
    fn main() {
    assert_eq!(65u8 as char, 'A');
    assert_eq!(214u8 as char, 'Ö');
    }

[expr.as.pointer-as-int]

#### Pointer to address cast

Casting from a raw pointer to an integer produces the machine address of the
referenced memory. If the integer type is smaller than the pointer type, the
address may be truncated; using `usize` avoids this.

[expr.as.int-as-pointer]

#### Address to pointer cast

Casting from an integer to a raw pointer interprets the integer as a memory
address and produces a pointer referencing that memory.

> Warning
>
> This interacts with the Rust memory model, which is still under development.
> A pointer obtained from this cast may suffer additional restrictions even if
> it is bitwise equal to a valid pointer. Dereferencing such a pointer may be
> undefined behavior if aliasing rules are not followed.

A trivial example of sound address arithmetic:

    
    
    #![allow(unused)]
    fn main() {
    let mut values: [i32; 2] = [1, 2];
    let p1: *mut i32 = values.as_mut_ptr();
    let first_address = p1 as usize;
    let second_address = first_address + 4; // 4 == size_of::<i32>()
    let p2 = second_address as *mut i32;
    unsafe {
        *p2 += 1;
    }
    assert_eq!(values[1], 3);
    }

[expr.as.pointer]

#### Pointer-to-pointer cast

[expr.as.pointer.behavior]

`*const T` / `*mut T` can be cast to `*const U` / `*mut U` with the following
behavior:

[expr.as.pointer.sized]

  * If `T` and `U` are both sized, the pointer is returned unchanged.

[expr.as.pointer.unsized]

  * If `T` and `U` are both unsized, the pointer is also returned unchanged. In particular, the metadata is preserved exactly.

For instance, a cast from `*const [T]` to `*const [U]` preserves the number of
elements. Note that, as a consequence, such casts do not necessarily preserve
the size of the pointer’s referent (e.g., casting `*const [u16]` to `*const
[u8]` will result in a raw pointer which refers to an object of half the size
of the original). The same holds for `str` and any compound type whose unsized
tail is a slice type, such as `struct Foo(i32, [u8])` or `(u64, Foo)`.

[expr.as.pointer.discard-metadata]

  * If `T` is unsized and `U` is sized, the cast discards all metadata that completes the wide pointer `T` and produces a thin pointer `U` consisting of the data part of the unsized pointer.

[expr.assign]

## Assignment expressions

[expr.assign.syntax]

**Syntax**  
AssignmentExpression → Expression = Expression

Show Railroad

AssignmentExpression Expression = Expression

[expr.assign.intro]

An _assignment expression_ moves a value into a specified place.

[expr.assign.assignee]

An assignment expression consists of a mutable assignee expression, the
_assignee operand_ , followed by an equals sign (`=`) and a value expression,
the _assigned value operand_.

[expr.assign.behavior-basic]

In its most basic form, an assignee expression is a place expression, and we
discuss this case first.

[expr.assign.behavior-destructuring]

The more general case of destructuring assignment is discussed below, but this
case always decomposes into sequential assignments to place expressions, which
may be considered the more fundamental case.

[expr.assign.basic]

### Basic assignments

[expr.assign.evaluation-order]

Evaluating assignment expressions begins by evaluating its operands. The
assigned value operand is evaluated first, followed by the assignee
expression.

[expr.assign.destructuring-order]

For destructuring assignment, subexpressions of the assignee expression are
evaluated left-to-right.

> Note
>
> This is different than other expressions in that the right operand is
> evaluated before the left one.

[expr.assign.drop-target]

It then has the effect of first dropping the value at the assigned place,
unless the place is an uninitialized local variable or an uninitialized field
of a local variable.

[expr.assign.behavior]

Next it either copies or moves the assigned value to the assigned place.

[expr.assign.result]

An assignment expression always produces the unit value.

Example:

    
    
    #![allow(unused)]
    fn main() {
    let mut x = 0;
    let y = 0;
    x = y;
    }

[expr.assign.destructure]

### Destructuring assignments

[expr.assign.destructure.intro]

Destructuring assignment is a counterpart to destructuring pattern matches for
variable declaration, permitting assignment to complex values, such as tuples
or structs. For instance, we may swap two mutable variables:

    
    
    #![allow(unused)]
    fn main() {
    let (mut a, mut b) = (0, 1);
    // Swap `a` and `b` using destructuring assignment.
    (b, a) = (a, b);
    }

[expr.assign.destructure.assignee]

In contrast to destructuring declarations using `let`, patterns may not appear
on the left-hand side of an assignment due to syntactic ambiguities. Instead,
a group of expressions that correspond to patterns are designated to be
assignee expressions, and permitted on the left-hand side of an assignment.
Assignee expressions are then desugared to pattern matches followed by
sequential assignment.

[expr.assign.destructure.irrefutable]

The desugared patterns must be irrefutable: in particular, this means that
only slice patterns whose length is known at compile-time, and the trivial
slice `[..]`, are permitted for destructuring assignment.

The desugaring method is straightforward, and is illustrated best by example.

    
    
    #![allow(unused)]
    fn main() {
    struct Struct { x: u32, y: u32 }
    let (mut a, mut b) = (0, 0);
    (a, b) = (3, 4);
    
    [a, b] = [3, 4];
    
    Struct { x: a, y: b } = Struct { x: 3, y: 4};
    
    // desugars to:
    
    {
        let (_a, _b) = (3, 4);
        a = _a;
        b = _b;
    }
    
    {
        let [_a, _b] = [3, 4];
        a = _a;
        b = _b;
    }
    
    {
        let Struct { x: _a, y: _b } = Struct { x: 3, y: 4};
        a = _a;
        b = _b;
    }
    }

[expr.assign.destructure.repeat-ident]

Identifiers are not forbidden from being used multiple times in a single
assignee expression.

[expr.assign.destructure.discard-value]

Underscore expressions and empty range expressions may be used to ignore
certain values, without binding them.

[expr.assign.destructure.default-binding]

Note that default binding modes do not apply for the desugared expression.

[expr.assign.destructure.tmp-scopes]

> Note
>
> The desugaring restricts the temporary scope of the assigned value operand
> (the RHS) of a destructuring assignment.
>
> In a basic assignment, the temporary is dropped at the end of the enclosing
> temporary scope. Below, that’s the statement. Therefore, the assignment and
> use is allowed.
>  
>  
>     #![allow(unused)]
>     fn main() {
>     fn temp() {}
>     fn f<T>(x: T) -> T { x }
>     let x;
>     (x = f(&temp()), x); // OK
>     }
>
> Conversely, in a destructuring assignment, the temporary is dropped at the
> end of the `let` statement in the desugaring. As that happens before we try
> to assign to `x`, below, it fails.
>  
>  
>     #![allow(unused)]
>     fn main() {
>     fn temp() {}
>     fn f<T>(x: T) -> T { x }
>     let x;
>     [x] = [f(&temp())]; // ERROR
>     }
>
> This desugars to:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     fn temp() {}
>     fn f<T>(x: T) -> T { x }
>     let x;
>     {
>         let [_x] = [f(&temp())];
>         //                     ^
>         //      The temporary is dropped here.
>         x = _x; // ERROR
>     }
>     }

[expr.assign.destructure.tmp-ext]

> Note
>
> Due to the desugaring, the assigned value operand (the RHS) of a
> destructuring assignment is an extending expression within a newly-
> introduced block.
>
> Below, because the temporary scope is extended to the end of this introduced
> block, the assignment is allowed.
>  
>  
>     #![allow(unused)]
>     fn main() {
>     fn temp() {}
>     let x;
>     [x] = [&temp()]; // OK
>     }
>
> This desugars to:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     fn temp() {}
>     let x;
>     { let [_x] = [&temp()]; x = _x; } // OK
>     }
>
> However, if we try to use `x`, even within the same statement, we’ll get an
> error because the temporary is dropped at the end of this introduced block.
>  
>  
>     #![allow(unused)]
>     fn main() {
>     fn temp() {}
>     let x;
>     ([x] = [&temp()], x); // ERROR
>     }
>
> This desugars to:
>  
>  
>     #![allow(unused)]
>     fn main() {
>     fn temp() {}
>     let x;
>     (
>         {
>             let [_x] = [&temp()];
>             x = _x;
>         }, // <-- The temporary is dropped here.
>         x, // ERROR
>     );
>     }

[expr.compound-assign]

## Compound assignment expressions

[expr.compound-assign.syntax]

**Syntax**  
CompoundAssignmentExpression →  
Expression += Expression  
| Expression -= Expression  
| Expression *= Expression  
| Expression /= Expression  
| Expression %= Expression  
| Expression &= Expression  
| Expression |= Expression  
| Expression ^= Expression  
| Expression <<= Expression  
| Expression >>= Expression

Show Railroad

CompoundAssignmentExpression Expression += Expression Expression -= Expression
Expression *= Expression Expression /= Expression Expression %= Expression
Expression &= Expression Expression |= Expression Expression ^= Expression
Expression <<= Expression Expression >>= Expression

[expr.compound-assign.intro]

_Compound assignment expressions_ combine arithmetic and logical binary
operators with assignment expressions.

For example:

    
    
    #![allow(unused)]
    fn main() {
    let mut x = 5;
    x += 1;
    assert!(x == 6);
    }

The syntax of compound assignment is a mutable place expression, the _assigned
operand_ , then one of the operators followed by an `=` as a single token (no
whitespace), and then a value expression, the _modifying operand_.

[expr.compound-assign.place]

Unlike other place operands, the assigned place operand must be a place
expression.

[expr.compound-assign.no-value]

Attempting to use a value expression is a compiler error rather than promoting
it to a temporary.

[expr.compound-assign.operand-order]

Evaluation of compound assignment expressions depends on the types of the
operands.

[expr.compound-assign.primitives]

If the types of both operands are known, prior to monomorphization, to be
primitive, the right hand side is evaluated first, the left hand side is
evaluated next, and the place given by the evaluation of the left hand side is
mutated by applying the operator to the values of both sides.

    
    
    use core::{num::Wrapping, ops::AddAssign};
    
    trait Equate {}
    impl<T> Equate for (T, T) {}
    
    fn f1(x: (u8,)) {
        let mut order = vec![];
        // The RHS is evaluated first as both operands are of primitive
        // type.
        { order.push(2); x }.0 += { order.push(1); x }.0;
        assert!(order.is_sorted());
    }
    
    fn f2(x: (Wrapping<u8>,)) {
        let mut order = vec![];
        // The LHS is evaluated first as `Wrapping<_>` is not a primitive
        // type.
        { order.push(1); x }.0 += { order.push(2); (0u8,) }.0;
        assert!(order.is_sorted());
    }
    
    fn f3<T: AddAssign<u8> + Copy>(x: (T,)) where (T, u8): Equate {
        let mut order = vec![];
        // The LHS is evaluated first as one of the operands is a generic
        // parameter, even though that generic parameter can be unified
        // with a primitive type due to the where clause bound.
        { order.push(1); x }.0 += { order.push(2); (0u8,) }.0;
        assert!(order.is_sorted());
    }
    
    fn main() {
        f1((0u8,));
        f2((Wrapping(0u8),));
        // We supply a primitive type as the generic argument, but this
        // does not affect the evaluation order in `f3` when
        // monomorphized.
        f3::<u8>((0u8,));
    }

> Note
>
> This is unusual. Elsewhere left to right evaluation is the norm.
>
> See the [eval order test](https://github.com/rust-
> lang/rust/blob/1.58.0/src/test/ui/expr/compound-assignment/eval-order.rs)
> for more examples.

[expr.compound-assign.trait]

Otherwise, this expression is syntactic sugar for using the corresponding
trait for the operator (see expr.arith-logic.behavior) and calling its method
with the left hand side as the receiver and the right hand side as the next
argument.

For example, the following two statements are equivalent:

    
    
    #![allow(unused)]
    fn main() {
    use std::ops::AddAssign;
    fn f<T: AddAssign + Copy>(mut x: T, y: T) {
        x += y; // Statement 1.
        x.add_assign(y); // Statement 2.
    }
    }

> Note
>
> Surprisingly, desugaring this further to a fully qualified method call is
> not equivalent, as there is special borrow checker behavior when the mutable
> reference to the first operand is taken via autoref.
>  
>  
>     #![allow(unused)]
>     fn main() {
>     use std::ops::AddAssign;
>     fn f<T: AddAssign + Copy>(mut x: T) {
>         // Here we used `x` as both the LHS and the RHS. Because the
>         // mutable borrow of the LHS needed to call the trait method
>         // is taken implicitly by autoref, this is OK.
>         x += x; //~ OK
>         x.add_assign(x); //~ OK
>     }
>     }
>  
>  
>     #![allow(unused)]
>     fn main() {
>     use std::ops::AddAssign;
>     fn f<T: AddAssign + Copy>(mut x: T) {
>         // We can't desugar the above to the below, as once we take the
>         // mutable borrow of `x` to pass the first argument, we can't
>         // pass `x` by value in the second argument because the mutable
>         // reference is still live.
>         <T as AddAssign>::add_assign(&mut x, x);
>         //~^ ERROR cannot use `x` because it was mutably borrowed
>     }
>     }
>  
>  
>     #![allow(unused)]
>     fn main() {
>     use std::ops::AddAssign;
>     fn f<T: AddAssign + Copy>(mut x: T) {
>         // As above.
>         (&mut x).add_assign(x);
>         //~^ ERROR cannot use `x` because it was mutably borrowed
>     }
>     }

[expr.compound-assign.result]

As with normal assignment expressions, compound assignment expressions always
produce the unit value.

> Warning
>
> Avoid writing code that depends on the evaluation order of operands in
> compound assignments as it can be unusual and surprising.

* * *

  1. Where `T` and `V` have compatible metadata:

     * `V: Sized`, or
     * Both slice metadata (`*[u16]` -> `*[u8]`, `*str` -> `*(u8, [u32])`), or
     * Both the same trait object metadata, modulo dropping auto traits (`*dyn Debug` -> `*(u16, dyn Debug)`, `*dyn Debug + Send` -> `*dyn Debug`) 
       * **Note** : _adding_ auto traits is only allowed if the principal trait has the auto trait as a super trait (given `trait T: Send {}`, `*dyn T` -> `*dyn T + Send` is valid, but `*dyn Debug` -> `*dyn Debug + Send` is not)
       * **Note** : Generics (including lifetimes) must match (`*dyn T<'a, A>` -> `*dyn T<'b, B>` requires `'a = 'b` and `A = B`)
↩

  2. Only when `m₁` is `mut` or `m₂` is `const`. Casting `mut` reference/pointer to `const` pointer is allowed. ↩ ↩2

  3. Only closures that do not capture (close over) any local variables can be cast to function pointers. ↩

[expr.paren]

# Grouped expressions

[expr.paren.syntax]

**Syntax**  
GroupedExpression → ( Expression )

Show Railroad

GroupedExpression ( Expression )

[expr.paren.intro]

A _parenthesized expression_ wraps a single expression, evaluating to that
expression. The syntax for a parenthesized expression is a `(`, then an
expression, called the _enclosed operand_ , and then a `)`.

[expr.paren.evaluation]

Parenthesized expressions evaluate to the value of the enclosed operand.

[expr.paren.place-or-value]

Unlike other expressions, parenthesized expressions are both place expressions
and value expressions. When the enclosed operand is a place expression, it is
a place expression and when the enclosed operand is a value expression, it is
a value expression.

[expr.paren.override-precedence]

Parentheses can be used to explicitly modify the precedence order of
subexpressions within an expression.

An example of a parenthesized expression:

    
    
    #![allow(unused)]
    fn main() {
    let x: i32 = 2 + 3 * 4; // not parenthesized
    let y: i32 = (2 + 3) * 4; // parenthesized
    assert_eq!(x, 14);
    assert_eq!(y, 20);
    }

An example of a necessary use of parentheses is when calling a function
pointer that is a member of a struct:

    
    
    #![allow(unused)]
    fn main() {
    struct A {
       f: fn() -> &'static str
    }
    impl A {
       fn f(&self) -> &'static str {
           "The method f"
       }
    }
    let a = A{f: || "The field f"};
    
    assert_eq!( a.f (), "The method f");
    assert_eq!((a.f)(), "The field f");
    }

[expr.array]

# Array and array index expressions

## Array expressions

[expr.array.syntax]

**Syntax**  
ArrayExpression → [ ArrayElements? ]

ArrayElements →  
Expression ( , Expression )* ,?  
| Expression ; Expression

Show Railroad

ArrayExpression [ ArrayElements ]

ArrayElements Expression , Expression , Expression ; Expression

[expr.array.constructor]

_Array expressions_ construct arrays. Array expressions come in two forms.

[expr.array.array]

The first form lists out every value in the array.

[expr.array.array-syntax]

The syntax for this form is a comma-separated list of expressions of uniform
type enclosed in square brackets.

[expr.array.array-behavior]

This produces an array containing each of these values in the order they are
written.

[expr.array.repeat]

The syntax for the second form is two expressions separated by a semicolon
(`;`) enclosed in square brackets.

[expr.array.repeat-operand]

The expression before the `;` is called the _repeat operand_.

[expr.array.length-operand]

The expression after the `;` is called the _length operand_.

[expr.array.length-restriction]

The length operand must either be an inferred const or be a constant
expression of type `usize` (e.g. a literal or a constant item).

    
    
    #![allow(unused)]
    fn main() {
    const C: usize = 1;
    let _: [u8; C] = [0; 1]; // Literal.
    let _: [u8; C] = [0; C]; // Constant item.
    let _: [u8; C] = [0; _]; // Inferred const.
    let _: [u8; C] = [0; (((_)))]; // Inferred const.
    }

> Note
>
> In an array expression, an inferred const is parsed as an expression but
> then semantically treated as a separate kind of const generic argument.

[expr.array.repeat-behavior]

An array expression of this form creates an array with the length of the value
of the length operand with each element being a copy of the repeat operand.
That is, `[a; b]` creates an array containing `b` copies of the value of `a`.

[expr.array.repeat-copy]

If the length operand has a value greater than 1 then this requires the repeat
operand to have a type that implements `Copy`, to be a const block expression,
or to be a path to a constant item.

[expr.array.repeat-const-item]

When the repeat operand is a const block or a path to a constant item, it is
evaluated the number of times specified in the length operand.

[expr.array.repeat-evaluation-zero]

If that value is `0`, then the const block or constant item is not evaluated
at all.

[expr.array.repeat-non-const]

For expressions that are neither a const block nor a path to a constant item,
it is evaluated exactly once, and then the result is copied the length
operand’s value times.

    
    
    #![allow(unused)]
    fn main() {
    [1, 2, 3, 4];
    ["a", "b", "c", "d"];
    [0; 128];              // array with 128 zeros
    [0u8, 0u8, 0u8, 0u8,];
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]; // 2D array
    const EMPTY: Vec<i32> = Vec::new();
    [EMPTY; 2];
    }

[expr.array.index]

## Array and slice indexing expressions

[expr.array.index.syntax]

**Syntax**  
IndexExpression → Expression [ Expression ]

Show Railroad

IndexExpression Expression [ Expression ]

[expr.array.index.array]

Array and slice-typed values can be indexed by writing a square-bracket-
enclosed expression of type `usize` (the index) after them. When the array is
mutable, the resulting memory location can be assigned to.

[expr.array.index.trait]

For other types an index expression `a[b]` is equivalent to
`*std::ops::Index::index(&a, b)`, or `*std::ops::IndexMut::index_mut(&mut a,
b)` in a mutable place expression context. Just as with methods, Rust will
also insert dereference operations on `a` repeatedly to find an
implementation.

[expr.array.index.zero-index]

Indices are zero-based for arrays and slices.

[expr.array.index.const]

Array access is a constant expression, so bounds can be checked at compile-
time with a constant index value. Otherwise a check will be performed at run-
time that will put the thread in a _panicked state_ if it fails.

    
    
    #![allow(unused)]
    fn main() {
    // lint is deny by default.
    #![warn(unconditional_panic)]
    
    ([1, 2, 3, 4])[2];        // Evaluates to 3
    
    let b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
    b[1][2];                  // multidimensional array indexing
    
    let x = (["a", "b"])[10]; // warning: index out of bounds
    
    let n = 10;
    let y = (["a", "b"])[n];  // panics
    
    let arr = ["a", "b"];
    arr[10];                  // warning: index out of bounds
    }

[expr.array.index.trait-impl]

The array index expression can be implemented for types other than arrays and
slices by implementing the [Index](../core/ops/index/trait.Index.html) and
[IndexMut](../core/ops/index/trait.IndexMut.html) traits.

[expr.tuple]

# Tuple and tuple indexing expressions

## Tuple expressions

[expr.tuple.syntax]

**Syntax**  
TupleExpression → ( TupleElements? )

TupleElements → ( Expression , )+ Expression?

Show Railroad

TupleExpression ( TupleElements )

TupleElements Expression , Expression

[expr.tuple.result]

A _tuple expression_ constructs tuple values.

[expr.tuple.intro]

The syntax for tuple expressions is a parenthesized, comma separated list of
expressions, called the _tuple initializer operands_.

[expr.tuple.unary-tuple-restriction]

1-ary tuple expressions require a comma after their tuple initializer operand
to be disambiguated with a parenthetical expression.

[expr.tuple.value]

Tuple expressions are a value expression that evaluate into a newly
constructed value of a tuple type.

[expr.tuple.type]

The number of tuple initializer operands is the arity of the constructed
tuple.

[expr.tuple.unit]

Tuple expressions without any tuple initializer operands produce the unit
tuple.

[expr.tuple.fields]

For other tuple expressions, the first written tuple initializer operand
initializes t