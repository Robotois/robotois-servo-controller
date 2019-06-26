{
  "targets": [
    {
      "target_name": "ServosModule",
      "sources": [
        "src/wrapper/addon.cpp",
        "src/wrapper/ServosWrapper.cpp",
        "src/lib/Servos.cpp",
        "src/lib/robotois-PCA9685/PCA9685.cpp",
      ],
      "libraries": ["-l bcm2835","-l rt"]
    }
  ]
}
