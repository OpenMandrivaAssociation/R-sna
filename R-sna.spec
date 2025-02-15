%bcond_with bootstrap
%global packname  sna
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.3.1
Release:          2
Summary:          Tools for Social Network Analysis
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/sna_2.3-1.tar.gz
Requires:         R-utils R-network R-rgl R-numDeriv R-SparseM
%if %{without bootstrap}
Requires:         R-statnet 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-utils R-network R-rgl R-numDeriv R-SparseM
%if %{without bootstrap}
BuildRequires:    R-statnet
%endif

%description
A range of tools for social network analysis, including node and
graph-level indices, structural distance and covariance methods,
structural equivalence detection, p* modeling, random graph generation,
and 2D/3D network visualization.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
