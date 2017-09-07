/*
 * Fuel UX Tree
 * https://github.com/ExactTarget/fuelux
 *
 * Copyright (c) 2014 ExactTarget
 * Licensed under the BSD New license.
 */
!function (a) {
	"function" == typeof define && define.amd ? define(["jquery"], a) : "object" == typeof exports ? module.exports = a(require("jquery")) : a(jQuery)
}
(function (a) {
	function b(a, b, c) {
		b.addClass("tree-selected"),
		"item" === b.data("type") && c.hasClass(a.options["unselected-icon"]) && c.removeClass(a.options["unselected-icon"]).addClass(a.options["selected-icon"])
	}
	function c(a, b, c) {
		b.removeClass("tree-selected"),
		"item" === b.data("type") && c.hasClass(a.options["selected-icon"]) && c.removeClass(a.options["selected-icon"]).addClass(a.options["unselected-icon"])
	}
	function d(d, e, f) {
		a.each(f.$elements, function (b, c) {
			var d = a(c);
			d[0] !== e.$element[0] && f.dataForEvent.push(a(d).data())
		}),
		e.$element.hasClass("tree-selected") ? (c(d, e.$element, e.$icon), f.eventType = "deselected") : (b(d, e.$element, e.$icon), f.eventType = "selected", f.dataForEvent.push(e.elementData))
	}
	function e(a, d, e) {
		if (e.$elements[0] !== d.$element[0]) {
			a.deselectAll(a.$element);
			b(a, d.$element, d.$icon),
			e.eventType = "selected",
			e.dataForEvent = [d.elementData]
		} else
			c(a, d.$element, d.$icon), e.eventType = "deselected", e.dataForEvent = []
	}
	var f = a.fn.tree,
	g = function (b, c) {
		this.$element = a(b),
		this.options = a.extend({}, a.fn.tree.defaults, c),
		this.options.itemSelect && this.$element.on("click.fu.tree", ".tree-item", a.proxy(function (a) {
				this.selectItem(a.currentTarget)
			}, this)),
		this.$element.on("click.fu.tree", ".tree-branch-header", a.proxy(function (a) {
				this.options.folderSelect || this.toggleFolder(a.currentTarget)
			}, this)),
		this.$element.on("click.fu.tree", ".tree-overflow", a.proxy(function (b) {
				this.populate(a(b.currentTarget))
			}, this)),
		this.options.folderSelect && (this.$element.addClass("tree-folder-select"), this.$element.off("click.fu.tree", ".tree-branch-name"), this.$element.on("click.fu.tree", ".icon-caret", a.proxy(function (b) {
					this.toggleFolder(a(b.currentTarget).next())
				}, this)), this.$element.on("click.fu.tree", ".tree-branch-header", a.proxy(function (b) {
					this.selectFolder(a(b.currentTarget))
				}, this))),
		this.render()
	};
	g.prototype = {
		constructor : g,
		deselectAll : function (b) {
			b = b || this.$element;
			var d = a(b).find(".tree-selected"),
			e = this;
			return d.each(function (b, d) {
				c(e, a(d), a(d).find("." + a.trim(e.options["base-icon"]).replace(/(\s+)/g, ".")))
			}),
			d
		},
		destroy : function () {
			return this.$element.find("li:not([data-template])").remove(),
			this.$element.remove(),
			this.$element[0].outerHTML
		},
		render : function () {
			this.populate(this.$element)
		},
		populate : function (b, c) {
                        console.log("haoi")
			var d = this,
			e = b.hasClass("tree-overflow"),
			f = b.hasClass("tree") ? b : b.parent(),
			g = f.hasClass("tree");
			e && !g && (f = f.parent());
			var h = f.data();
                   
			e && (h.overflow = b.data()),
			c = c || !1,
			e && (g ? b.replaceWith(f.find("> .tree-loader").remove()) : b.remove());
			var i = f.find(".tree-loader:last");
			c === !1 && i.removeClass("hide hidden"),
			this.options.dataSource(h ? h : {}, function (b) {
				a.each(b.data, function (b, c) {
					var e;
					if ("folder" === c.type) {
						e = d.$element.find("[data-template=treebranch]:eq(0)").clone().removeClass("hide hidden").removeData("template").removeAttr("data-template"),
						e.data(c),
                                                e.attr("id", c.id);
						e.find(".tree-branch-name > .tree-label").html(c.text || c.name);
						var h = e.find(".tree-branch-header");
						"icon-class" in c && h.find("i").addClass(c["icon-class"]),
						"additionalParameters" in c && "item-selected" in c.additionalParameters && 1 == c.additionalParameters["item-selected"] && setTimeout(function () {
							h.trigger("click")
						}, 0)
					} else
                                          
						"item" === c.type ? (e = d.$element.find("[data-template=treeitem]:eq(0)").clone().removeClass("hide hidden").removeData("template").removeAttr("data-template"), e.attr("id", c.id), e.find(".tree-item-name > .tree-label").html(c.text || c.name), e.data(c), "additionalParameters" in c && "item-selected" in c.additionalParameters && 1 == c.additionalParameters["item-selected"] && (e.addClass("tree-selected"), e.find("i").removeClass(d.options["unselected-icon"]).addClass(d.options["selected-icon"]))) : "overflow" === c.type && (e = d.$element.find("[data-template=treeoverflow]:eq(0)").clone().removeClass("hide hidden").removeData("template").removeAttr("data-template"), e.find(".tree-overflow-name > .tree-label").html(c.text || c.name), e.data(c));
					var i = c.attr || c.dataAttributes || [];
					a.each(i, function (a, b) {
						switch (a) {
						case "cssClass":
						case "class":
						case "className":
							e.addClass(b);
							break;
						case "data-icon":
							e.find(".icon-item").removeClass().addClass("icon-item " + b),
							e.attr(a, b);
							break;
						case "id":
							e.attr(a, b),
							e.attr("aria-labelledby", b + "-label"),
							e.find(".tree-branch-name > .tree-label").attr("id", b + "-label");
							break;
						default:
							e.attr(a, b)
						}
					}),
					g ? f.append(e) : f.find(".tree-branch-children:eq(0)").append(e)
				}),
				f.find(".tree-loader").addClass("hidden"),
				d.$element.trigger("loaded.fu.tree", f)
			})
		},
		selectTreeNode : function (b, c) {
			var f = {};
			f.$element = a(b);
			var g = {};
			g.$elements = this.$element.find(".tree-selected"),
			g.dataForEvent = [],
			"folder" === c ? (f.$element = f.$element.closest(".tree-branch"), f.$icon = f.$element.find(".icon-folder")) : f.$icon = f.$element.find(".icon-item"),
			f.elementData = f.$element.data(),
			this.options.multiSelect ? d(this, f, g) : e(this, f, g),
			this.$element.trigger(g.eventType + ".fu.tree", {
				target : f.elementData,
				selected : g.dataForEvent
			}),
			f.$element.trigger("updated.fu.tree", {
				selected : g.dataForEvent,
				item : f.$element,
				eventType : g.eventType
			})
		},
		discloseFolder : function (b) {
			var c = a(b),
			d = c.closest(".tree-branch"),
			e = d.find(".tree-branch-children"),
			f = e.eq(0);
			d.addClass("tree-open"),
			d.attr("aria-expanded", "true"),
			f.removeClass("hide hidden"),
			d.find("> .tree-branch-header .icon-folder").eq(0).removeClass(this.options["close-icon"]).addClass(this.options["open-icon"]),
			d.find("> .icon-caret").eq(0).removeClass(this.options["folder-open-icon"]).addClass(this.options["folder-close-icon"]),
			e.children().length || this.populate(e),
			this.$element.trigger("disclosedFolder.fu.tree", d.data())
		},
		closeFolder : function (b) {
			var c = a(b),
			d = c.closest(".tree-branch"),
			e = d.find(".tree-branch-children"),
			f = e.eq(0);
			d.removeClass("tree-open"),
			d.attr("aria-expanded", "false"),
			f.addClass("hidden"),
			d.find("> .tree-branch-header .icon-folder").eq(0).removeClass(this.options["open-icon"]).addClass(this.options["close-icon"]),
			d.find("> .icon-caret").eq(0).removeClass(this.options["folder-close-icon"]).addClass(this.options["folder-open-icon"]),
			this.options.cacheItems || f.empty(),
			this.$element.trigger("closed.fu.tree", d.data())
		},
		toggleFolder : function (b) {
			var c = a(b);
			c.find("." + a.trim(this.options["close-icon"]).replace(/(\s+)/g, ".")).length ? this.discloseFolder(b) : c.find("." + a.trim(this.options["open-icon"]).replace(/(\s+)/g, ".")).length && this.closeFolder(b)
		},
		selectFolder : function (a) {
			this.options.folderSelect && this.selectTreeNode(a, "folder")
		},
		selectItem : function (a) {
			this.options.itemSelect && this.selectTreeNode(a, "item")
		},
		selectedItems : function () {
			var b = this.$element.find(".tree-selected"),
			c = [];
			return a.each(b, function (b, d) {
				c.push(a(d).data())
			}),
			c
		},
		collapse : function () {
			var a = this,
			b = [],
			c = function d(c, e) {
				b.push(e),
				0 === a.$element.find(".tree-branch.tree-open:not('.hidden, .hide')").length && (a.$element.trigger("closedAll.fu.tree", {
						tree : a.$element,
						reportedClosed : b
					}), a.$element.off("loaded.fu.tree", a.$element, d))
			};
			a.$element.on("closed.fu.tree", c),
			a.$element.find(".tree-branch.tree-open:not('.hidden, .hide')").each(function () {
				a.closeFolder(this)
			})
		},
		discloseVisible : function () {
			var b = this,
			c = b.$element.find(".tree-branch:not('.tree-open, .hidden, .hide')"),
			d = [],
			e = function f(a, e) {
				d.push(e),
				d.length === c.length && (b.$element.trigger("disclosedVisible.fu.tree", {
						tree : b.$element,
						reportedOpened : d
					}), b.$element.off("loaded.fu.tree", b.$element, f))
			};
			b.$element.on("loaded.fu.tree", e),
			b.$element.find(".tree-branch:not('.tree-open, .hidden, .hide')").each(function () {
				b.discloseFolder(a(this).find(".tree-branch-header"))
			})
		},
		discloseAll : function () {
			var a = this;
			"undefined" == typeof a.$element.data("disclosures") && a.$element.data("disclosures", 0);
			var b = a.options.disclosuresUpperLimit >= 1 && a.$element.data("disclosures") >= a.options.disclosuresUpperLimit,
			c = 0 === a.$element.find(".tree-branch:not('.tree-open, .hidden, .hide')").length;
			if (c)
				a.$element.trigger("disclosedAll.fu.tree", {
					tree : a.$element,
					disclosures : a.$element.data("disclosures")
				}), a.options.cacheItems || a.$element.one("closeAll.fu.tree", function () {
					a.$element.data("disclosures", 0)
				});
			else {
				if (b && (a.$element.trigger("exceededDisclosuresLimit.fu.tree", {
							tree : a.$element,
							disclosures : a.$element.data("disclosures")
						}), !a.$element.data("ignore-disclosures-limit")))
					return;
				a.$element.data("disclosures", a.$element.data("disclosures") + 1),
				a.$element.one("disclosedVisible.fu.tree", function () {
					a.discloseAll()
				}),
				a.discloseVisible()
			}
		},
		refreshFolder : function (a) {
			var b = a.closest(".tree-branch"),
			c = b.find(".tree-branch-children");
			c.eq(0).empty(),
			b.hasClass("tree-open") ? this.populate(c, !1) : this.populate(c, !0),
			this.$element.trigger("refreshedFolder.fu.tree", b.data())
		}
	},
	g.prototype.closeAll = g.prototype.collapse,
	g.prototype.openFolder = g.prototype.discloseFolder,
	g.prototype.getValue = g.prototype.selectedItems,
	a.fn.tree = function (b) {
		var c,
		d = Array.prototype.slice.call(arguments, 1),
		e = this.each(function () {
				var e = a(this),
				f = e.data("fu.tree"),
				h = "object" == typeof b && b;
				f || e.data("fu.tree", f = new g(this, h)),
				"string" == typeof b && (c = f[b].apply(f, d))
			});
		return void 0 === c ? e : c
	},
	a.fn.tree.defaults = {
		dataSource : function (a, b) {},
		multiSelect : !1,
		cacheItems : !0,
		folderSelect : !0,
		itemSelect : !0,
		disclosuresUpperLimit : 0
	},
	a.fn.tree.Constructor = g,
	a.fn.tree.noConflict = function () {
		return a.fn.tree = f,
		this
	}
});
