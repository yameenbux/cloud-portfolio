provider "local" {}

resource "local_file" "example" {
  filename = "${path.module}/hello.txt"
  content  = "Buzzfuly was here 🚀"
}
