%global tl_name hyphenat
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3c
Release:	%{tl_revision}.1
Summary:	Disable/enable hyphenation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hyphenat
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can disable all hyphenation or enable hyphenation of non-
alphabetics or monospaced fonts. The package can also enable hyphenation
within 'words' that contain non-alphabetic characters (e.g., that
include underscores), and hyphenation of text typeset in monospaced
(e.g., cmtt) fonts.

