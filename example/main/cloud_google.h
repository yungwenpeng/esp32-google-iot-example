/**
 * @file cloud_google.h
 */

#ifndef PRJ_CLOUD_MODULE
#define PRJ_CLOUD_MODULE

/*! Identifier of the log messages produced by the application */
#define CLOUD_TAG "app_cloud"

#define DEVICE_PATH "projects/%s/locations/%s/registries/%s/devices/%s"
#define SUBSCRIBE_TOPIC_COMMAND "/devices/%s/commands/#"
#define SUBSCRIBE_TOPIC_CONFIG "/devices/%s/config"
#define PUBLISH_TOPIC_EVENT "/devices/%s/events"
#define PUBLISH_TOPIC_STATE "/devices/%s/state"

void cloud_start(void);

#endif /* PRJ_CLOUD_MODULE */
