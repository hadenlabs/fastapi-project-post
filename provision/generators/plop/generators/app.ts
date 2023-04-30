import { Actions, PlopGeneratorConfig } from "node-plop"
import * as path from "path"
import slugify from "slugify"
import { baseGeneratorPath, baseTemplatesPath, pathMake } from "../utils"
import { AnswersApp, AppPromptNames } from "./entities"

const appGeneratorPath = path.join(baseGeneratorPath, "app", "v1")

export const appGenerator: PlopGeneratorConfig = {
  description: "add an model app",
  prompts: [
    {
      type: "input",
      name: AppPromptNames.modelName,
      message: "What should it be name model?",
      default: "name"
    },
    {
      type: "input",
      name: AppPromptNames.nameTable,
      message: "What should it be name table?",
      default: "name"
    }
  ],
  actions: (data) => {
    const answers = data as AnswersApp

    const appTemplatesPath = path.join(baseTemplatesPath, "app")

    const actions: Actions = []

    actions.push({
      type: "add",
      templateFile: `${appTemplatesPath}/model.add.hbs`,
      path: `${appGeneratorPath}/model/${answers.modelName}_model.py`,
      abortOnFail: false
    })

    actions.push({
      type: "add",
      templateFile: `${appTemplatesPath}/router.add.hbs`,
      path: `${appGeneratorPath}/router/${answers.modelName}_router.py`,
      abortOnFail: false
    })

    actions.push({
      type: "add",
      templateFile: `${appTemplatesPath}/service.add.hbs`,
      path: `${appGeneratorPath}/service/${answers.modelName}_service.py`,
      abortOnFail: false
    })

    actions.push({
      type: "add",
      templateFile: `${appTemplatesPath}/schema.add.hbs`,
      path: `${appGeneratorPath}/schema/${answers.modelName}_schema.py`,
      abortOnFail: false
    })

    return actions
  }
}
