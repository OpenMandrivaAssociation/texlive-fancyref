# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fancyref
# catalog-date 2006-12-05 17:23:05 +0100
# catalog-license gpl
# catalog-version 0.9c
Name:		texlive-fancyref
Version:	0.9c
Release:	1
Summary:	A LaTeX package for fancy cross-referencing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancyref
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyref.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyref.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides fancy cross-referencing support, based on the
package's reference commands (\fref and \Fref) that recognise
what sort of object is being referenced. So, for example, the
label for a \section would be expected to be of the form
'sec:foo': the package would recognise the 'sec:' part.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
