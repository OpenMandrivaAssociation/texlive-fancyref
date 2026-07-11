%global tl_name fancyref
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9c
Release:	%{tl_revision}.1
Summary:	A LaTeX package for fancy cross-referencing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fancyref
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyref.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyref.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides fancy cross-referencing support, based on the package's
reference commands (\fref and \Fref) that recognise what sort of object
is being referenced. So, for example, the label for a \section would be
expected to be of the form 'sec:foo': the package would recognise the
'sec:' part.

