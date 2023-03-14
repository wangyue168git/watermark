#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

// 将字符串转换为二进制形式
vector<bool> stringToBinary(string str) {
    vector<bool> binary;
    for (char c : str) {
        for (int i = 0; i < 8; i++) {
            binary.push_back(c & (1 << i));
        }
    }
    return binary;
}

// 将二进制形式的水印转换为字符串
string binaryToString(const vector<bool>& binary) {
    string str;
    for (int i = 0; i < binary.size(); i += 8) {
        char c = 0;
        for (int j = 0; j < 8; j++) {
            c |= binary[i + j] << j;
        }
        str += c;
    }
    return str;
}

// 嵌入水印
void embedWatermark(Mat& img, const vector<bool>& watermark) {
    int watermarkSize = watermark.size();
    double alpha = 0.01;  // 嵌入强度
    int index = 0;
    for (int i = 0; i < img.rows; i++) {
        for (int j = 0; j < img.cols; j++) {
            if (index >= watermarkSize) {
                return;
            }
            uchar& pixel = img.at<uchar>(i, j);
            if (watermark[index]) {
                pixel |= 1 << 0;
            } else {
                pixel &= ~(1 << 0);
            }
            index++;
        }
    }
}

// 提取水印
vector<bool> extractWatermark(const Mat& img, int watermarkSize) {
    vector<bool> watermark(watermarkSize);
    int index = 0;
    for (int i = 0; i < img.rows; i++) {
        for (int j = 0; j < img.cols; j++) {
            if (index >= watermarkSize) {
                return watermark;
            }
            uchar pixel = img.at<uchar>(i, j);
            watermark[index] = (pixel & (1 << 0)) != 0;
            index++;
        }
    }
    return watermark;
}

int main() {
    string str = "Hello World!";  // 要嵌入的字符串水印
    vector<bool> watermark = stringToBinary(str);  // 将字符串转换为二进制形式
    Mat img = imread("pic/ori_img.jpeg", IMREAD_GRAYSCALE);  // 读取灰度图像
    embedWatermark(img, watermark);  // 嵌入水印
    vector<bool> extractedWatermark = extractWatermark(img, watermark.size());  // 提取水印
    string extractedStr = binaryToString(extractedWatermark);  // 将提取的水印转换为字符串
    cout << "Extracted Watermark: " << extractedStr << endl;  // 输出提取的水印
    return 0;
}