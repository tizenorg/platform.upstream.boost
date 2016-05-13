%define run_tests 0
%if %{run_tests}
    # check is defined off at .rpmmacros file.
    %define check %%check
%endif

%define ver 1.58.0
%define file_version 1_58_0
%define short_version 1_58

#Only define to 1 to generate the man pages
%define build_docs 0

#Define to 0 to not package the pdf documentation
%define package_pdf 0

# Just hardcode build_mpi to 1 as soon as openmpi builds on all
# named architectures.

# TODO: make openmpi package
%define build_mpi 0

# context hasn't been ported to most architectures yet
%ifarch %ix86 x86_64 %arm mips ppc ppc64 ppc64le
%define build_context 1
%else
%define build_context 0
%endif

%ifarch hppa
%define disable_long_double 1
%else
%define disable_long_double 0
%endif

%define boost_libs1 boost-date-time boost-filesystem boost-graph
%define boost_libs2 boost-iostreams boost-math boost-test
%define boost_libs3 boost-program-options boost-python boost-serialization
%define boost_libs4 boost-signals boost-system boost-thread
%define boost_libs5 boost-wave boost-regex
%define boost_libs6 boost-random boost-chrono boost-locale
%define boost_libs7 boost-timer boost-atomic boost-log boost-container
%if %build_context
%define boost_libs_context boost-context boost-coroutine
%endif

%define most_libs %boost_libs1 %boost_libs2 %boost_libs3 %boost_libs4 %boost_libs5 %boost_libs6 %boost_libs7 %{?boost_libs_context}

%if %build_mpi
%define all_libs %{most_libs} boost-graph-parallel boost-mpi
%else
%define all_libs %{most_libs}
%endif

Name:           boost
BuildRequires:  boost-jam
BuildRequires:  dos2unix
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  expat-devel
BuildRequires:  libicu-devel
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  xz
BuildRequires:  fdupes
Url:            http://www.boost.org
Summary:        Boost C++ Libraries
License:        BSL-1.0
Group:          Base/Libraries
Version:        1.58.0
Release:        0
Source0:        %{name}_%{file_version}.tar.bz2
Source1:        boost-rpmlintrc
Source4:        existing_extra_docs
Source1001: 	boost.manifest
Source1002:     boost.pc

%define _docdir %{_datadir}/doc/packages/boost-%{version}

%description
Boost provides free peer-reviewed portable C++ source libraries. The
emphasis is on libraries that work well with the C++ Standard Library.
One goal is to establish "existing practice" and provide reference
implementations so that the Boost libraries are suitable for eventual
standardization. Some of the libraries have already been proposed for
inclusion in the C++ Standards Committee's upcoming C++ Standard
Library Technical Report.

Although Boost was begun by members of the C++ Standards Committee
Library Working Group, membership has expanded to include nearly two
thousand members of the C++ community at large.

This package is mainly needed for updating from a prior version, the
dynamic libraries are found in their respective package. For development
using Boost, you also need the boost-devel package. For documentation,
see the boost-doc package.

%package        devel
Summary:        Development package for Boost C++
Group:          Development/Libraries/C and C++
Requires:       %{all_libs}
Requires:       libstdc++-devel

%description    devel
This package contains all that is needed to develop/compile
applications that use the Boost C++ libraries. For documentation see
the documentation packages (html, man or pdf).

%package     -n boost-license
Summary:        Boost License
Group:          Development/Libraries/C and C++
Provides:       boost-license = %{version}-%{release}
BuildArch:      noarch

%description -n boost-license
This package contains the license boost is provided under.

%package        doc-html
Summary:        HTML documentation for the Boost C++ Libraries
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description    doc-html
This package contains the documentation of the boost dynamic libraries
in HTML format.

%package     -n boost-atomic
Summary:        Run-Time component of boost atomic library
Group:          System/Libraries
Requires:       boost-license

%description -n boost-atomic
Run-Time support for Boost.Atomic, a library that provides atomic data types
and operations on these data types, as well as memory ordering constraints
required for coordinating multiple threads through atomic variables.

%package     -n boost-container
Summary:        Boost::Container Runtime libraries
Group:          System/Libraries
Requires:       boost-license

%description -n boost-container
This package contains the Boost Container runtime libraries.

%package     -n boost-context
Summary:        Run-Time component of boost context switching library
Group:          System/Libraries
Requires:       boost-license

%description -n boost-context
Run-Time support for Boost.Context, a foundational library that
provides a sort of cooperative multitasking on a single thread.

%package     -n boost-coroutine
Summary:        Boost::Coroutine Runtime libraries
Group:          System/Libraries
Requires:       boost-license

%description -n boost-coroutine
This package contains the Boost Coroutine runtime libraries.

%package     -n boost-date-time
Summary:        Boost::Date.Time Runtime libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-date-time

%description -n boost-date-time
This package contains the Boost Date.Time runtime libraries.

%package     -n boost-filesystem
Summary:        Boost::Filesystem Runtime Libraries
Group:          System/Localization
Requires:       boost-license
Provides:		boost-filesystem

%description -n boost-filesystem
This package contains the Boost::Filesystem libraries.

%package     -n boost-graph
Summary:        Boost::Graph Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:		boost-graph

%description -n boost-graph
This package contains the Boost::Graph Runtime libraries.

%if %build_mpi
%package     -n boost-graph-parallel
Summary:        Boost graph::distributed runtime libraries
Group:          System/Libraries
Requires:       boost-license

%description -n boost-graph-parallel
This package contains the boost::graph::distributed runtime libraries.
%endif

%package     -n boost-iostreams
Summary:        Boost::IOStreams Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:		boost-iostreams

%description -n boost-iostreams
This package contains the Boost::IOStreams Runtime libraries.

%package     -n boost-log
Summary:        Run-Time component of boost logging library
Group:          System/Libraries
Requires:       boost-license
Provides:		boost-log

%description -n boost-log
Boost.Log library aims to make logging significantly easier for the
application developer. It provides a wide range of out-of-the-box
tools along with public interfaces for extending the library.

%package     -n boost-math
Summary:        Boost::Math Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:		boost-math

%description -n boost-math
This package contains the Boost::Math Runtime libraries.

%if %build_mpi
%package     -n boost-mpi
Summary:        Boost::MPI Runtime libraries
Group:          System/Libraries
Requires:       boost-license
Provides:		boost-mpi

%description -n boost-mpi
This package contains the Boost::MPI Runtime libraries.
%endif

%package    -n boost-test
Summary:        Boost::Test Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:		boost-test

%description -n boost-test
This package contains the Boost::Test runtime libraries.

%package     -n boost-program-options
Summary:        Boost::ProgramOptions Runtime libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-program-options

%description -n boost-program-options
This package contains the Boost::ProgramOptions Runtime libraries.


%package     -n boost-python
Summary:        Boost::Python Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-python

%description -n boost-python
This package contains the Boost::Python Runtime libraries.

%package     -n boost-serialization
Summary:        Boost::Serialization Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-serialization

%description -n boost-serialization
This package contains the Boost::Serialization Runtime libraries.

%package     -n boost-signals
Summary:        Boost::Signals Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:		boost-signals

%description -n boost-signals
This package contains the Boost::Signals Runtime libraries.

%package     -n boost-system
Summary:        Boost::System Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-system

%description -n boost-system
This package contains the Boost::System runtime libraries.

%package     -n boost-thread
Summary:        Boost::Thread Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-thread

%description -n boost-thread
This package contains the Boost::Thread runtime libraries.

%package     -n boost-wave
Summary:        Boost::Wave Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-wave

%description -n boost-wave
This package contains the Boost::Wave runtime libraries.

%package     -n boost-regex
Summary:        The Boost::Regex runtime library
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-regex

%description -n boost-regex
This package contains the Boost::Regex runtime library.

%package     -n boost-random
Summary:        The Boost::Random runtime library
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-random

%description -n boost-random
This package contains the Boost::Random runtime library.

%package     -n boost-chrono
Summary:        The Boost::Chrono runtime library
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-chrono

%description -n boost-chrono
This package contains the Boost::Chrono runtime library.

%package     -n boost-locale
Summary:        The Boost::Locale runtime library
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-locale

%description -n boost-locale
This package contains the Boost::Locale runtime library.

%package     -n boost-timer
Summary:        The Boost::Timer runtime library
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-timer

%description -n boost-timer
This package contains the Boost::Timer runtime library.


%prep
%setup -q -n %{name}_%{file_version}
cp %{SOURCE1001} .
cp %{SOURCE1002} .
#everything in the tarball has the executable flag set ...
find -type f ! \( -name \*.sh -o -name \*.py -o -name \*.pl \) -exec chmod -x {} +

#stupid build machinery copies .orig files
find . -name \*.orig -exec rm {} +

%build
find . -type f -exec chmod u+w {} +

# Create shared build instructions
cat << \EOF >.build
# Now build it
J_P=%{jobs}
J_G=$(getconf _NPROCESSORS_ONLN)
[ $J_G -gt 64 ] && J_G=64

if test -z "$JOBS"; then
  JOBS=$J_G
else
  test 1 -gt "$JOBS" && JOBS=1
fi

%if %{disable_long_double}
export LONG_DOUBLE_FLAGS="--disable-long-double"
%endif
BJAM_CONFIG="-d2 -j$JOBS -sICU_PATH=%{_prefix}"
PYTHON_VERSION=$(python -c 'import sys; print sys.version[:3]')
PYTHON_FLAGS="--with-python-root=/usr --with-python-version=$PYTHON_VERSION"
export REGEX_FLAGS="--with-icu"
export EXPAT_INCLUDE=/usr/include EXPAT_LIBPATH=%{_libdir}
export PYTHON_FLAGS
LIBRARIES_FLAGS=--with-libraries=all
%if !%build_context
# coroutine depends on context
LIBRARIES_FLAGS+=" --without-libraries=context,coroutine"
%endif
EOF

touch user-config.jam

# Read shared build instructions
. ./.build

%if %build_mpi
# Set PATH, MANPATH and LD_LIBRARY_PATH for mpi
. /var/mpi-selector/data/$(rpm --qf "%{NAME}-%{VERSION}" -q openmpi).sh
%endif

# use supplied bootstrap.sh instead of mucking with old bjam
# see also: https://svn.boost.org/trac/boost/ticket/9304
./bootstrap.sh $LIBRARIES_FLAGS \
    --prefix=%{_prefix} --exec-prefix=%{_bindir} \
    --libdir=%{_libdir} --includedir=%{_includedir}

# add specific wishes in user-config.jam
%if %build_docs
cat << EOF >user-config.jam
using xsltproc ;

using boostbook
    : /usr/share/xml/docbook/stylesheet/nwalsh/current
    : /usr/share/xml/docbook/schema/dtd/4.2
    ;

using doxygen ;
EOF
%endif

%if %build_mpi
cat << EOF >>user-config.jam
using mpi ;
EOF
%endif

# perform the compilation
./b2 %{?_smp_mflags} --prefix=%{_prefix} --libdir=%{_libdir} \
	--user-config=./user-config.jam ${CFLAGS:+cflags="$CFLAGS"} \
    ${CXXFLAGS:+cxxflags="$CXXFLAGS"} ${LDFLAGS:+linkflags="$LDFLAGS"}


%if %build_docs
cd doc
../b2 --user-config=../user-config.jam --v2 man
%endif

%check
%if %{run_tests}
BOOST_LIBS="chrono,program_options,thread,system,filesystem,date_time,regex,serialization,iostreams,random,test"
    chmod 777 ./run_test.sh
    echo "RUN run_test.sh"
    ./run_test.sh %{version} $BOOST_LIBS || exit 0
%endif

%install

# Read shared build instructions
. ./.build

%if %build_mpi
# Set PATH, MANPATH and LD_LIBRARY_PATH for mpi
. /var/mpi-selector/data/$(rpm --qf "%{NAME}-%{VERSION}" -q openmpi).sh
%endif

./b2 install \
    --prefix=%{buildroot}%{_prefix} --exec-prefix=%{buildroot}%{_bindir} \
    --libdir=%{buildroot}%{_libdir} --includedir=%{buildroot}%{_includedir} \
    --user-config=./user-config.jam

# do not install the python module - as long as noone needs it, it requires more fixes
# see https://bugzilla.redhat.com/show_bug.cgi?id=801534 for details
rm -f %{buildroot}%{_libdir}/mpi.so

mkdir -p %{buildroot}%{_docdir}

pushd %{buildroot}%{_libdir}
blibs=$(find . -name \*.so.%{version})
echo $blibs | xargs chrpath -d

for lib in ${blibs}; do
  BASE=$(basename ${lib} .so.%{version})
  SONAME_MT="$BASE-mt.so"
  ln -sf ${lib} $SONAME_MT
done
popd

# install pkgconfig file
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
install -D -m 644 %{SOURCE1002} $RPM_BUILD_ROOT%{_libdir}/pkgconfig

# install the man pages
# rm -rf doc/man/man3/boost::units::operator
# mv doc/man/man3/path.3 doc/man/man3/boost::property_tree::path.3
# mv doc/man/man3/string.3 doc/man/man3/boost::container::string.3
#
# for sec in 3 7 9; do
#     install -d %%buildroot/%%{_mandir}/man${sec}
# done
# pushd doc/man
# rm -f *.manifest
# tar -cf - .| tar -C %%{buildroot}/%%{_mandir} -xvf -
# popd

#install doc files
dos2unix libs/ptr_container/doc/tutorial_example.html \
	libs/parameter/doc/html/reference.html \
	libs/parameter/doc/html/index.html \
	libs/iostreams/doc/tree/tree.js \
	libs/graph/doc/lengauer_tarjan_dominator.htm \
	libs/test/test/test_files/errors_handling_test.pattern \
	libs/test/test/test_files/result_report_test.pattern
find . -name \*.htm\* -o -name \*.gif -o -name \*.css -o -name \*.jpg -o -name \*.png -o -name \*.ico | \
	tar --files-from=%{S:4} -cf - --files-from=- | tar -C %{buildroot}%{_docdir} -xf -
rm -rf %{buildroot}%{_docdir}/boost
ln -s /usr/include/boost %{buildroot}%{_docdir}
ln -s ../LICENSE_1_0.txt %{buildroot}%{_docdir}/libs
#Copy the news file.
#cp %%{S:5} %%{buildroot}%%{_docdir}
#only for documentation, doesn't need to be executable
find %{buildroot}%{_docdir} -name \*.py -exec chmod -x {} +

%if %package_pdf
chmod -x ../%{name}_%{short_version}_pdf/*.pdf
%endif

rm -f %{buildroot}%{_libdir}/*.a
#symlink dupes
%fdupes %buildroot

# LICENSE
mkdir -p %{buildroot}/usr/share/licenses
cp -af LICENSE_1_0.txt %{buildroot}/usr/share/licenses/%{name}

%post -n boost-atomic -p /sbin/ldconfig
%post -n boost-container -p /sbin/ldconfig
%post -n boost-context -p /sbin/ldconfig
%post -n boost-coroutine -p /sbin/ldconfig
%post -n boost-date-time -p /sbin/ldconfig
%post -n boost-filesystem -p /sbin/ldconfig
%post -n boost-iostreams -p /sbin/ldconfig
%post -n boost-log -p /sbin/ldconfig
%post -n boost-test -p /sbin/ldconfig
%post -n boost-program-options -p /sbin/ldconfig
%post -n boost-python -p /sbin/ldconfig
%post -n boost-regex -p /sbin/ldconfig
%post -n boost-serialization -p /sbin/ldconfig
%post -n boost-signals -p /sbin/ldconfig
%post -n boost-thread -p /sbin/ldconfig
%post -n boost-math -p /sbin/ldconfig
%if %build_mpi
%post -n boost-mpi -p /sbin/ldconfig
%endif
%post -n boost-graph -p /sbin/ldconfig
%post -n boost-system -p /sbin/ldconfig
%post -n boost-wave -p /sbin/ldconfig
%post -n boost-random -p /sbin/ldconfig
%post -n boost-chrono -p /sbin/ldconfig
%post -n boost-locale -p /sbin/ldconfig
%post -n boost-timer -p /sbin/ldconfig
%if %build_mpi
%post -n boost-graph-parallel -p /sbin/ldconfig
%endif

%postun -n boost-atomic -p /sbin/ldconfig
%postun -n boost-container -p /sbin/ldconfig
%postun -n boost-context -p /sbin/ldconfig
%postun -n boost-coroutine -p /sbin/ldconfig
%postun -n boost-date-time -p /sbin/ldconfig
%postun -n boost-filesystem -p /sbin/ldconfig
%postun -n boost-iostreams -p /sbin/ldconfig
%postun -n boost-log -p /sbin/ldconfig
%postun -n boost-test -p /sbin/ldconfig
%postun -n boost-program-options -p /sbin/ldconfig
%postun -n boost-python -p /sbin/ldconfig
%postun -n boost-regex -p /sbin/ldconfig
%postun -n boost-serialization -p /sbin/ldconfig
%postun -n boost-signals -p /sbin/ldconfig
%postun -n boost-thread -p /sbin/ldconfig
%postun -n boost-math -p /sbin/ldconfig
%if %build_mpi
%postun -n boost-mpi -p /sbin/ldconfig
%endif
%postun -n boost-graph -p /sbin/ldconfig
%postun -n boost-system -p /sbin/ldconfig
%postun -n boost-wave -p /sbin/ldconfig
%postun -n boost-random -p /sbin/ldconfig
%postun -n boost-chrono -p /sbin/ldconfig
%postun -n boost-locale -p /sbin/ldconfig
%postun -n boost-timer -p /sbin/ldconfig
%if %build_mpi
%postun -n boost-graph-parallel -p /sbin/ldconfig
%endif

%files
%manifest %{name}.manifest
%{_datadir}/licenses/%{name}

%files -n boost-license
%manifest %{name}.manifest
%defattr(-, root, root, -)
%dir %{_docdir}
#%%doc %%{_docdir}/NEWS
%doc %{_docdir}/LICENSE_1_0.txt

%files -n boost-atomic
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_atomic*.so.*

%files -n boost-container
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_container*.so.*

%if %build_context
%manifest %{name}.manifest
%files -n boost-context
%defattr(-, root, root, -)
%{_libdir}/libboost_context*.so.*

%files -n boost-coroutine
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_coroutine*.so.*
%endif

%files -n boost-date-time
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_date_time*.so.*

%files -n boost-filesystem
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_filesystem*.so.*

%files -n boost-graph
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_graph.so.*

%if %build_mpi
%files -n boost-graph-parallel
%manifest %{name}.manifest
%defattr(-,root,root)
%_libdir/libboost_graph_parallel.so.*
%endif

%files -n boost-iostreams
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_iostreams*.so.*

%files -n boost-log
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_log*.so.*

%files -n boost-math
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_math_*.so.*

%if %build_mpi
%manifest %{name}.manifest
%files -n boost-mpi
%defattr(-, root, root, -)
%{_libdir}/libboost_mpi*.so.*
%endif

%files -n boost-test
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_prg_exec_monitor*.so.*
%{_libdir}/libboost_unit_test_framework*.so.*

%files -n boost-program-options
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_program_options*.so.*

%files -n boost-python
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_python*.so.*

%files -n boost-serialization
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_*serialization*.so.*

%files -n boost-signals
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_signals*.so.*

%files -n boost-system
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_system*.so.*

%files -n boost-thread
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_thread*.so.*

%files -n boost-wave
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_wave*.so.*

%files -n boost-regex
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_regex*.so.*

%files -n boost-random
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_random*.so.*

%files -n boost-chrono
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_chrono*.so.*

%files -n boost-locale
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_locale*.so.*

%files -n boost-timer
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_libdir}/libboost_timer*.so.*

%files devel
%manifest %{name}.manifest
%defattr(-, root, root, -)
%{_includedir}/boost
%{_libdir}/*.so
%{_libdir}/pkgconfig/boost.pc
#%%{_datadir}/aclocal/*.m4

%files doc-html
%manifest %{name}.manifest
%defattr(-, root, root, -)
%doc %{_docdir}/*
%exclude %{_docdir}/LICENSE_1_0.txt

%if %package_pdf
%files doc-pdf
%manifest %{name}.manifest
%defattr(-, root, root, -)
%doc ../%{name}_%{short_version}_pdf/*.pdf
%endif

%changelog
