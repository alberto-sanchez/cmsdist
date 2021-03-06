### RPM external flex 2.6.0
Source: http://iweb.dl.sourceforge.net/project/flex/flex-%{realversion}.tar.bz2

Patch0: gcc-flex-nonfull-path-m4
Patch1: gcc-flex-disable-doc

BuildRequires: autotools bison

%prep
%setup -q -n %{n}-%{realversion}
%patch0 -p1
%patch1 -p1

%build
./configure --disable-dependency-tracking --disable-nls \
            --build=%{_build} --host="%{_host}" --prefix=%{i}
make %{makeprocesses}

%install
make install

%define drop_files %{i}/share
