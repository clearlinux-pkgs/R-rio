#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-rio
Version  : 1.2.3
Release  : 63
URL      : https://cran.r-project.org/src/contrib/rio_1.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rio_1.2.3.tar.gz
Summary  : A Swiss-Army Knife for Data I/O
Group    : Development/Tools
License  : GPL-2.0
Requires: R-R.utils
Requires: R-curl
Requires: R-data.table
Requires: R-haven
Requires: R-lifecycle
Requires: R-readr
Requires: R-readxl
Requires: R-tibble
Requires: R-writexl
BuildRequires : R-R.utils
BuildRequires : R-curl
BuildRequires : R-data.table
BuildRequires : R-haven
BuildRequires : R-lifecycle
BuildRequires : R-readr
BuildRequires : R-readxl
BuildRequires : R-tibble
BuildRequires : R-writexl
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# rio: A Swiss-Army Knife for Data I/O <img src="man/figures/logo.png" align="right" height="139"/>

%prep
%setup -q -n rio
pushd ..
cp -a rio buildavx2
popd
pushd ..
cp -a rio buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727297348

%install
export SOURCE_DATE_EPOCH=1727297348
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/rio/R/sysdata.rdb
/usr/lib64/R/library/rio/R/sysdata.rdx
/usr/lib64/R/library/rio/doc/extension.R
/usr/lib64/R/library/rio/doc/extension.Rmd
/usr/lib64/R/library/rio/doc/extension.html
/usr/lib64/R/library/rio/doc/index.html
/usr/lib64/R/library/rio/doc/labelled.R
/usr/lib64/R/library/rio/doc/labelled.Rmd
/usr/lib64/R/library/rio/doc/labelled.html
/usr/lib64/R/library/rio/doc/philosophy.Rmd
/usr/lib64/R/library/rio/doc/philosophy.html
/usr/lib64/R/library/rio/doc/remap.R
/usr/lib64/R/library/rio/doc/remap.Rmd
/usr/lib64/R/library/rio/doc/remap.html
/usr/lib64/R/library/rio/doc/rio.R
/usr/lib64/R/library/rio/doc/rio.Rmd
/usr/lib64/R/library/rio/doc/rio.html
/usr/lib64/R/library/rio/help/AnIndex
/usr/lib64/R/library/rio/help/aliases.rds
/usr/lib64/R/library/rio/help/figures/logo.png
/usr/lib64/R/library/rio/help/figures/logo.svg
/usr/lib64/R/library/rio/help/paths.rds
/usr/lib64/R/library/rio/help/rio.rdb
/usr/lib64/R/library/rio/help/rio.rdx
/usr/lib64/R/library/rio/html/00Index.html
/usr/lib64/R/library/rio/html/R.css
/usr/lib64/R/library/rio/tests/testdata/br-in-header.html
/usr/lib64/R/library/rio/tests/testdata/br-in-td.html
/usr/lib64/R/library/rio/tests/testdata/example.csvy
/usr/lib64/R/library/rio/tests/testdata/iris.xls
/usr/lib64/R/library/rio/tests/testdata/iris_no_extension_xls
/usr/lib64/R/library/rio/tests/testdata/mtcars.ods
/usr/lib64/R/library/rio/tests/testdata/noheader.csv
/usr/lib64/R/library/rio/tests/testdata/th-as-row-element.html
/usr/lib64/R/library/rio/tests/testdata/two-tbody.html
/usr/lib64/R/library/rio/tests/testdata/twotables.html
/usr/lib64/R/library/rio/tests/testthat.R
/usr/lib64/R/library/rio/tests/testthat/test_characterize.R
/usr/lib64/R/library/rio/tests/testthat/test_check_file.R
/usr/lib64/R/library/rio/tests/testthat/test_compress.R
/usr/lib64/R/library/rio/tests/testthat/test_convert.R
/usr/lib64/R/library/rio/tests/testthat/test_create_outfiles.R
/usr/lib64/R/library/rio/tests/testthat/test_errors.R
/usr/lib64/R/library/rio/tests/testthat/test_export_corner_cases.R
/usr/lib64/R/library/rio/tests/testthat/test_export_list.R
/usr/lib64/R/library/rio/tests/testthat/test_extensions.R
/usr/lib64/R/library/rio/tests/testthat/test_format_R.R
/usr/lib64/R/library/rio/tests/testthat/test_format_arff.R
/usr/lib64/R/library/rio/tests/testthat/test_format_csv.R
/usr/lib64/R/library/rio/tests/testthat/test_format_csvy.R
/usr/lib64/R/library/rio/tests/testthat/test_format_dbf.R
/usr/lib64/R/library/rio/tests/testthat/test_format_dif.R
/usr/lib64/R/library/rio/tests/testthat/test_format_dta.R
/usr/lib64/R/library/rio/tests/testthat/test_format_eviews.R
/usr/lib64/R/library/rio/tests/testthat/test_format_external_packages.R
/usr/lib64/R/library/rio/tests/testthat/test_format_feather.R
/usr/lib64/R/library/rio/tests/testthat/test_format_fortran.R
/usr/lib64/R/library/rio/tests/testthat/test_format_fst.R
/usr/lib64/R/library/rio/tests/testthat/test_format_fwf.R
/usr/lib64/R/library/rio/tests/testthat/test_format_html.R
/usr/lib64/R/library/rio/tests/testthat/test_format_json.R
/usr/lib64/R/library/rio/tests/testthat/test_format_matlab.R
/usr/lib64/R/library/rio/tests/testthat/test_format_mtp.R
/usr/lib64/R/library/rio/tests/testthat/test_format_ods.R
/usr/lib64/R/library/rio/tests/testthat/test_format_parquet.R
/usr/lib64/R/library/rio/tests/testthat/test_format_psv.R
/usr/lib64/R/library/rio/tests/testthat/test_format_pzfx.R
/usr/lib64/R/library/rio/tests/testthat/test_format_qs.R
/usr/lib64/R/library/rio/tests/testthat/test_format_rdata.R
/usr/lib64/R/library/rio/tests/testthat/test_format_rds.R
/usr/lib64/R/library/rio/tests/testthat/test_format_rec.R
/usr/lib64/R/library/rio/tests/testthat/test_format_sas.R
/usr/lib64/R/library/rio/tests/testthat/test_format_sav.R
/usr/lib64/R/library/rio/tests/testthat/test_format_syd.R
/usr/lib64/R/library/rio/tests/testthat/test_format_tsv.R
/usr/lib64/R/library/rio/tests/testthat/test_format_xls.R
/usr/lib64/R/library/rio/tests/testthat/test_format_xml.R
/usr/lib64/R/library/rio/tests/testthat/test_format_yml.R
/usr/lib64/R/library/rio/tests/testthat/test_gather_attrs.R
/usr/lib64/R/library/rio/tests/testthat/test_guess.R
/usr/lib64/R/library/rio/tests/testthat/test_identical.R
/usr/lib64/R/library/rio/tests/testthat/test_import_list.R
/usr/lib64/R/library/rio/tests/testthat/test_mapping.R
/usr/lib64/R/library/rio/tests/testthat/test_matrix.R
/usr/lib64/R/library/rio/tests/testthat/test_remote.R
/usr/lib64/R/library/rio/tests/testthat/test_set_class.R
/usr/lib64/R/library/rio/tests/testthat/test_suggestions.R
/usr/lib64/R/library/rio/tests/testthat/test_trust.R
