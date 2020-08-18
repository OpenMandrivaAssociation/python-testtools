%global srcname testtools
%global __requires_exclude fixtures

Name:           python-%{srcname}
Version:        2.4.0
Release:        1
Summary:        Extensions to the Python standard library unit testing framework

Group:          Development/Python
License:        MIT
URL:            https://github.com/testing-cabal/testtools
Source0:        https://pypi.io/packages/source/t/%{srcname}/%{srcname}-%version.tar.gz
Patch0:         testtools-1.8.0-py3.patch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:	python3dist(pbr)
%{?python_provide:%python_provide python3-%{srcname}}
BuildArch:      noarch
Requires:       python3dist(python-mimeparse)
Requires:       python3dist(traceback2)
Requires:       python3dist(unittest2)

%description
testtools is a set of extensions to the Python standard library’s unit
testing framework. These extensions have been derived from many years
of experience with unit testing in Python and come from many different
sources.

%prep
%setup -q -n %{srcname}-%{version}

# make the Python 3 build load the Python 3.x compatibility library directly
%patch0 -p1 -b .py3

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
rm testtools/_compat2x.py

%build
%py_build

%install
%py_install

%files
%doc AUTHORS ChangeLog README.rst
%{python_sitelib}/%{srcname}
%{python_sitelib}/%{srcname}-%{version}-py%{python_version}.egg-info
