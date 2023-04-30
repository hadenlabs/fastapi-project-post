export enum AppPromptNames {
  "modelName" = "modelName",
  "nameTable" = "nameTable"
}

export type AnswersApp = { [P in AppPromptNames]: string }
