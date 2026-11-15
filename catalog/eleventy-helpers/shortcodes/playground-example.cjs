/**
 * @license
 * Copyright 2023 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

/**
 * Will render a playground example with a project.json in the
 * `/catalog/stories/${dirname}/` directory.
 *
 * This shorcode takes the following arguments:
 * - dirname: (required) The name of the directory where the project.json is
 *   located
 * - id: (optional) The id of the project. This is used to identify the project on pages
 *   with multiple playground examples.
 * - previewHeight: (optional) The height of the preview window. Defaults to `400`.
 * - editorHeight: (optional) The height of the editor window. Defaults to `500`.
 *
 * @example
 * ```html
 * <!--
 *   Will generate a playground example located at
 *   /catalog/stories/checkbox/project.json
 *   and give the project the id "example1"
 * -->
 * {% playgroundexample dirname="checkbox", id="example2", previewHeight="400", editorHeight="500" %}
 * ```
 *
 * @param eleventyConfig The 11ty config in which to attach this shortcode.
 */
function playgroundExample(eleventyConfig) {
  eleventyConfig.addShortcode('playgroundexample', (config) => {
    let { id, dirname } = config;
    if (!dirname) {
      throw new Error('No dirname provided to playgroundexample shortcode');
    }

    id ||= 'project';

    const previewHeight = config.previewHeight
      ? `height: ${config.previewHeight}px`
      : 'height: 400px;';
    const editorHeight = config.editorHeight
      ? `height: ${config.editorHeight}px`
      : 'height: 500px;';

    return `
      <div class="tb-playground-accordion-wrap">
        <details class="tb-playground-details">
          <summary class="tb-playground-summary">
            <div class="tb-summary-left">
              <md-outlined-icon-button toggle tabindex="-1" aria-hidden="true" class="tb-summary-toggle">
                <md-icon aria-hidden="true">expand_more</md-icon>
                <md-icon aria-hidden="true" slot="selected">expand_less</md-icon>
              </md-outlined-icon-button>
              <div class="tb-summary-text-wrap">
                <div class="tb-summary-title">
                  <span>토스뱅크 실시간 인터랙티브 데모</span>
                  <span class="tb-playground-badge" style="background: #0064FF; color: #FFFFFF;">TB Playground</span>
                </div>
                <span class="tb-summary-desc">다양한 옵션 조합과 코드를 실시간으로 테스트하고 편집해볼 수 있습니다.</span>
              </div>
            </div>
          </summary>
          <div class="tb-playground-inner">
            <lit-island on:visible import="/js/hydration-entrypoints/playground-elements.js" class="example" aria-hidden="true">
              <playground-project
                  id="${id}" project-src="/assets/stories/${dirname}/project.json">
              <playground-preview
                  style="${previewHeight}"
                  project="${id}"
              ><md-circular-progress indeterminate></md-circular-progress></playground-preview>
              <playground-file-editor
                style="${editorHeight}"
                project="${id}"
                filename="stories.ts"
                line-numbers
              ><md-circular-progress indeterminate></md-circular-progress></playground-file-editor>
            </playground-project>
            </lit-island>
          </div>
        </details>
        <div class="tb-playground-footer">
          <a href="./stories/" target="_blank" class="tb-newtab-link">
            새 탭에서 인터랙티브 데모 전체화면으로 열기 ↗
          </a>
        </div>
      </div>
    `;
  });
}

module.exports = playgroundExample;
