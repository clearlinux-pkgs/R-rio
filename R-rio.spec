#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rio
Version  : 0.5.10
Release  : 5
URL      : https://cran.r-project.org/src/contrib/rio_0.5.10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rio_0.5.10.tar.gz
Summary  : A Swiss-Army Knife for Data I/O
Group    : Development/Tools
License  : GPL-2.0
Requires: R-curl
Requires: R-data.table
Requires: R-haven
Requires: R-openxlsx
Requires: R-readxl
Requires: R-tibble
BuildRequires : R-curl
BuildRequires : R-data.table
BuildRequires : R-haven
BuildRequires : R-openxlsx
BuildRequires : R-readxl
BuildRequires : R-tibble
BuildRequires : clr-R-helpers

%description
# rio: A Swiss-Army Knife for Data I/O
The aim of **rio** is to make data file I/O in R as easy as possible by implementing four simple functions in Swiss-army knife style:

%prep
%setup -q -c -n rio

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522686222

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1522686222
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rio
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rio
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rio
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rio|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rio/CITATION
/usr/lib64/R/library/rio/DESCRIPTION
/usr/lib64/R/library/rio/INDEX
/usr/lib64/R/library/rio/Meta/Rd.rds
/usr/lib64/R/library/rio/Meta/features.rds
/usr/lib64/R/library/rio/Meta/hsearch.rds
/usr/lib64/R/library/rio/Meta/links.rds
/usr/lib64/R/library/rio/Meta/nsInfo.rds
/usr/lib64/R/library/rio/Meta/package.rds
/usr/lib64/R/library/rio/Meta/vignette.rds
/usr/lib64/R/library/rio/NAMESPACE
/usr/lib64/R/library/rio/NEWS.md
/usr/lib64/R/library/rio/R/rio
/usr/lib64/R/library/rio/R/rio.rdb
/usr/lib64/R/library/rio/R/rio.rdx
/usr/lib64/R/library/rio/doc/index.html
/usr/lib64/R/library/rio/doc/rio.R
/usr/lib64/R/library/rio/doc/rio.html
/usr/lib64/R/library/rio/examples/example.csvy
/usr/lib64/R/library/rio/examples/mtcars.ods
/usr/lib64/R/library/rio/examples/noheader.csv
/usr/lib64/R/library/rio/examples/twotables.html
/usr/lib64/R/library/rio/help/AnIndex
/usr/lib64/R/library/rio/help/aliases.rds
/usr/lib64/R/library/rio/help/paths.rds
/usr/lib64/R/library/rio/help/rio.rdb
/usr/lib64/R/library/rio/help/rio.rdx
/usr/lib64/R/library/rio/html/00Index.html
/usr/lib64/R/library/rio/html/R.css
