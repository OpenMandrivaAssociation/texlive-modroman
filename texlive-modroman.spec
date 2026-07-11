%global tl_name modroman
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	Write numbers in lower case roman numerals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/modroman
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/modroman.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/modroman.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/modroman.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides only two macros viz. \modromannumeral which writes
the number given as argument in lower case roman numeral with a 'j'
instead of a 'i' as the final letter of numbers greater than 1 and
\modroman{MyCounter} which writes the value of a counter in the same
way. You use the first in the same way as the TeX primitive
\romannumeral and the second as LaTeX command \roman. The default option
is 'vpourv' with which 5 is 'translated' as 'v' and option 'upourv' with
which the same 5 is given as 'u'.

