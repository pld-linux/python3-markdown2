#
# Conditional build:
%bcond_with	tests	# unit tests (quite bitrotten)

Summary:	A fast and complete Python implementation of Markdown
Summary(pl.UTF-8):	Szybka i kompletne implementacja Markdown w Pythonie
Name:		python3-markdown2
Version:	2.5.5
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/markdown2/
Source0:	https://files.pythonhosted.org/packages/source/m/markdown2/markdown2-%{version}.tar.gz
# Source0-md5:	81a628175ca4ec7ffb9428e0609d4fe3
URL:		https://pypi.org/project/markdown2/
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-latex2mathml
BuildRequires:	python3-pygments >= 2.7.3
BuildRequires:	python3-wavedrom
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This (markdown2) is a fast and complete Python implementation of
Markdown. It was written to closely match the behaviour of the
original Perl-implemented Markdown.pl. Markdown2 also comes with a
number of extensions (called "extras") for things like syntax
coloring, tables, header-ids.

%description -l pl.UTF-8
Ten pakiet (markdown2) to szybka i kompletna implementacja Markdown w
Pythonie. Został napisany jako zbliżony w zachowaniu do oryginalnej
implementacji Markdown.pl w Perlu. Markdown2 zawiera także kilka
rozszerzeń ("extras") do elementów takich jak kolorowanie składni,
tabele, identyfikatory nagłówków.

%prep
%setup -q -n markdown2-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} test/test.py

%{__python3} test/test_redos.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md CONTRIBUTORS.txt LICENSE.txt README.md TODO.txt
%attr(755,root,root) %{_bindir}/markdown2
%{py3_sitescriptdir}/markdown2.py
%{py3_sitescriptdir}/__pycache__/markdown2.cpython-*.py[co]
%{py3_sitescriptdir}/markdown2-%{version}-py*.egg-info
