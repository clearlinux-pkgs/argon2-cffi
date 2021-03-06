#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAE2536227F69F181 (hs@ox.cx)
#
Name     : argon2-cffi
Version  : 20.1.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/74/fd/d78e003a79c453e8454197092fce9d1c6099445b7e7da0b04eb4fe1dbab7/argon2-cffi-20.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/74/fd/d78e003a79c453e8454197092fce9d1c6099445b7e7da0b04eb4fe1dbab7/argon2-cffi-20.1.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/74/fd/d78e003a79c453e8454197092fce9d1c6099445b7e7da0b04eb4fe1dbab7/argon2-cffi-20.1.0.tar.gz.asc
Summary  : The secure Argon2 password hashing algorithm.
Group    : Development/Tools
License  : CC0-1.0 MIT
Requires: argon2-cffi-license = %{version}-%{release}
Requires: argon2-cffi-python = %{version}-%{release}
Requires: argon2-cffi-python3 = %{version}-%{release}
Requires: cffi
Requires: six
Provides: argon2_cffi
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
CFFI-based Argon2 Bindings for Python
        =====================================

%package license
Summary: license components for the argon2-cffi package.
Group: Default

%description license
license components for the argon2-cffi package.


%package python
Summary: python components for the argon2-cffi package.
Group: Default
Requires: argon2-cffi-python3 = %{version}-%{release}

%description python
python components for the argon2-cffi package.


%package python3
Summary: python3 components for the argon2-cffi package.
Group: Default
Requires: python3-core
Provides: pypi(argon2_cffi)
Requires: pypi(cffi)
Requires: pypi(six)

%description python3
python3 components for the argon2-cffi package.


%prep
%setup -q -n argon2-cffi-20.1.0
cd %{_builddir}/argon2-cffi-20.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597270004
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/argon2-cffi
cp %{_builddir}/argon2-cffi-20.1.0/LICENSE %{buildroot}/usr/share/package-licenses/argon2-cffi/00ff890e8493d10b07d5d3fafa23639bb071e443
cp %{_builddir}/argon2-cffi-20.1.0/extras/libargon2/LICENSE %{buildroot}/usr/share/package-licenses/argon2-cffi/edffb32348c3b38dd68cfb2e6cac9dc4a3502c8b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/argon2-cffi/00ff890e8493d10b07d5d3fafa23639bb071e443
/usr/share/package-licenses/argon2-cffi/edffb32348c3b38dd68cfb2e6cac9dc4a3502c8b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
