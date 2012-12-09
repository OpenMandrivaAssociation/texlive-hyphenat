# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/hyphenat
# catalog-date 2009-09-02 18:09:14 +0200
# catalog-license lppl1.3
# catalog-version 2.3c
Name:		texlive-hyphenat
Version:	2.3c
Release:	2
Summary:	Disable/enable hypenation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hyphenat
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenat.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.3c-2
+ Revision: 752631
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.3c-1
+ Revision: 718637
- texlive-hyphenat
- texlive-hyphenat
- texlive-hyphenat
- texlive-hyphenat

