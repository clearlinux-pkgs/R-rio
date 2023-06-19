#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rio
Version  : 0.5.29
Release  : 52
URL      : https://cran.r-project.org/src/contrib/rio_0.5.29.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rio_0.5.29.tar.gz
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
BuildRequires : buildreq-R

%description
# rio: A Swiss-Army Knife for Data I/O <img src="man/figures/logo.png" align="right" height="139"/>

%prep
%setup -q -c -n rio
cd %{_builddir}/rio

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641096565

%install
export SOURCE_DATE_EPOCH=1641096565
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rio
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rio
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rio
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

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
/usr/lib64/R/library/rio/examples/example-DESCRIPTION
/usr/lib64/R/library/rio/examples/example.csvy
/usr/lib64/R/library/rio/examples/iris.xls
/usr/lib64/R/library/rio/examples/mtcars.ods
/usr/lib64/R/library/rio/examples/noheader.csv
/usr/lib64/R/library/rio/examples/twotables.html
/usr/lib64/R/library/rio/help/AnIndex
/usr/lib64/R/library/rio/help/aliases.rds
/usr/lib64/R/library/rio/help/figures/logo.png
/usr/lib64/R/library/rio/help/figures/logo.svg
/usr/lib64/R/library/rio/help/paths.rds
/usr/lib64/R/library/rio/help/rio.rdb
/usr/lib64/R/library/rio/help/rio.rdx
/usr/lib64/R/library/rio/html/00Index.html
/usr/lib64/R/library/rio/html/R.css
/usr/lib64/R/library/rio/tests/test-all.R
/usr/lib64/R/library/rio/tests/testthat/files/br-in-header.html
/usr/lib64/R/library/rio/tests/testthat/files/br-in-td.html
/usr/lib64/R/library/rio/tests/testthat/files/th-as-row-element.html
/usr/lib64/R/library/rio/tests/testthat/files/two-tbody.html
/usr/lib64/R/library/rio/tests/testthat/test_arg_reconcile.R
/usr/lib64/R/library/rio/tests/testthat/test_characterize.R
/usr/lib64/R/library/rio/tests/testthat/test_compress.R
/usr/lib64/R/library/rio/tests/testthat/test_convert.R
/usr/lib64/R/library/rio/tests/testthat/test_errors.R
/usr/lib64/R/library/rio/tests/testthat/test_export_list.R
/usr/lib64/R/library/rio/tests/testthat/test_extensions.R
/usr/lib64/R/library/rio/tests/testthat/test_format_R.R
/usr/lib64/R/library/rio/tests/testthat/test_format_arff.R
/usr/lib64/R/library/rio/tests/testthat/test_format_csv.R
/usr/lib64/R/library/rio/tests/testthat/test_format_csv_gz.R
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
/usr/lib64/R/library/rio/tests/testthat/test_install_formats.R
/usr/lib64/R/library/rio/tests/testthat/test_is_file_text.R
/usr/lib64/R/library/rio/tests/testthat/test_matrix.R
/usr/lib64/R/library/rio/tests/testthat/test_remote.R
/usr/lib64/R/library/rio/tests/testthat/test_set_class.R
