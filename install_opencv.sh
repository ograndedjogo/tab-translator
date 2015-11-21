SCRIPTDIR=$PWD
PREFIX=$SCRIPTDIR/opencv3.0
SYSTEM_PYTHON34=/opt/python/3.4.2

cd $SCRIPTDIR
git clone https://github.com/Itseez/opencv_contrib.git
cd opencv_contrib
git checkout 3.0.0

cd $SCRIPTDIR
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout 3.0.0
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX= $PREFIX\
    -D OPENCV_EXTRA_MODULES_PATH=$SCRIPTDIR/opencv_contrib/modules \
    -D BUILD_opencv_python3=ON \
    -D PYTHON3_PACKAGES_PATH=$VIRTUAL_ENV/lib/python3.4/site-packages \
    -D PYTHON3_LIBRARY=$SYSTEM_PYTHON34/lib/libpython3.4m.so \
    -D PYTHON3_INCLUDE_DIR=$SYSTEM_PYTHON34/include/python3.4m \
    -D WITH_GTK=OFF \
    -D INSTALL_C_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_opencv_java=OFF
    -D BUILD_opencv_test_java=OFF
    -D BUILD_FAT_JAVA_LIB=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D BUILD_DOCS=OFF \
    ..

make -j4
make install


ln -ls $PREFIX/lib/python3.4/site-packages/cv2*.so \
       $VIRTUAL_ENV/lib/python3.4/site-packages/cv2.so
