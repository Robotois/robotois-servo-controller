// addon.cc
#include <node.h>
#include "ServosWrapper.h"

namespace demo {

using v8::Local;
using v8::Object;

void InitAll(Local<Object> exports) {
  ServosWrapper::Init(exports);
}

NODE_MODULE(Servos, InitAll)

}  // namespace demo