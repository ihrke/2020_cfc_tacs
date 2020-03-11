# fixing loo() and model_weights() so that they can be called using invoke() on a list of model-objects
#
# USE: invoke(loo_wrapper, .x = models.fitted, model_names = names(models.fitted)),
#
loo_wrapper <- function(...) {
  dots <- list(...)
  if (!"x" %in% names(dots)) {
    names(dots)[1] <- "x"
  }
  do.call(brms::loo, dots)
}
model_weights_wrapper <- function(...) {
  dots <- list(...)
  if (!"x" %in% names(dots)) {
    names(dots)[1] <- "x"
  }
  do.call(brms::model_weights, dots)
}