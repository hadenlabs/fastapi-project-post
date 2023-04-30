import { NodePlopAPI } from "node-plop"
import helpers from "handlebars-helpers"
import { appGenerator } from "./generators"
import shell from "shelljs"
import slugify from "slugify"
import { hyphenate } from "./utils"
interface PrettifyCustomActionData {
  path: string
}

export default function plop(plop: NodePlopAPI) {
  plop.setHelper("eq", helpers().eq)
  plop.setHelper("slugify", slugify)
  plop.setHelper("hyphenate", hyphenate)
  plop.setGenerator("react", appGenerator)
  plop.setActionType("prettify", (_, config) => {
    const data = config.data as PrettifyCustomActionData
    shell.exec(`yarn prettier:fix -- "${data.path}"`, { silent: true })
    return ""
  })
}
