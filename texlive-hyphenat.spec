Name:		texlive-hyphenat
Version:	2.3c
Release:	1
Summary:	Disable/enable hypenation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hyphenat
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package can disable all hyphenation or enable hyphenation
of non-alphabetics or monospaced fonts. The package can also
enable hyphenation within 'words' that contain non-alphabetic
characters (e.g., that include underscores), and hyphenation of
text typeset in monospaced (e.g., cmtt) fonts.

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
%{_texmfdistdir}/tex/latex/hyphenat/hyphenat.sty
%doc %{_texmfdistdir}/doc/latex/hyphenat/README
%doc %{_texmfdistdir}/doc/latex/hyphenat/hyphenat.pdf
#- source
%doc %{_texmfdistdir}/source/latex/hyphenat/hyphenat.dtx
%doc %{_texmfdistdir}/source/latex/hyphenat/hyphenat.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
