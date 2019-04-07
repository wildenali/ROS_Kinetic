#include <highgui.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <stdio.h>
#include "opencv2/opencv.hpp"

using namespace cv;

using namespace cv;
using namespace std;

int main()
{
    Mat image;

    // Load Image
    image = imread("/home/password-admin/catkin_ws/src/ROS_Kinetic_Basics/02_Intermediate/af_opencv_cvbridge_ros/images/chess.jpg", CV_LOAD_IMAGE_COLOR);

    if (!image.data) {
        cout << "Could not open or find the image" << std::endl;
        return -1;
    }

    // DISPLAY image
    namedWindow("window", CV_WINDOW_AUTOSIZE);  // create window for display
    imshow("window", image);                    // show our image inside it.
    
    // SAVE image
    imwrite("/home/password-admin/catkin_ws/src/ROS_Kinetic_Basics/02_Intermediate/af_opencv_cvbridge_ros/images/copy-image.jpg", image);


    waitKey(0);
    return 0;
}
