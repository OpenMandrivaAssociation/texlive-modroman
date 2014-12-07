# revision 29803
# category Package
# catalog-ctan /macros/latex/contrib/modroman
# catalog-date 2012-07-07 22:27:26 +0200
# catalog-license lppl
# catalog-version 1
Name:		texlive-modroman
Version:	1
Release:	10
Summary:	Write numbers in lower case roman numerals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/modroman
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modroman.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modroman.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modroman.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides only two macros viz. \modromannumeral
which writes the number given as argument in lower case roman
numeral with a 'j' instead of a 'i' as the final letter of
numbers greater than 1 and \modroman{MyCounter} which writes
the value of a counter in the same way. You use the first in
the same way as the TeX primitive \romannumeral and the second
as LaTeX command \roman. The default option is 'vpourv' with
which 5 is 'translated' as 'v' and option 'upourv' whith which
the same 5 is given as 'u'.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/modroman/modroman.sty
%doc %{_texmfdistdir}/doc/latex/modroman/MODRdoctools.sty
%doc %{_texmfdistdir}/doc/latex/modroman/modroman-en.pdf
%doc %{_texmfdistdir}/doc/latex/modroman/modroman-en.tex
%doc %{_texmfdistdir}/doc/latex/modroman/modroman-fr.pdf
%doc %{_texmfdistdir}/doc/latex/modroman/modroman-fr.tex
%doc %{_texmfdistdir}/doc/latex/modroman/modroman.dtx
%doc %{_texmfdistdir}/doc/latex/modroman/modroman.pdf
#- source
%doc %{_texmfdistdir}/source/latex/modroman/LISEZMOI
%doc %{_texmfdistdir}/source/latex/modroman/Makefile
%doc %{_texmfdistdir}/source/latex/modroman/README
%doc %{_texmfdistdir}/source/latex/modroman/modroman.dtx
%doc %{_texmfdistdir}/source/latex/modroman/modroman.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
