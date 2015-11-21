SCRIPTDIR=$PWD
PREFIX=$SCRIPTDIR/opencv3.0/

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
    ..

make -j4
make install


ln -ls $PREFIX/lib/python3.4/site-packages/cv2*.so \
       $VIRTUAL_ENV/lib/python3.4/site-packages/cv2.so
