Name:		texlive-padauk
Version:	42617
Release:	1
Summary:	A high-quality TrueType font that supports the many diverse languages that use the Myanmar script
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/padauk
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/padauk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/padauk.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Padauk is a Unicode-based font family with broad support for
writing systems that use the Myanmar script.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/truetype/public/padauk
%doc %{_texmfdistdir}/doc/fonts/padauk

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
