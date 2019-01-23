/***********************
 *  CUSTOM TEMPLATES   *
 ***********************/

var oppodevelopCol = 0;
var masterCol = 1;
var opensourceCol = 2;

var graphConfig = new GitGraph.Template({
  colors: [ "#9993FF", "#47E8D4", "#6BDB52", "#F85BB5", "#FFA657", "#F85BB5" ],
  branch: {
    color: "#000000",
    lineWidth: 3,
    spacingX: 60,
    mergeStyle: "straight",
    showLabel: true, // display branch names on graph
    labelFont: "normal 12pt Arial",
    labelRotation: 0
  },
  commit: {
    spacingY: -40,
    dot: {
      size: 8,
      strokeColor: "#000000",
      strokeWidth: 4,
    },
    tag: {
      font: "normal 12pt Arial",
      color: "yellow"
    },
    message: {
      color: "black",
      font: "normal 12pt Arial",
      displayAuthor: false,
      displayBranch: true,
      displayHash: true,
    }
  },
  arrow: {
    size: 8,
    offset: 2
  }
});

var config = {
  template: graphConfig,
  reverseArrow: false, // to make arrows point to ancestors, if displayed
  /*mode: "extended",*/
  orientation: "vertical"
};

var gitGraph = new GitGraph(config);

/************************
 * BRANCHES AND COMMITS *
 ************************/

var master = gitGraph.branch({
    name: "master",
    column: masterCol
});

master.commit("Initial commit");

var opensourcemaster = master.branch({
  parentBranch: master,
  name: "opensourcemaster",
  column: opensourceCol,
  color: "#F00",
  // lineDash: [5],
  commitDefaultOptions: {
    color: "#F00"
  }
});

var oppodevelop = master.branch({
  parentBranch: master,
  name: "oppodevelop",
  column: oppodevelopCol,
  color: "#deb887",
  // lineDash: [5],
  commitDefaultOptions: {
    color: "#deb887"
  }
});

// Commit on HEAD Branch which is "master"
opensourcemaster.commit("OpenSource commit 1");

oppodevelop.commit("oppodevelop commit 1")

oppodevelop.commit("oppodevelop commit 2")

// Add few commits on master
opensourcemaster.commit("OpenSource commit 2");

oppodevelop.commit({
    lineDash: [3, 2],
    dotStrokeWidth: 5,
    dotColor: "white",
    messageHashDisplay: false,
    messageAuthorDisplay: false,
    message: "Current",
    tag: "HEAD",
    displayTagBox: true
});
