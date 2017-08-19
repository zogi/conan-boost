from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="lasote", channel="stable", args="--build=missing")
    builder.add_common_builds(shared_option_name="Boost:shared")
    builder.run()
