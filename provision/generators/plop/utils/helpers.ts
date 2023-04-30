import * as path from "path"
import fs from "fs"

export const baseGeneratorPath = path.join(__dirname, "../../../../")
export const baseTemplatesPath = path.join(__dirname, "../templates")

export function hyphenate(data: string) {
  return data
    .replace(/([a-zA-Z])(?=[A-Z])/g, "$1-")
    .replace(":", "-")
    .toLowerCase()
}

export function pathExists(path: string) {
  return fs.existsSync(path)
}

export function pathMake(path: string) {
  if (!pathExists(path)) {
    return fs.mkdirSync(path)
  }
}
