// Generated by gencpp from file cam_test/ImageSrv.msg
// DO NOT EDIT!


#ifndef CAM_TEST_MESSAGE_IMAGESRV_H
#define CAM_TEST_MESSAGE_IMAGESRV_H

#include <ros/service_traits.h>


#include <cam_test/ImageSrvRequest.h>
#include <cam_test/ImageSrvResponse.h>


namespace cam_test
{

struct ImageSrv
{

typedef ImageSrvRequest Request;
typedef ImageSrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct ImageSrv
} // namespace cam_test


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::cam_test::ImageSrv > {
  static const char* value()
  {
    return "ba55116f263d40ea8759822097ad63d4";
  }

  static const char* value(const ::cam_test::ImageSrv&) { return value(); }
};

template<>
struct DataType< ::cam_test::ImageSrv > {
  static const char* value()
  {
    return "cam_test/ImageSrv";
  }

  static const char* value(const ::cam_test::ImageSrv&) { return value(); }
};


// service_traits::MD5Sum< ::cam_test::ImageSrvRequest> should match 
// service_traits::MD5Sum< ::cam_test::ImageSrv > 
template<>
struct MD5Sum< ::cam_test::ImageSrvRequest>
{
  static const char* value()
  {
    return MD5Sum< ::cam_test::ImageSrv >::value();
  }
  static const char* value(const ::cam_test::ImageSrvRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::cam_test::ImageSrvRequest> should match 
// service_traits::DataType< ::cam_test::ImageSrv > 
template<>
struct DataType< ::cam_test::ImageSrvRequest>
{
  static const char* value()
  {
    return DataType< ::cam_test::ImageSrv >::value();
  }
  static const char* value(const ::cam_test::ImageSrvRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::cam_test::ImageSrvResponse> should match 
// service_traits::MD5Sum< ::cam_test::ImageSrv > 
template<>
struct MD5Sum< ::cam_test::ImageSrvResponse>
{
  static const char* value()
  {
    return MD5Sum< ::cam_test::ImageSrv >::value();
  }
  static const char* value(const ::cam_test::ImageSrvResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::cam_test::ImageSrvResponse> should match 
// service_traits::DataType< ::cam_test::ImageSrv > 
template<>
struct DataType< ::cam_test::ImageSrvResponse>
{
  static const char* value()
  {
    return DataType< ::cam_test::ImageSrv >::value();
  }
  static const char* value(const ::cam_test::ImageSrvResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // CAM_TEST_MESSAGE_IMAGESRV_H
