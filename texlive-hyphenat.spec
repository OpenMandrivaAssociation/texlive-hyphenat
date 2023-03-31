Name:		texlive-hyphenat
Version:	15878
Release:	2
Summary:	Disable/enable hypenation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hyphenat
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can disable all hyphenation or enable hyphenation
of non-alphabetics or monospaced fonts. The package can also
enable hyphenation within 'words' that contain non-alphabetic
characters (e.g., that include underscores), and hyphenation of
text typeset in monospaced (e.g., cmtt) fonts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
