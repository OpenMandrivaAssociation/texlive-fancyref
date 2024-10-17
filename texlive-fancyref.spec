Name:		texlive-fancyref
Version:	15878
Release:	2
Summary:	A LaTeX package for fancy cross-referencing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fancyref
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyref.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyref.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides fancy cross-referencing support, based on the
package's reference commands (\fref and \Fref) that recognise
what sort of object is being referenced. So, for example, the
label for a \section would be expected to be of the form
'sec:foo': the package would recognise the 'sec:' part.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fancyref/fancyref.sty
%doc %{_texmfdistdir}/doc/latex/fancyref/COPYING
%doc %{_texmfdistdir}/doc/latex/fancyref/README
%doc %{_texmfdistdir}/doc/latex/fancyref/fancyref.pdf
%doc %{_texmfdistdir}/doc/latex/fancyref/freftest.tex
#- source
%doc %{_texmfdistdir}/source/latex/fancyref/fancyref.dtx
%doc %{_texmfdistdir}/source/latex/fancyref/fancyref.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
