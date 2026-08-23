;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="80790123-f952-251c-2095-710ec5e4f415")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,972981,336265,260031,e=>{"use strict";var t=e.i(973245),r=e.i(951262);let a={},i=t.gql`
    fragment DeleteFolderDialogFolder on ReplFolder {
  id
  pathnames
}
    `,l=t.gql`
    mutation DeleteFolderDialogDeleteFolder($folderId: String!) {
  deleteReplFolder(folderId: $folderId) {
    id
  }
}
    `;e.s(["DeleteFolderDialogFolderFragmentDoc",0,i,"useDeleteFolderDialogDeleteFolderMutation",0,function(e){let t={...a,...e};return r.useMutation(l,t)}],336265);let n=t.gql`
    fragment ReplsDashboardFolderItemReplFolder on ReplFolder {
  id
  name
  canEdit
  pathnames
  image
  timeCreated
  replsCount
  folderType
  ...DeleteFolderDialogFolder
}
    ${i}`;var s=e.i(781258);let o=t.gql`
    fragment ReplsDashboardReplItemActionsRepl on Repl {
  id
  url
  slug
  pinnedToProfile
  isPrivate
  title
  description
  ...TransferReplToOrgDialogRepl
  org {
    __typename
    ... on Org {
      id
    }
  }
  owner {
    __typename
    ... on User {
      id
      username
    }
    ... on Team {
      id
      username
    }
  }
  authorizations {
    deleteRepl {
      isAuthorized
    }
    editFileContents {
      isAuthorized
    }
    editFolder {
      isAuthorized
    }
    editMetadata {
      isAuthorized
    }
    editPermissions {
      isAuthorized
    }
    editVisibility {
      isAuthorized
    }
    fork {
      isAuthorized
    }
    removeSelf {
      isAuthorized
    }
    star {
      isAuthorized
    }
  }
}
    ${s.TransferReplToOrgDialogReplFragmentDoc}`;var u=e.i(319801),d=e.i(566578),c=e.i(855763),p=e.i(80593),m=e.i(748538),g=e.i(913864);let h={},x=t.gql`
    fragment ReplsDashboardReplItemRepl on Repl {
  id
  title
  timeCreated
  isStarred
  isPrivate
  isOwner
  iconUrl
  publishedAs
  ...ReplsDashboardReplItemActionsRepl
  ...ReplLinkRepl
  user {
    id
    username
  }
  hostingDeployment {
    ... on HostingDeployment {
      id
      ...BuildStatusBadgeHostingDeployment
    }
  }
  ...BulkDeleteConfirmationModalRepl
  ...LeaveMultiplayerReplDialogRepl
  ...EditReplFormRepl
  ...ReplEnvironmentDesktopRepl
}
    ${o}
${u.ReplLinkReplFragmentDoc}
${d.BuildStatusBadgeHostingDeploymentFragmentDoc}
${c.BulkDeleteConfirmationModalReplFragmentDoc}
${p.LeaveMultiplayerReplDialogReplFragmentDoc}
${m.EditReplFormReplFragmentDoc}
${g.ReplEnvironmentDesktopReplFragmentDoc}`,f=t.gql`
    mutation ReplsDashboardUpdateRepl($input: UpdateReplInput!) {
  updateRepl(input: $input) {
    repl {
      id
      ...ReplsDashboardReplItemRepl
    }
  }
}
    ${x}`;e.s(["ReplsDashboardReplItemReplFragmentDoc",0,x,"useReplsDashboardUpdateReplMutation",0,function(e){let t={...h,...e};return r.useMutation(f,t)}],260031);var j=e.i(304277),b=e.i(566901);let v={},y=t.gql`
    query ReplsDashboardReplFolderList($path: String!, $starred: Boolean, $after: String) {
  currentUser {
    id
    username
    replFolderByPath(path: $path) {
      id
      ownerId: userId
      pathnames
      canEdit
      canCreateSubFolders
      parent {
        id
        pathnames
      }
      folders {
        id
        ...ReplsDashboardFolderItemReplFolder
      }
      repls(starred: $starred, after: $after) {
        items {
          id
          ...ReplsDashboardReplItemRepl
        }
        pageInfo {
          nextCursor
        }
      }
    }
    replCount {
      ... on ReplCount {
        count
      }
    }
  }
}
    ${n}
${x}`,R=t.gql`
    mutation ReplsDashboardCreateReplFolder($name: String!, $parentId: String, $teamId: Int) {
  createReplFolder(name: $name, parentId: $parentId, teamId: $teamId) {
    id
    ...ReplsDashboardFolderItemReplFolder
  }
}
    ${n}`,w=t.gql`
    mutation ReplsDashboardMoveItemsToFolder($replIds: [String!]!, $folderIds: [String!]!, $destFolderId: String!, $teamId: Int) {
  moveItemsToFolder(
    replIds: $replIds
    folderIds: $folderIds
    destFolderId: $destFolderId
    teamId: $teamId
  ) {
    ... on Repl {
      __typename
      id
      ...ReplsDashboardReplItemRepl
    }
    ... on ReplFolder {
      __typename
      id
      ...ReplsDashboardFolderItemReplFolder
    }
  }
}
    ${x}
${n}`;e.s(["useReplsDashboardCreateReplFolderMutation",0,function(e){let t={...v,...e};return r.useMutation(R,t)},"useReplsDashboardMoveItemsToFolderMutation",0,function(e){let t={...v,...e};return r.useMutation(w,t)},"useReplsDashboardReplFolderListLazyQuery",0,function(e){let t={...v,...e};return b.useLazyQuery(y,t)},"useReplsDashboardReplFolderListQuery",0,function(e){let t={...v,...e};return j.useQuery(y,t)}],972981)},445807,437497,289038,e=>{"use strict";var t=e.i(973245),r=e.i(304277);e.i(566901);let a={},i=t.gql`
    query UsageActionRequired {
  currentUser {
    __typename
    id
    usageBasedBillingBudget {
      ... on UsageBasedBillingBudget {
        id
        hasReachedBudget
      }
      ... on UnauthorizedError {
        message
      }
    }
    storageInfo {
      __typename
      storageQuotaStatus2 {
        __typename
        ... on StorageQuotaStatus {
          status
        }
        ... on ServiceUnavailable {
          message
        }
      }
    }
  }
}
    `;function l(e){let t={...a,...e};return r.useQuery(i,t)}let n=t.gql`
    query OrgUsageActionRequired($orgId: String!) {
  currentUser {
    __typename
    id
    org(orgId: $orgId) {
      __typename
      ... on Org {
        id
        usageBasedBillingBudget {
          __typename
          ... on UsageBasedBillingBudget {
            id
            hasReachedBudget
          }
          ... on Error {
            message
          }
        }
      }
      ... on Error {
        message
      }
    }
  }
}
    `;function s(e){let t={...a,...e};return r.useQuery(n,t)}e.s(["UsageActionRequiredDocument",0,i,"useOrgUsageActionRequiredQuery",0,s,"useUsageActionRequiredQuery",0,l],437497);var o=e.i(908796);e.s(["useUsageActionRequired",0,e=>{let{loading:t,data:r}=l({ssr:!1,context:{noBatch:!0},skip:void 0!==e}),{loading:a,data:i}=s({variables:{orgId:e??""},ssr:!1,context:{noBatch:!0},skip:!e});if(e)return{loading:a,actionRequired:i?.currentUser?.org.__typename==="Org"&&i.currentUser.org.usageBasedBillingBudget?.__typename==="UsageBasedBillingBudget"&&!!i.currentUser.org.usageBasedBillingBudget.hasReachedBudget};{if(!r||r.currentUser?.__typename!=="CurrentUser"||r.currentUser.storageInfo?.__typename!=="StorageInfo"||"StorageQuotaStatus"!==r.currentUser.storageInfo.storageQuotaStatus2.__typename)return{loading:t,actionRequired:!1};let{storageInfo:{storageQuotaStatus2:{status:e}},usageBasedBillingBudget:a}=r.currentUser;return{loading:t,actionRequired:a?.__typename==="UsageBasedBillingBudget"&&a.hasReachedBudget||e===o.StorageQuotaEnum.ExceedingQuota||e===o.StorageQuotaEnum.ApproachingQuota}}}],445807);var u=e.i(276385),d=e.i(138716),c=e.i(995691),p=e.i(255701),m=e.i(612343),g=e.i(776065),h=e.i(448942);let x=e=>t=>t.pathname===e;e.s(["useOrgGroupNavItems",0,function({orgSlug:e}){let t=(0,g.useQueryParam)("groupId","string"),r=(0,g.useQueryParam)("groupSlug","string");if(!e||!t||!r)return[];let a=(0,h.orgLinks)({slug:e}),i=(0,h.orgGroupLinks)({orgSlug:e,groupId:t,groupSlug:r});return[{label:"Back",href:a.groups.href.toString(),icon:(0,u.jsx)(d.default,{}),active:x(a.groups.routerPath)},{label:"Members",href:i.members.href.toString(),icon:(0,u.jsx)(m.default,{}),active:x(i.members.routerPath)},{label:"Permissions",href:i.permissions.href.toString(),icon:(0,u.jsx)(c.default,{}),active:x(i.permissions.routerPath)},{label:"Group settings",href:i.settings.href.toString(),icon:(0,u.jsx)(p.default,{}),active:x(i.settings.routerPath)}]}],289038)},63811,895897,e=>{"use strict";var t=e.i(389959),r=e.i(972981);e.s(["usePrefetchFolderList",0,function(){let e=(0,t.useRef)(!1),[a]=(0,r.useReplsDashboardReplFolderListLazyQuery)();return(0,t.useCallback)(()=>{e.current||(e.current=!0,a({variables:{path:""}}))},[a])}],63811);var a=e.i(973245),i=e.i(319801),l=e.i(304277),n=e.i(566901);let s={},o=a.gql`
    fragment GlobalSearchRepl on Repl {
  id
  title
  iconUrl
  ...ReplLinkRepl
}
    ${i.ReplLinkReplFragmentDoc}`,u=a.gql`
    query GlobalPersonalRecentRepls($count: Int!) {
  currentUser {
    id
    isStaff: hasRole(role: REPLIT_STAFF)
    clui
  }
  recentRepls(count: $count) {
    id
    ...GlobalSearchRepl
  }
}
    ${o}`,d=a.gql`
    query GlobalPersonalSearch($search: String!) {
  currentUser {
    id
    replSearch(search: $search) {
      id
      ...GlobalSearchRepl
    }
  }
}
    ${o}`,c=a.gql`
    query GlobalOrgRecentRepls($count: Int!, $orgId: String!) {
  currentUser {
    id
    isStaff: hasRole(role: REPLIT_STAFF)
    clui
    org(orgId: $orgId) {
      ... on Org {
        id
        name
        recentRepls(input: {count: $count}) {
          ... on ReplConnection {
            items {
              ...GlobalSearchRepl
            }
          }
        }
      }
    }
  }
}
    ${o}`,p=a.gql`
    query GlobalOrgSearch($orgId: String!, $replsInput: OrgReplsInput!) {
  currentUser {
    id
    org(orgId: $orgId) {
      ... on Org {
        id
        repls(input: $replsInput) {
          ... on ReplConnection {
            items {
              ...GlobalSearchRepl
            }
          }
        }
      }
    }
  }
}
    ${o}`;e.s(["useGlobalOrgRecentReplsQuery",0,function(e){let t={...s,...e};return l.useQuery(c,t)},"useGlobalOrgSearchLazyQuery",0,function(e){let t={...s,...e};return n.useLazyQuery(p,t)},"useGlobalPersonalRecentReplsQuery",0,function(e){let t={...s,...e};return l.useQuery(u,t)},"useGlobalPersonalSearchLazyQuery",0,function(e){let t={...s,...e};return n.useLazyQuery(d,t)}],895897)},208301,(e,t,r)=>{t.exports=e.g&&e.g.Object===Object&&e.g},240240,(e,t,r)=>{var a=e.r(208301),i="object"==typeof self&&self&&self.Object===Object&&self;t.exports=a||i||Function("return this")()},220259,(e,t,r)=>{t.exports=e.r(240240).Symbol},70234,(e,t,r)=>{t.exports=function(e,t){for(var r=-1,a=null==e?0:e.length,i=Array(a);++r<a;)i[r]=t(e[r],r,e);return i}},372797,(e,t,r)=>{t.exports=Array.isArray},895771,(e,t,r)=>{var a=e.r(220259),i=Object.prototype,l=i.hasOwnProperty,n=i.toString,s=a?a.toStringTag:void 0;t.exports=function(e){var t=l.call(e,s),r=e[s];try{e[s]=void 0;var a=!0}catch(e){}var i=n.call(e);return a&&(t?e[s]=r:delete e[s]),i}},750351,(e,t,r)=>{var a=Object.prototype.toString;t.exports=function(e){return a.call(e)}},346012,(e,t,r)=>{var a=e.r(220259),i=e.r(895771),l=e.r(750351),n=a?a.toStringTag:void 0;t.exports=function(e){return null==e?void 0===e?"[object Undefined]":"[object Null]":n&&n in Object(e)?i(e):l(e)}},386457,(e,t,r)=>{t.exports=function(e){return null!=e&&"object"==typeof e}},887178,(e,t,r)=>{var a=e.r(346012),i=e.r(386457);t.exports=function(e){return"symbol"==typeof e||i(e)&&"[object Symbol]"==a(e)}},296438,(e,t,r)=>{var a=e.r(220259),i=e.r(70234),l=e.r(372797),n=e.r(887178),s=1/0,o=a?a.prototype:void 0,u=o?o.toString:void 0;t.exports=function e(t){if("string"==typeof t)return t;if(l(t))return i(t,e)+"";if(n(t))return u?u.call(t):"";var r=t+"";return"0"==r&&1/t==-s?"-0":r}},669135,(e,t,r)=>{var a=e.r(296438);t.exports=function(e){return null==e?"":a(e)}},290308,(e,t,r)=>{t.exports=function(e,t,r){var a=-1,i=e.length;t<0&&(t=-t>i?0:i+t),(r=r>i?i:r)<0&&(r+=i),i=t>r?0:r-t>>>0,t>>>=0;for(var l=Array(i);++a<i;)l[a]=e[a+t];return l}},555231,(e,t,r)=>{var a=e.r(290308);t.exports=function(e,t,r){var i=e.length;return r=void 0===r?i:r,!t&&r>=i?e:a(e,t,r)}},973701,(e,t,r)=>{var a=RegExp("[\\u200d\\ud800-\\udfff\\u0300-\\u036f\\ufe20-\\ufe2f\\u20d0-\\u20ff\\ufe0e\\ufe0f]");t.exports=function(e){return a.test(e)}},382798,(e,t,r)=>{t.exports=function(e){return e.split("")}},486096,(e,t,r)=>{var a="\\ud800-\\udfff",i="[\\u0300-\\u036f\\ufe20-\\ufe2f\\u20d0-\\u20ff]",l="\\ud83c[\\udffb-\\udfff]",n="[^"+a+"]",s="(?:\\ud83c[\\udde6-\\uddff]){2}",o="[\\ud800-\\udbff][\\udc00-\\udfff]",u="(?:"+i+"|"+l+")?",d="[\\ufe0e\\ufe0f]?",c="(?:\\u200d(?:"+[n,s,o].join("|")+")"+d+u+")*",p=RegExp(l+"(?="+l+")|"+("(?:"+[n+i+"?",i,s,o,"["+a+"]"].join("|"))+")"+(d+u+c),"g");t.exports=function(e){return e.match(p)||[]}},475593,(e,t,r)=>{var a=e.r(382798),i=e.r(973701),l=e.r(486096);t.exports=function(e){return i(e)?l(e):a(e)}},484092,(e,t,r)=>{var a=e.r(555231),i=e.r(973701),l=e.r(475593),n=e.r(669135);t.exports=function(e){return function(t){var r=i(t=n(t))?l(t):void 0,s=r?r[0]:t.charAt(0),o=r?a(r,1).join(""):t.slice(1);return s[e]()+o}}},428803,(e,t,r)=>{t.exports=e.r(484092)("toUpperCase")},312388,(e,t,r)=>{var a=e.r(669135),i=e.r(428803);t.exports=function(e){return i(a(e).toLowerCase())}},338198,(e,t,r)=>{t.exports=function(e,t,r,a){var i=-1,l=null==e?0:e.length;for(a&&l&&(r=e[++i]);++i<l;)r=t(r,e[i],i,e);return r}},235319,(e,t,r)=>{t.exports=function(e){return function(t){return null==e?void 0:e[t]}}},614796,(e,t,r)=>{t.exports=e.r(235319)({À:"A",Á:"A",Â:"A",Ã:"A",Ä:"A",Å:"A",à:"a",á:"a",â:"a",ã:"a",ä:"a",å:"a",Ç:"C",ç:"c",Ð:"D",ð:"d",È:"E",É:"E",Ê:"E",Ë:"E",è:"e",é:"e",ê:"e",ë:"e",Ì:"I",Í:"I",Î:"I",Ï:"I",ì:"i",í:"i",î:"i",ï:"i",Ñ:"N",ñ:"n",Ò:"O",Ó:"O",Ô:"O",Õ:"O",Ö:"O",Ø:"O",ò:"o",ó:"o",ô:"o",õ:"o",ö:"o",ø:"o",Ù:"U",Ú:"U",Û:"U",Ü:"U",ù:"u",ú:"u",û:"u",ü:"u",Ý:"Y",ý:"y",ÿ:"y",Æ:"Ae",æ:"ae",Þ:"Th",þ:"th",ß:"ss",Ā:"A",Ă:"A",Ą:"A",ā:"a",ă:"a",ą:"a",Ć:"C",Ĉ:"C",Ċ:"C",Č:"C",ć:"c",ĉ:"c",ċ:"c",č:"c",Ď:"D",Đ:"D",ď:"d",đ:"d",Ē:"E",Ĕ:"E",Ė:"E",Ę:"E",Ě:"E",ē:"e",ĕ:"e",ė:"e",ę:"e",ě:"e",Ĝ:"G",Ğ:"G",Ġ:"G",Ģ:"G",ĝ:"g",ğ:"g",ġ:"g",ģ:"g",Ĥ:"H",Ħ:"H",ĥ:"h",ħ:"h",Ĩ:"I",Ī:"I",Ĭ:"I",Į:"I",İ:"I",ĩ:"i",ī:"i",ĭ:"i",į:"i",ı:"i",Ĵ:"J",ĵ:"j",Ķ:"K",ķ:"k",ĸ:"k",Ĺ:"L",Ļ:"L",Ľ:"L",Ŀ:"L",Ł:"L",ĺ:"l",ļ:"l",ľ:"l",ŀ:"l",ł:"l",Ń:"N",Ņ:"N",Ň:"N",Ŋ:"N",ń:"n",ņ:"n",ň:"n",ŋ:"n",Ō:"O",Ŏ:"O",Ő:"O",ō:"o",ŏ:"o",ő:"o",Ŕ:"R",Ŗ:"R",Ř:"R",ŕ:"r",ŗ:"r",ř:"r",Ś:"S",Ŝ:"S",Ş:"S",Š:"S",ś:"s",ŝ:"s",ş:"s",š:"s",Ţ:"T",Ť:"T",Ŧ:"T",ţ:"t",ť:"t",ŧ:"t",Ũ:"U",Ū:"U",Ŭ:"U",Ů:"U",Ű:"U",Ų:"U",ũ:"u",ū:"u",ŭ:"u",ů:"u",ű:"u",ų:"u",Ŵ:"W",ŵ:"w",Ŷ:"Y",ŷ:"y",Ÿ:"Y",Ź:"Z",Ż:"Z",Ž:"Z",ź:"z",ż:"z",ž:"z",Ĳ:"IJ",ĳ:"ij",Œ:"Oe",œ:"oe",ŉ:"'n",ſ:"s"})},868380,(e,t,r)=>{var a=e.r(614796),i=e.r(669135),l=/[\xc0-\xd6\xd8-\xf6\xf8-\xff\u0100-\u017f]/g,n=RegExp("[\\u0300-\\u036f\\ufe20-\\ufe2f\\u20d0-\\u20ff]","g");t.exports=function(e){return(e=i(e))&&e.replace(l,a).replace(n,"")}},813601,(e,t,r)=>{var a=/[^\x00-\x2f\x3a-\x40\x5b-\x60\x7b-\x7f]+/g;t.exports=function(e){return e.match(a)||[]}},666792,(e,t,r)=>{var a=/[a-z][A-Z]|[A-Z]{2}[a-z]|[0-9][a-zA-Z]|[a-zA-Z][0-9]|[^a-zA-Z0-9 ]/;t.exports=function(e){return a.test(e)}},400642,(e,t,r)=>{var a="\\ud800-\\udfff",i="\\u2700-\\u27bf",l="a-z\\xdf-\\xf6\\xf8-\\xff",n="A-Z\\xc0-\\xd6\\xd8-\\xde",s="\\xac\\xb1\\xd7\\xf7\\x00-\\x2f\\x3a-\\x40\\x5b-\\x60\\x7b-\\xbf\\u2000-\\u206f \\t\\x0b\\f\\xa0\\ufeff\\n\\r\\u2028\\u2029\\u1680\\u180e\\u2000\\u2001\\u2002\\u2003\\u2004\\u2005\\u2006\\u2007\\u2008\\u2009\\u200a\\u202f\\u205f\\u3000",o="['’]",u="["+s+"]",d="["+l+"]",c="[^"+a+s+"\\d+"+i+l+n+"]",p="(?:\\ud83c[\\udde6-\\uddff]){2}",m="[\\ud800-\\udbff][\\udc00-\\udfff]",g="["+n+"]",h="(?:"+d+"|"+c+")",x="(?:"+g+"|"+c+")",f="(?:"+o+"(?:d|ll|m|re|s|t|ve))?",j="(?:"+o+"(?:D|LL|M|RE|S|T|VE))?",b="(?:[\\u0300-\\u036f\\ufe20-\\ufe2f\\u20d0-\\u20ff]|\\ud83c[\\udffb-\\udfff])?",v="[\\ufe0e\\ufe0f]?",y="(?:\\u200d(?:"+["[^"+a+"]",p,m].join("|")+")"+v+b+")*",R="(?:"+["["+i+"]",p,m].join("|")+")"+(v+b+y),w=RegExp([g+"?"+d+"+"+f+"(?="+[u,g,"$"].join("|")+")",x+"+"+j+"(?="+[u,g+h,"$"].join("|")+")",g+"?"+h+"+"+f,g+"+"+j,"\\d*(?:1ST|2ND|3RD|(?![123])\\dTH)(?=\\b|[a-z_])|\\d*(?:1st|2nd|3rd|(?![123])\\dth)(?=\\b|[A-Z_])|\\d+",R].join("|"),"g");t.exports=function(e){return e.match(w)||[]}},713084,(e,t,r)=>{var a=e.r(813601),i=e.r(666792),l=e.r(669135),n=e.r(400642);t.exports=function(e,t,r){return(e=l(e),void 0===(t=r?void 0:t))?i(e)?n(e):a(e):e.match(t)||[]}},114915,(e,t,r)=>{var a=e.r(338198),i=e.r(868380),l=e.r(713084),n=RegExp("['’]","g");t.exports=function(e){return function(t){return a(l(i(t).replace(n,"")),e,"")}}},156289,(e,t,r)=>{var a=e.r(312388);t.exports=e.r(114915)(function(e,t,r){return t=t.toLowerCase(),e+(r?a(t):t)})},941706,e=>{e.v({fieldWrapper:"index-module__BB7faG__fieldWrapper",menuWrapper:"index-module__BB7faG__menuWrapper"})},109273,135069,458713,89610,338657,196064,762902,166295,771087,796820,e=>{"use strict";var t=e.i(973245),r=e.i(304277);e.i(566901);let a={},i=t.gql`
    query CurrentUserClui {
  currentUser {
    id
    clui
  }
}
    `;e.s(["useCurrentUserCluiQuery",0,function(e){let t={...a,...e};return r.useQuery(i,t)}],109273),e.i(156289),e.s([],135069),e.s(["forEach",0,(e,t)=>{if("object"!=typeof e.commands)throw Error("Expected commands object");t({command:e,root:e});let r=[...Object.values(e.commands)];for(;r.length;){let a=r.shift();a&&(t({command:a,root:e}),a.commands&&r.push(...Object.values(a.commands)))}}],458713);let l=e=>{if("ENUM"===e.arg.graphql.kind)return e.value||void 0;switch(e.arg.type){case"string":return e.value;case"int":return parseInt(e.value,10);case"float":return parseFloat(e.value);case"boolean":return!!e.value;default:return}};e.s(["parseArgs",0,e=>{let t=[],r=[],a={},i={...e.args};if(!e.command.args)return{variables:a,missing:{},extra:Object.keys(i).length?i:void 0};for(let n of Object.values(e.command.args)){let s=e.args[n.name];if(delete i[n.name],void 0===s)n.required?t.push(n):r.push(n);else if("boolean"===n.type&&"boolean"==typeof s)a[n.name]=s;else{let e=l({value:s.toString(),arg:n});void 0!==e&&(a[n.name]=e)}}return{variables:a,missing:{...t.length?{required:t}:{},...r.length?{optional:r}:{}},extra:Object.keys(i).length?i:void 0}}],89610);var n=e.i(276385),s=e.i(183035),o=e.i(167392),u=e.i(416298),d=e.i(967629),c=e.i(480028);let p=(0,d.css)({"div :global(svg)":{transform:"rotate(270deg)"}}),m=(0,d.css)({".icon":{flex:"0 0 auto",whiteSpace:"pre",userSelect:"none"},".icon.success":{color:c.tokens.accentPositiveDefault},".error":{color:c.tokens.accentNegativeDefault}}),g=e=>(0,n.jsxs)("div",{clsx:["icon",e],css:m,children:[(({error:e,success:t})=>e?(0,n.jsx)(u.default,{}):t?(0,n.jsx)(s.default,{}):(0,n.jsx)("div",{css:p,children:(0,n.jsx)(o.default,{})}))(e)," "]});e.s(["default",0,g],338657);let h=(0,d.css)({"&":{display:"flex"}}),x=({children:e})=>(0,n.jsx)("div",{className:"prompt",css:h,children:e});e.s(["default",0,e=>{let{networkError:t}=e.error,r=t&&t.result&&t.result.errors?t.result.errors.map(e=>e.message):[e.error.toString()];return(0,n.jsxs)(x,{children:[(0,n.jsx)(g,{error:!0}),(0,n.jsx)("div",{children:r.map(e=>(0,n.jsx)("div",{children:e},e))})]})}],196064);var f=e.i(389959),j=e.i(54456),b=e.i(37048),v=e.i(643484),y=e.i(86145),R=e.i(8047);let w=(e,t)=>"UPDATE"===t.type?{...e,...t.updates}:e,C=({description:e,...t})=>(0,n.jsxs)(b.VStack,{spacing:1,align:"stretch",children:[(0,n.jsx)(j.default,{...t,label:t.name}),e?(0,n.jsxs)(R.Text,{color:"dimmer",variant:"small",children:[e,t.required?"":" (optional)"]}):null,e||t.required?null:(0,n.jsx)(R.Text,{color:"dimmer",variant:"small",children:"optional"})]}),S=(0,d.css)({"&":{display:"grid",gridGap:"10px"},label:{userSelect:"none",display:"grid",gridTemplateColumns:"20px auto",gridGap:"10px",alignItems:"center"}}),T=({description:e,...t})=>(0,n.jsxs)("div",{css:S,children:[(0,n.jsxs)("label",{children:[(0,n.jsx)(y.Checkbox,{...t}),(0,n.jsx)("span",{children:t.name})]}),e?(0,n.jsxs)(R.Text,{color:"dimmer",variant:"small",children:[e,t.required?"":" (optional)"]}):null,e||t.required?null:(0,n.jsx)(R.Text,{color:"dimmer",variant:"small",children:"optional"})]}),k=(0,d.css)({"&":{display:"block"},select:{fontSize:c.tokens.fontSizeDefault,fontFamily:c.tokens.fontFamilyDefault,lineHeight:c.tokens.lineHeightDefault,backgroundColor:c.tokens.backgroundDefault,color:c.tokens.foregroundDefault,padding:c.tokens.space8,border:`1px solid ${c.tokens.outlineDimmest}`,borderRadius:c.tokens.borderRadius4,outline:"none",width:"100%",boxSizing:"border-box",transition:"color 0.1s, background-color 0.1s"},"select:hover":{border:`1px solid ${c.tokens.accentPrimaryDimmer}`},"select:active,select:focus":{outline:"none",borderColor:c.tokens.accentPrimaryDefault}}),I=({description:e,...t})=>(0,n.jsxs)(b.VStack,{spacing:1,align:"stretch",children:[t.name?(0,n.jsx)(R.Text,{color:"dimmer",variant:"small",children:t.name}):null,(0,n.jsx)("label",{css:k,children:(0,n.jsxs)("select",{...t,children:[(0,n.jsx)("option",{value:""},"empty"),t.options.map(e=>(0,n.jsx)("option",{value:e.value,children:e.value},e.value))]})}),e?(0,n.jsxs)(R.Text,{color:"dimmer",variant:"small",children:[e,t.required?"":" (optional)"]}):null,e||t.required?null:(0,n.jsx)(R.Text,{color:"dimmer",variant:"small",children:"optional"})]}),_=(0,d.css)({form:{maxWidth:"600px"}});e.s(["default",0,e=>{let{command:t,parsedVariables:r}=e,a=t.args&&Object.values(t.args).reverse(),i=Object.keys(r).reduce((e,t)=>(a?.find(e=>e.name===t)&&(e[t]=r[t]),e),{}),[l,s]=(0,f.useReducer)(w,i),o=(0,f.useCallback)(e=>s({type:"UPDATE",updates:e}),[s]),u=a?.find(e=>"boolean"!==e.type&&!l[e.name]);return(0,n.jsx)("div",{className:"wrap",css:_,children:(0,n.jsx)("form",{onSubmit:t=>{t.preventDefault(),e.onSubmit(l)},children:(0,n.jsxs)(b.VStack,{spacing:2,align:"stretch",children:[t.description?(0,n.jsx)(R.Text,{children:t.description}):null,a?a.map(e=>{let t=e.name,r={name:e.name,required:e.required,description:e.description||void 0},a=l[e.name];return"ENUM"===e.graphql.kind&&Array.isArray(e.options)?(0,n.jsx)(I,{...r,options:e.options,autoFocus:u&&u.name===e.name,onChange:t=>o({[e.name]:t.currentTarget.value})},t):"boolean"===e.type?(0,n.jsx)(T,{...r,id:t,checked:!!l[e.name],onChange:t=>o({[e.name]:t})},t):(0,n.jsx)(C,{...r,autoFocus:u&&u.name===e.name,value:a?a.toString():"",onChange:t=>o({[e.name]:t.currentTarget.value})},t)}):null,(0,n.jsx)("div",{children:(0,n.jsx)(v.Button,{colorway:"primary",type:"submit",disabled:e.isLoading,text:e.isLoading?"Loading...":"Submit"})})]})})})}],762902);var E=e.i(951262);let U={},A=t.gql`
    mutation DeleteTipInteractions($mode: DeleteTipInteractionsMode!, $target: String) {
  deleteTipInteractions(mode: $mode, target: $target) {
    __typename
    ... on DeleteTipInteractionsResult {
      message
      deletedCount
      details
    }
    ... on NotFoundError {
      message
    }
    ... on UserError {
      message
    }
  }
}
    `;var L=e.i(399245),D=e.i(355407),P=e.i(334028),$=e.i(612343),O=e.i(570438),B=e.i(449525),V=e.i(142406),M=e.i(528326),F=e.i(61732);let N={maxWidth:"600px",padding:c.tokens.space16},q={display:"flex",flexDirection:"column",gap:c.tokens.space16,alignItems:"stretch"},z={display:"flex",flexDirection:"column",gap:c.tokens.space12,alignItems:"stretch"},G={marginBottom:c.tokens.space8},Q={alignSelf:"flex-start"},W={marginTop:c.tokens.space4},H={display:"flex",flexDirection:"column",gap:c.tokens.space8};e.s(["default",0,()=>{let e,[t,r]=(0,f.useState)("USERNAME"),[a,i]=(0,f.useState)(""),[l,s]=(0,f.useState)(""),[o,u]=(0,f.useState)(null),[d,p]=(0,f.useState)(!1),m=(0,O.useCurrentUserId)(),[g,{loading:h}]=(e={...U,...void 0},E.useMutation(A,e)),x=(0,f.useCallback)(async()=>{try{let e;e="ALL"===t?void 0:"MYSELF"===t?m?.toString():a.trim();let{data:r}=await g({variables:{mode:"MYSELF"===t?"USER_ID":t,target:e}}),l=r?.deleteTipInteractions;l&&("DeleteTipInteractionsResult"===l.__typename?(u({message:l.message}),i("")):("NotFoundError"===l.__typename||"UserError"===l.__typename)&&u({error:l.message}))}catch(e){u({error:"An unexpected error occurred"})}},[g,t,a,m]),b=(0,f.useCallback)(async e=>{(e.preventDefault(),s(""),t)?"MYSELF"!==t||m?"USERNAME"!==t&&"USER_ID"!==t&&"ORG"!==t||a.trim()?"ALL"===t?p(!0):await x():"USERNAME"===t?s("Please enter a username"):"USER_ID"===t?s("Please enter a user ID"):s("Please enter a workspace ID"):s("Current user ID not available"):s("Please select what to delete")},[t,a,x,m]),y=(0,f.useCallback)(async()=>{p(!1),await x()},[x]);return(0,n.jsxs)(n.Fragment,{children:[(0,n.jsx)(F.View,{css:N,children:(0,n.jsxs)(F.View,{css:q,children:[(0,n.jsx)(R.Text,{variant:"subheadBig",children:"Delete user tip interactions"}),(0,n.jsx)(R.Text,{variant:"small",color:"dimmer",children:"This will permanently delete tip interaction data. This action cannot be undone."}),(0,n.jsx)("form",{onSubmit:b,children:(0,n.jsxs)(F.View,{css:z,children:[(0,n.jsxs)(F.View,{children:[(0,n.jsx)(R.Text,{variant:"small",css:G,children:"What to delete"}),(0,n.jsxs)(B.ButtonGroup,{primary:!0,name:"delete-mode",value:t,onChange:e=>{r(e),s(""),u(null)},disabled:h,row:!0,stretch:!0,children:[(0,n.jsx)(B.ButtonGroupItem,{id:"myself-mode",text:"Myself",value:"MYSELF",icon:(0,n.jsx)(P.default,{})}),(0,n.jsx)(B.ButtonGroupItem,{id:"username-mode",text:"Username",value:"USERNAME",icon:(0,n.jsx)(P.default,{})}),(0,n.jsx)(B.ButtonGroupItem,{id:"user-id-mode",text:"User ID",value:"USER_ID",icon:(0,n.jsx)(D.default,{})}),(0,n.jsx)(B.ButtonGroupItem,{id:"org-mode",text:"Workspace",value:"ORG",icon:(0,n.jsx)($.default,{})}),(0,n.jsx)(B.ButtonGroupItem,{id:"all-mode",text:"All Users",value:"ALL",icon:(0,n.jsx)(L.default,{})})]})]}),"USERNAME"===t||"USER_ID"===t||"ORG"===t?(0,n.jsxs)(F.View,{children:[(0,n.jsx)(R.Text,{variant:"small",css:G,children:"USERNAME"===t?"Username":"USER_ID"===t?"User ID":"ORG"===t?"Workspace ID":""}),(0,n.jsx)(j.default,{value:a,onChange:e=>{i(e.target.value),s(""),u(null)},placeholder:"USERNAME"===t?"Enter username (e.g., johndoe)...":"USER_ID"===t?"Enter numeric user ID (e.g., 12345)...":"ORG"===t?"Enter workspace ID...":"",disabled:h}),(0,n.jsx)(R.Text,{variant:"small",color:"dimmer",css:W,children:"USERNAME"===t?"Enter the exact username without the @ symbol.":"USER_ID"===t?"Enter the numeric user ID from the database.":"ORG"===t?"This will delete tip interactions for all users within the specified workspace.":""})]}):null,"MYSELF"===t&&(0,n.jsx)(F.View,{children:(0,n.jsxs)(R.Text,{variant:"small",color:"dimmer",children:["This will delete your own tip interactions (User ID:"," ",m||"Loading...",")."]})}),"ALL"===t&&(0,n.jsx)(F.View,{children:(0,n.jsx)(R.Text,{variant:"small",color:"dimmer",children:"⚠️ This will delete ALL tip interactions for ALL users globally. This action cannot be undone."})}),l?(0,n.jsxs)(R.Text,{variant:"small",color:"dimmer",children:["⚠️ ",l]}):null,o?(0,n.jsx)(F.View,{style:{padding:c.tokens.space12,borderRadius:c.tokens.borderRadius8,backgroundColor:o.error?c.tokens.redDimmest:c.tokens.greenDimmest,border:`1px solid ${o.error?c.tokens.redDimmer:c.tokens.greenDimmer}`},children:(0,n.jsxs)(R.Text,{variant:"small",children:[o.error?"❌":"✅"," ",o.message||o.error]})}):null,(0,n.jsx)(v.Button,{type:"submit",disabled:!(t&&("ALL"===t||("MYSELF"===t?!!m:a.trim().length>0)))||h,css:Q,colorway:"ALL"===t?"negative":"primary",text:h?"Deleting...":"ALL"===t?"Delete All Interactions":"Delete Interactions"})]})})]})}),(0,n.jsx)(M.Modal,{isOpen:d,onRequestClose:()=>p(!1),maxWidth:500,centered:!0,children:(0,n.jsx)(V.default,{prompt:"Confirm Global Deletion",desc:(0,n.jsxs)(F.View,{css:H,children:[(0,n.jsxs)(R.Text,{children:["You are about to permanently delete"," ",(0,n.jsx)("strong",{children:"ALL tip interactions"})," for"," ",(0,n.jsx)("strong",{children:"ALL users"})," in the system."]}),(0,n.jsx)(R.Text,{color:"dimmer",children:"This action is irreversible and will affect the entire platform. Are you absolutely sure you want to continue?"})]}),confirmText:"Yes, Delete Everything",danger:!0,loading:h,onCancel:()=>p(!1),onConfirm:y})})]})}],166295);var Y=e.i(330666),K=e.i(162372),Z=e.i(319801);let J={},X=t.gql`
    fragment CluiTemplateReplsRepl on Repl {
  id
  slug
  title
  language
  iconUrl
  ...ReplLinkRepl
}
    ${Z.ReplLinkReplFragmentDoc}`,ee=t.gql`
    fragment CluiTemplateReplsLanguage on Language {
  id
  key
  icon
  displayName
  templateRepl {
    id
  }
  betaTemplateRepl {
    id
  }
}
    `,et=t.gql`
    mutation CluiSetLanguageRepl($input: SetLanguageTemplateInput!) {
  setLanguageTemplateRepl(input: $input) {
    ... on Repl {
      id
    }
    ... on UnauthorizedError {
      message
    }
    ... on NotFoundError {
      message
    }
    ... on UserError {
      message
    }
  }
}
    `;function er(e){let t={...J,...e};return E.useMutation(et,t)}let ea=t.gql`
    query CluiSetTemplate {
  languageTemplateRepls {
    id
    ...CluiTemplateReplsRepl
  }
  languages(getAll: true) {
    id
    ...CluiTemplateReplsLanguage
  }
}
    ${X}
${ee}`;var ei=e.i(657929),el=e.i(491194),en=e.i(585227),es=e.i(109459),eo=e.i(215814),eu=e.i(295798),ed=e.i(320216),ec=e.i(462229),ep=e.i(723517),em=e.i(691636),eg=e.i(528710),eh=e.i(921125),ex=e.i(365757),ef=e.i(941706);let ej=(0,d.css)({fontFamily:c.tokens.fontFamilyCode,color:c.tokens.accentPrimaryDefault}),eb=(0,ec.cssRecord)({button:[ep.interactive.filled,em.rcss.p(8),em.rcss.color.foregroundDefault,em.rcss.height(32),em.rcss.display.flex,em.rcss.align.center]});function ev({id:e,items:t,"aria-label":r,initialSelectedItem:a,selectedItem:i,onChange:l,placeholder:s,dataCy:o,...u}){let d=(0,eu.default)(l),[c,p]=(0,f.useState)(t),m=(0,K.useCombobox)({id:e,items:c,onInputValueChange({inputValue:e}){let r;p(t.filter((r=e?.toLowerCase()??"",function(t){return!e||t.title.toLowerCase().includes(r)})))},initialSelectedItem:a,onSelectedItemChange({selectedItem:e}){e&&d.current(e)},itemToString:e=>e?e.title:"",...void 0!==i&&{selectedItem:i}});return(0,n.jsxs)(F.View,{dataCy:o,children:[(0,n.jsx)(Y.VisuallyHidden,{children:(0,n.jsx)("label",{...m.getLabelProps(),children:r})}),(0,n.jsx)("button",{type:"button",css:eb.button,...u,...m.getToggleButtonProps(),children:(0,n.jsxs)(F.View,{clsx:ef.default.fieldWrapper,align:"center",row:!0,gap:8,children:[(0,n.jsx)(eg.Input,{placeholder:s,...m.getInputProps()}),(0,n.jsx)(ei.default,{rotate:180*!!m.isOpen})]})}),(0,n.jsx)("div",{...m.getMenuProps(),clsx:ef.default.menuWrapper,children:m.isOpen&&c.length>0?(0,n.jsx)(es.default,{children:c.map((e,t)=>(0,n.jsx)("li",{...m.getItemProps({item:e,index:t}),children:(0,n.jsx)(eo.default,{highlighted:t===m.highlightedIndex,selected:e===m.selectedItem,title:e.title})},e.title))}):null})]})}function ey(e){return!en.default.allSupported().find(({key:t})=>t===e)}function eR(e){return e.slice().sort((e,t)=>{let r=ey(e.key),a=ey(t.key);return r&&!a?1:!r&&a?-1:!e.templateRepl&&t.templateRepl?1:e.templateRepl&&!t.templateRepl?-1:e.key!==t.key?e.key.localeCompare(t.key):0})}let ew=(0,d.css)({td:{padding:c.tokens.space8}});function eC({icon:e,repl:t,betaRepl:r,displayName:a,onRemove:i,language:l}){let[s,o]=(0,f.useState)(null),[u,{loading:d}]=er({onCompleted:()=>{i()},onError:e=>{o(e.message)}});return(0,n.jsxs)("tr",{css:ew,children:[(0,n.jsx)("td",{children:(0,n.jsxs)(b.HStack,{spacing:1,children:[(0,n.jsx)(ex.default,{size:16,alt:a,iconUrl:e}),(0,n.jsxs)(b.VStack,{children:[(0,n.jsx)(R.Text,{children:a}),(0,n.jsx)(R.Text,{css:ej,children:l})]})]})}),(0,n.jsx)("td",{children:(0,n.jsxs)(b.HStack,{spacing:1,children:[(0,n.jsx)("div",{children:(0,n.jsx)(ex.default,{size:16,alt:t.title,iconUrl:t.iconUrl})}),(0,n.jsx)(eh.default,{repl:t,children:t.url}),"nix"===t.language||"nix_beta"===t.language?(0,n.jsx)("div",{children:"(nix)"}):null]})}),(0,n.jsx)("td",{children:r?(0,n.jsxs)(b.HStack,{spacing:1,children:[(0,n.jsx)("div",{children:(0,n.jsx)(ex.default,{size:16,alt:r.title,iconUrl:r.iconUrl})}),(0,n.jsx)(eh.default,{repl:r,children:r.url}),"nix"===r.language||"nix_beta"===r.language?(0,n.jsx)("div",{children:"(nix)"}):null]}):(0,n.jsx)("div",{children:"-"})}),(0,n.jsxs)("td",{children:[(0,n.jsx)(v.Button,{disabled:d,size:"small",colorway:"negative",variant:"underlined",onClick:()=>{window.confirm(`Are you sure you want to remove the template for ${a}?`)&&u({variables:{input:{language:l}}})},iconLeft:(0,n.jsx)(el.default,{}),text:""}),s?(0,n.jsx)(R.Text,{css:{color:c.tokens.accentNegativeDefault},children:s}):null]})]})}let eS=(0,d.css)({td:{padding:c.tokens.space8}});function eT({language:e,icon:t,displayName:r}){return(0,n.jsxs)("tr",{css:eS,children:[(0,n.jsx)("td",{children:(0,n.jsxs)(b.HStack,{spacing:1,children:[(0,n.jsx)(ex.default,{size:16,alt:r,iconUrl:t}),(0,n.jsxs)(b.VStack,{children:[(0,n.jsx)(R.Text,{children:r}),(0,n.jsx)(R.Text,{css:ej,children:e})]})]})}),(0,n.jsx)("td",{children:(0,n.jsx)(b.HStack,{spacing:1,children:(0,n.jsx)("div",{children:"-"})})}),(0,n.jsx)("td",{children:(0,n.jsx)("div",{children:"-"})}),(0,n.jsx)("td",{children:"-"})]})}function ek({languages:e,templates:t,onSubmit:r}){let{showError:a}=(0,ed.default)(),[i,l]=(0,f.useState)(null),[s,o]=(0,f.useState)(null),[u,d]=(0,f.useState)(null),[c,p]=(0,f.useState)(null),[m,{loading:g}]=er({onCompleted:()=>{r(),l(null),o(null),d(null),p(null)},onError:e=>{a(e.message)}}),h=eR(e).map(e=>({value:e.key,title:`${e.key} (${e.displayName})`})),x=t.map(e=>({value:e.id,title:e.slug}));return(0,n.jsx)(b.VStack,{spacing:2,children:(0,n.jsxs)(b.HStack,{spacing:3,align:"center",justify:"space-evenly",children:[(0,n.jsx)(b.VStack,{children:(0,n.jsx)("div",{style:{width:200},children:(0,n.jsx)(ev,{selectedItem:h.find(e=>e.value===i),placeholder:"Select a language",onChange:t=>{l(t.value);let r=e.find(e=>e.key===t.value);if(!r)return;let a=x.find(e=>e.value===r.templateRepl?.id);a&&(o(a.value),p(a.title));let i=x.find(e=>e.value===r.betaTemplateRepl?.id);i&&d(i.value)},items:h})})}),(0,n.jsx)(b.VStack,{children:(0,n.jsx)("div",{className:"select",children:(0,n.jsx)(ev,{selectedItem:x.find(e=>e.value===s),placeholder:"Select a template",onChange:e=>{o(e.value),p(e.title)},items:x})})}),(0,n.jsx)(b.VStack,{children:(0,n.jsx)("div",{className:"select",children:(0,n.jsx)(ev,{selectedItem:x.find(e=>e.value===u),placeholder:"(optional) Select a beta template",onChange:e=>{d(e.value)},items:x})})}),(0,n.jsx)(b.VStack,{children:(0,n.jsx)(v.Button,{colorway:"primary",disabled:!i||!s||g,onClick:()=>{if(!i||!s)throw Error("Expected language and template");let t=e.find(e=>e.key===i);if(!t)throw Error(`Expected language with key ${i}`);!window.confirm(`Are you sure you want to map ${t.displayName} to the template ${c}?`)||g||m({variables:{input:{language:i,replId:s,betaReplId:u}}}).then(e=>{let t=e.data?.setLanguageTemplateRepl;t&&"message"in t&&a(t.message)})},text:"Submit"})})]})})}e.s(["default",0,function(){var e;let t,{data:a,loading:i,error:l,refetch:s}=(e={fetchPolicy:"cache-and-network",ssr:!1},t={...J,...e},r.useQuery(ea,t));if(i)return(0,n.jsx)("div",{children:"Loading..."});if(l)return(0,n.jsx)("div",{children:l.message});if(!a?.languages||!a.languageTemplateRepls)throw Error("Error loading language templates");let{languages:o,languageTemplateRepls:u}=a;return(0,n.jsxs)(b.VStack,{spacing:2,align:"stretch",children:[(0,n.jsxs)(b.VStack,{spacing:1,align:"stretch",children:[(0,n.jsx)(R.Header,{level:3,variant:"subheadDefault",children:"Language Templates"}),(0,n.jsxs)(R.Text,{children:["To perform a flagged rollout, create/find a flag called flag-beta-template-",(0,n.jsx)("span",{css:em.rcss.color.accentPrimaryDefault,children:"languageKey"}),", and set a beta template in the form below."]})]}),(0,n.jsxs)(b.VStack,{spacing:2,children:[(0,n.jsxs)("table",{children:[(0,n.jsx)("thead",{children:(0,n.jsxs)("tr",{children:[(0,n.jsx)("td",{children:(0,n.jsx)(R.Text,{children:"Language"})}),(0,n.jsx)("td",{children:(0,n.jsx)(R.Text,{children:"Template"})}),(0,n.jsx)("td",{children:(0,n.jsx)(R.Text,{children:"Beta Template (optional)"})})]})}),eR(o).map(e=>{let{icon:t,displayName:r,key:a,templateRepl:i,betaTemplateRepl:l}=e,o=i?.id,d=u.find(e=>e.id===o),c=l?.id,p=u.find(e=>e.id===c);return d?(0,n.jsx)(eC,{language:a,icon:t||"",displayName:r,repl:d,betaRepl:p,onRemove:()=>s()},o):(0,n.jsx)(eT,{language:a,icon:t||"",displayName:r},a)})]}),(0,n.jsx)(b.VStack,{spacing:1,align:"stretch",children:(0,n.jsx)(R.Header,{level:3,variant:"subheadDefault",children:"Set new language template"})}),(0,n.jsx)(ek,{languages:o,templates:u,onSubmit:()=>s()})]})]})}],771087);var eI=e.i(59897);let e_={},eE=t.gql`
    fragment CluiTemplateReplCategories2Results on TemplateCategoriesResults {
  results {
    id
    title
  }
}
    `,eU=t.gql`
    query CluiTemplateReplCategories2 {
  currentUser {
    ...CluiTemplateReplCurrentUser
  }
  templateCategories {
    ... on TemplateCategoriesResults {
      ...CluiTemplateReplCategories2Results
    }
  }
}
    ${eI.CluiTemplateReplCurrentUserFragmentDoc}
${eE}`,eA=t.gql`
    mutation CluiTemplateReplCategories2SetTemplateReplCategory($input: SetTemplateCategoryReplInput!) {
  setTemplateCategoryRepl(input: $input) {
    ... on TemplateCategoryReplResult {
      templateCategoryRepl {
        id
        templateCategoryId
      }
    }
    ... on NotFoundError {
      message
    }
    ... on UnauthorizedError {
      message
    }
    ... on UserError {
      message
    }
  }
}
    `,eL=t.gql`
    mutation CluiTemplateReplCategories2UnsetTemplateReplCategory($input: UnsetTemplateCategoryReplInput!) {
  unsetTemplateCategoryRepl(input: $input) {
    ... on TemplateCategoryReplResult {
      templateCategoryRepl {
        id
        templateCategoryId
      }
    }
    ... on NotFoundError {
      message
    }
    ... on UnauthorizedError {
      message
    }
    ... on UserError {
      message
    }
  }
}
    `;e.s(["useCluiTemplateReplCategories2Query",0,function(e){let t={...e_,...e};return r.useQuery(eU,t)},"useCluiTemplateReplCategories2SetTemplateReplCategoryMutation",0,function(e){let t={...e_,...e};return E.useMutation(eA,t)},"useCluiTemplateReplCategories2UnsetTemplateReplCategoryMutation",0,function(e){let t={...e_,...e};return E.useMutation(eL,t)}],796820)},167485,e=>{e.v({form:"BanReplAuthor-module__bbC0Sq__form",reasonInput:"BanReplAuthor-module__bbC0Sq__reasonInput"})},197992,e=>{"use strict";var t,r=e.i(276385),a=e.i(488081),i=e.i(389959),l=e.i(908796),n=e.i(682205),s=e.i(597853),o=e.i(619542),u=e.i(534141),d=e.i(828322),c=e.i(973245),p=e.i(951262);let m={},g=c.gql`
    mutation BanUserFromCommunity($username: String!, $reason: String!) {
  banCommunityUser(username: $username, reason: $reason) {
    ... on BannedBoardUser {
      id
    }
    ... on UserError {
      message
    }
  }
}
    `;var h=e.i(320216),x=e.i(643484),f=e.i(528710),j=e.i(8047),b=e.i(61732),v=e.i(167485);let y=b.SpecializedView.form;function R({username:e,onDone:t}){var a;let l,[n,s]=(0,i.useState)(""),{showConfirm:u,showError:d}=(0,h.default)(),[c,{loading:w}]=(a={onCompleted({banCommunityUser:e}){"UserError"===e.__typename?d(e.message):u("The user has been banned.")}},l={...m,...a},p.useMutation(g,l));return(0,r.jsxs)(b.View,{gap:24,children:[(0,r.jsx)(j.Header,{level:1,variant:"headerDefault",children:"Ban the author of the Repl?"}),(0,r.jsx)(j.Text,{children:"Are you sure you want to ban this user? All their Apps will be deleted and they will no longer be able to access their account."}),(0,r.jsxs)(y,{onSubmit:r=>{r.preventDefault(),n&&e?(c({variables:{username:e,reason:n}}),t()):d("Please provide a reason.")},clsx:v.default.form,children:[(0,r.jsx)(b.View,{gap:8,children:(0,r.jsx)(f.MultiLineInput,{placeholder:"Reason for banning the user",value:n,onChange:e=>s(e.currentTarget.value),clsx:v.default.reasonInput})}),(0,r.jsxs)(b.View,{row:!0,gap:8,justify:"end",children:[(0,r.jsx)(x.Button,{type:"button",text:"Cancel",onClick:()=>t()}),(0,r.jsx)(x.Button,{disabled:w,colorway:"negative",text:w?"Banning user...":"Yes, ban this user",type:"submit",iconLeft:(0,r.jsx)(o.default,{})})]})]})]})}var w=e.i(696664);let C={},S=c.gql`
    mutation ReviewTemplateReview($input: ReviewTemplateInput!) {
  reviewTemplate(input: $input) {
    ... on TemplateReview {
      id
      repl {
        id
        ...ReplViewReplActionsPermissions
      }
    }
    ... on UserError {
      message
    }
    ... on UnauthorizedError {
      message
    }
  }
}
    ${w.ReplViewReplActionsPermissionsFragmentDoc}`,T=b.SpecializedView.form;function k({replId:e,reviewType:t,onDone:a}){var i;let l,{showConfirm:o,showError:u}=(0,h.default)(),d=`Something went wrong ${"promote"===t?"promoting":"demoting"} this Template`,[c,m]=(i={variables:{input:{replId:e,shouldPromote:"promote"===t}},onError:({message:e})=>{u(e)},onCompleted:e=>{"TemplateReview"===e.reviewTemplate.__typename?(o(`Template successfully ${"promote"===t?"promoted":"demoted"}`),a()):"UnauthorizedError"===e.reviewTemplate.__typename||"UserError"===e.reviewTemplate.__typename?u(e.reviewTemplate.message):u(d)}},l={...C,...i},p.useMutation(S,l));return(0,r.jsxs)(b.View,{gap:24,children:[(0,r.jsx)(j.Header,{level:1,variant:"headerDefault",children:"promote"===t?"Promote Framework":"Demote Framework?"}),(0,r.jsxs)(T,{onSubmit:async e=>{e.preventDefault(),c()},gap:24,children:["promote"===t?(0,r.jsx)(j.Text,{children:"Promoting a Template will show the Template in the Create App modal."}):(0,r.jsx)(j.Text,{children:"Demoting a Template will remove the Template from the Create App modal."}),(0,r.jsxs)(b.View,{row:!0,gap:8,justify:"end",children:[(0,r.jsx)(x.Button,{type:"button",text:"Cancel",onClick:()=>a()}),"promote"===t?(0,r.jsx)(x.Button,{type:"submit",disabled:m.loading,colorway:"primary",iconLeft:(0,r.jsx)(s.default,{}),text:m.loading?"Promoting Framework...":"Promote Framework"}):(0,r.jsx)(x.Button,{type:"submit",disabled:m.loading,colorway:"negative",iconLeft:(0,r.jsx)(n.default,{}),text:m.loading?"Demoting Framework...":"Demote Framework"})]})]})]})}var I=e.i(488299),_=e.i(295231),E=e.i(528326),U=e.i(921125),A=((t=A||{}).warnAuthor="warnAuthor",t.banAuthor="banAuthor",t.reportRepl="reportRepl",t.unpublish="unpublish",t.promoteTemplate="promoteTemplate",t.demoteTemplate="demoteTemplate",t.modUnpublish="modUnpublish",t);e.s(["default",0,function({repl:e,currentUser:t}){let[c,p]=(0,i.useState)(null),m=new Map,g=(0,a.useRouter)(),h="/replEnvironmentDesktop"===g.pathname||"/replEnvironmentMobile"===g.pathname,x=(0,U.replLinkProps)(e);return(e.authorizations.editFileContents.isAuthorized&&!h&&m.set("edit",{label:"Edit App",onClick:()=>g.push(x.href,x.as),icon:(0,r.jsx)(u.default,{})}),t?.isModerator&&m.set("banauthor",{label:"Ban author",isMod:!0,icon:(0,r.jsx)(o.default,{}),onClick:()=>p("banAuthor"),isDestructive:!0}),t?.isAdmin&&e.publishedAs===l.PublishedReplKind.Template&&(e.templateReview?.promoted?m.set("demote",{label:"Demote Framework",icon:(0,r.jsx)(n.default,{}),isDestructive:!0,onClick:()=>p("demoteTemplate")}):m.set("promote",{label:"Promote Framework",icon:(0,r.jsx)(s.default,{}),onClick:()=>p("promoteTemplate")})),m.size)?(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(_.PopupMenu,{trigger:(0,r.jsx)(I.IconButton,{filled:!0,size:32,alt:"More",children:(0,r.jsx)(d.default,{size:16})}),onAction:e=>m.get(e)?.onClick(),children:Array.from(m).map(([e,t])=>(0,r.jsx)(_.MenuItem,{isDestructive:t.isDestructive,label:t.label,icon:t.icon,id:e},e))}),(0,r.jsx)(E.Modal,{isOpen:"banAuthor"===c,onRequestClose:()=>p(null),children:(0,r.jsx)(R,{username:e.owner?.username,onDone:()=>p(null)})}),(0,r.jsx)(E.Modal,{isOpen:"demoteTemplate"===c,onRequestClose:()=>p(null),children:(0,r.jsx)(k,{replId:e.id,reviewType:"demote",onDone:()=>p(null)})}),(0,r.jsx)(E.Modal,{isOpen:"promoteTemplate"===c,onRequestClose:()=>p(null),children:(0,r.jsx)(k,{replId:e.id,reviewType:"promote",onDone:()=>p(null)})})]}):null}],197992)},541271,e=>{"use strict";var t=e.i(276385),r=e.i(656077),a=e.i(602686),i=e.i(346781),l=e.i(415541),n=e.i(709485);e.i(373104);var s=e.i(849492),o=e.i(504099),u=e.i(462229),d=e.i(316431),c=e.i(691636),p=e.i(419635),m=e.i(488299),g=e.i(528710),h=e.i(335670),x=e.i(8047),f=e.i(61732);let j=(0,u.cssRecord)({header:[{[`@media (max-width: ${o.BREAKPOINTS.tabletMax}px)`]:[c.rcss.colWithGap(16)],[`@media (min-width: ${o.BREAKPOINTS.tabletMin+1}px)`]:[c.rcss.rowWithGap(8),c.rcss.align.start,c.rcss.justify.spaceBetween]}],headerBottom:[{[`@media (max-width: ${o.BREAKPOINTS.tabletMax}px)`]:[c.rcss.rowWithGap(16),c.rcss.justify.spaceBetween],[`@media (min-width: ${o.BREAKPOINTS.tabletMin+1}px)`]:[c.rcss.rowWithGap(16),c.rcss.justify.end]}],backButtonWrapper:[c.rcss.mb(32),{marginRight:"auto"}],searchBoxWrapper:[{position:"relative",flex:1,[`@media (min-width: ${o.BREAKPOINTS.mobileMax+1}px)`]:[c.rcss.flex.row,c.rcss.align.start,c.rcss.justify.end,c.rcss.width(220)]}],searchIconButtonWrapper:[c.rcss.center,c.rcss.borderRadius(8),c.rcss.pr(4),c.rcss.width(24),c.rcss.height(24),c.rcss.top(4),c.rcss.right(1),c.rcss.position.absolute,{transition:"120ms ease-out"}]}),b=[{value:s.OrderBy.Recent,title:"New"},{value:s.OrderBy.Forks,title:"Popular"}];e.s(["TemplatesHeader",0,function({title:e,description:o,searchInputValue:u,setSearchInputValue:v,orderBy:y=s.OrderBy.Forks,setOrderBy:R,showOrderBy:w=!1,showBackButton:C=!1,showHowToLink:S=!1,variant:T="default",actionButton:k,statusBanner:I}){let _="https://docs.replit.com/replit-workspace/templates";return(0,t.jsxs)(f.View,{css:j.header,children:[(0,t.jsxs)(f.View,{grow:!0,shrink:!0,gap:16,children:[(0,t.jsxs)(f.View,{gap:8,children:[C?(0,t.jsx)(f.View,{css:j.backButtonWrapper,children:(0,t.jsx)(p.ButtonLink,{href:"/templates/templates",as:"/templates",text:"Back to all Frameworks",iconLeft:(0,t.jsx)(r.default,{})})}):null,(0,t.jsx)(x.Header,{level:1,variant:"headerBig",children:e}),o?(0,t.jsx)(x.Text,{variant:"subheadBig",color:"dimmer",children:o}):null]}),I,S?(0,t.jsx)("a",{href:_,target:"_blank",onClick:()=>{(0,l.track)(n.events.EXTERNAL_LINK_VIEWED,{url:_,campaign:"templates"})},children:"How to publish a Framework"}):null]}),(0,t.jsxs)(f.View,{css:j.headerBottom,children:[k,w?(0,t.jsx)(d.Select,{css:["higher"===T&&c.rcss.backgroundColor.backgroundHigher],"aria-label":"Sort by",items:b,selectedItem:b.find(e=>e.value===y),onChange:e=>{R&&(e.value===s.OrderBy.Recent?R(s.OrderBy.Recent):R(s.OrderBy.Forks))}}):null,(0,t.jsxs)(f.View,{css:j.searchBoxWrapper,children:[(0,t.jsx)(g.Input,{value:u,onChange:e=>v(e.currentTarget.value),placeholder:"Search Frameworks",css:["higher"===T&&c.rcss.backgroundColor.backgroundHigher],type:"search","aria-label":"Search Frameworks"}),(0,t.jsx)(h.Surface,{background:"default",css:j.searchIconButtonWrapper,children:u?(0,t.jsx)(m.IconButton,{alt:"Clear",onClick:()=>v(""),children:(0,t.jsx)(a.default,{})}):(0,t.jsx)(i.default,{})})]})]})]})}])},456147,e=>{e.v({modalContent:"UserTipForm-module__6zOkyG__modalContent"})},964228,e=>{e.v({container:"index-module__HPzRfq__container",errorContainer:"index-module__HPzRfq__errorContainer",header:"index-module__HPzRfq__header",modalFooter:"index-module__HPzRfq__modalFooter",paginationContainer:"index-module__HPzRfq__paginationContainer",tableRow:"index-module__HPzRfq__tableRow"})},228759,e=>{e.v({surfcae:"OutputContainer-module__E34JzG__surfcae"})},141738,e=>{e.v({loading:"UserCli-module__fP09pW__loading",output:"UserCli-module__fP09pW__output",root:"UserCli-module__fP09pW__root"})},339487,477743,859194,e=>{"use strict";var t=e.i(276385),r=e.i(389959),a=e.i(190927),i=e.i(109273),l=e.i(197106),n=e.i(659042),s=e.i(712771),o=e.i(5257),u=e.i(269848),d=e.i(525864),c=e.i(255701),p=e.i(195206),m=e.i(491194),g=e.i(612343);e.i(135069);var h=e.i(458713),x=e.i(442121),f=e.i(951262),j=e.i(89610),b=e.i(443197),v=e.i(196064),y=e.i(762902),R=e.i(126585),w=e.i(166295),C=e.i(771087),S=e.i(796820),T=e.i(657929),k=e.i(602686),I=e.i(416746),_=e.i(40916),E=e.i(110481),U=e.i(320216),A=e.i(197992),L=e.i(908904),D=e.i(541271),P=e.i(373104),$=e.i(849492),O=e.i(79949),B=e.i(480028),V=e.i(316431),M=e.i(919073),F=e.i(691636),N=e.i(488299),q=e.i(744006),z=e.i(108431),G=e.i(8047),Q=e.i(61732),W=e.i(365757);let H={value:0,title:"Select category"};function Y({template:e,categories:a,currentUser:i}){let{showError:l}=(0,U.default)(),[n,s]=(0,r.useState)(e.templateCategories),[o,d]=(0,r.useState)(H),[c,{loading:p}]=(0,S.useCluiTemplateReplCategories2SetTemplateReplCategoryMutation)({onError:e=>{l(e.message)},onCompleted:e=>{switch(e.setTemplateCategoryRepl?.__typename){case"NotFoundError":case"UnauthorizedError":case"UserError":l(e.setTemplateCategoryRepl.message);break;case"TemplateCategoryReplResult":{let t=e.setTemplateCategoryRepl.templateCategoryRepl.templateCategoryId,r=a.find(e=>e.id===t);if(!r)return;s([r,...n]),d(H)}}}}),[m,{loading:g}]=(0,S.useCluiTemplateReplCategories2UnsetTemplateReplCategoryMutation)({onError:e=>{l(e.message)},onCompleted:e=>{switch(e.unsetTemplateCategoryRepl?.__typename){case"NotFoundError":case"UnauthorizedError":case"UserError":l(e.unsetTemplateCategoryRepl.message);break;case"TemplateCategoryReplResult":{let t=e.unsetTemplateCategoryRepl.templateCategoryRepl.templateCategoryId;s(n.filter(e=>e?.id!==t)),d(H)}}}}),h=a.filter(e=>!n.find(t=>e.id===t?.id)).map(({id:e,title:t})=>({value:e,title:t}));return(0,t.jsxs)(M.ShadesSurface,{css:[F.rcss.overflow("visible"),{border:"1px solid "+B.tokens.outlineDimmest}],p:16,br:8,children:[(0,t.jsxs)(Q.View,{row:!0,gap:8,align:"start",children:[(0,t.jsx)(Q.View,{css:[F.rcss.flex.wrap],grow:!0,shrink:0,row:!0,gap:8,align:"center",children:(0,t.jsxs)(Q.View,{gap:8,children:[g?(0,t.jsx)(u.default,{size:16,css:F.rcss.mb(8)}):(0,t.jsx)(Q.View,{row:!0,gap:8,css:[F.rcss.flex.wrap],children:n.map(r=>{if(r)return(0,t.jsxs)(Q.View,{css:[F.rcss.backgroundColor.backgroundHigher,F.rcss.mb(8)],br:8,row:!0,gap:0,children:[(0,t.jsx)(q.Pill,{text:r.title}),(0,t.jsx)(N.IconButton,{alt:"Remove category from template",onClick:()=>{var t;return t=r.id,void m({variables:{input:{replId:e.id,templateCategoryId:t}}})},tooltipBehavior:"hidden",children:(0,t.jsx)(k.default,{})})]},r.id)})}),(0,t.jsxs)(Q.View,{row:!0,gap:8,children:[(0,t.jsx)(W.default,{alt:e.title,iconUrl:e.iconUrl,size:24}),(0,t.jsx)(G.Text,{variant:"subheadBig",multiline:!1,children:e.title})]})]})}),(0,t.jsxs)(Q.View,{row:!0,gap:4,align:"center",children:[(0,t.jsxs)(Q.View,{css:[F.rcss.backgroundColor.backgroundHigher],align:"center",br:8,row:!0,gap:2,children:[(0,t.jsx)(V.Select,{"aria-label":"Select category",disabled:p||g,css:{borderRight:`1px solid ${B.tokens.backgroundDefault}`,borderTopRightRadius:0,borderBottomRightRadius:0},placeholder:"Select category",initialSelectedItem:o,selectedItem:o,items:h,onChange:e=>d(e)}),(0,t.jsx)(Q.View,{px:4,children:p?(0,t.jsx)(u.default,{size:16}):(0,t.jsx)(N.IconButton,{alt:"Add selected category to template",onClick:()=>{o&&o.value!==H.value&&c({variables:{input:{replId:e.id,templateCategoryId:o.value}}})},tooltipBehavior:"hidden",children:(0,t.jsx)(_.default,{})})})]}),(0,t.jsx)(A.default,{repl:e,currentUser:i})]})]}),(0,t.jsx)(Q.View,{grow:!0,shrink:!0,justify:"end",children:(0,t.jsx)(G.Text,{color:"dimmest",maxLines:3,multiline:!1,children:e.description||"--"})}),(0,t.jsx)(Q.View,{children:(0,t.jsx)(L.OwnerLink,{owner:e.owner||null})})]})}var K=e.i(59897);function Z({template:e,currentUser:r}){return(0,t.jsxs)(M.ShadesSurface,{css:[F.rcss.overflow("visible"),{border:"1px solid "+B.tokens.outlineDimmest}],p:16,br:8,children:[(0,t.jsxs)(Q.View,{row:!0,gap:8,align:"start",children:[(0,t.jsx)(Q.View,{css:[F.rcss.flex.wrap],grow:!0,shrink:0,row:!0,gap:8,align:"center",children:(0,t.jsx)(Q.View,{gap:8,children:(0,t.jsxs)(Q.View,{row:!0,gap:8,children:[(0,t.jsx)(W.default,{alt:e.title,iconUrl:e.iconUrl,size:24}),(0,t.jsx)(G.Text,{variant:"subheadBig",multiline:!1,children:e.title})]})})}),(0,t.jsx)(Q.View,{row:!0,gap:4,align:"center",children:(0,t.jsx)(A.default,{repl:e,currentUser:r})})]}),(0,t.jsx)(Q.View,{grow:!0,shrink:!0,justify:"end",children:(0,t.jsx)(G.Text,{color:"dimmest",maxLines:3,multiline:!1,children:e.description||"--"})}),(0,t.jsx)(Q.View,{children:(0,t.jsx)(L.OwnerLink,{owner:e.owner||null})})]})}var J=e.i(261348),X=e.i(973245),ee=e.i(304277),et=e.i(566901);let er={},ea=X.gql`
    fragment UserTipFields on UserTip {
  id
  title
  description
  content
  tags
  priority
  externalUrl
  criteria
  ctaTrigger
  ctaLabel
  publishedAt
  timeCreated
  timeUpdated
  timeDeleted
}
    `,ei=X.gql`
    query UserTipsManagementTable($after: String, $count: Int, $showArchived: Boolean) {
  userTips(after: $after, count: $count, showArchived: $showArchived) {
    items {
      ...UserTipFields
    }
    pageInfo {
      hasNextPage
      hasPreviousPage
      nextCursor
      previousCursor
    }
  }
}
    ${ea}`,el=X.gql`
    mutation CreateUserTip($title: String!, $description: String!, $content: String, $tags: [String!], $priority: Int, $externalUrl: String, $criteria: String, $ctaTrigger: String, $ctaLabel: String, $publishedAt: DateTime) {
  createUserTip(
    title: $title
    description: $description
    content: $content
    tags: $tags
    priority: $priority
    externalUrl: $externalUrl
    criteria: $criteria
    ctaTrigger: $ctaTrigger
    ctaLabel: $ctaLabel
    publishedAt: $publishedAt
  ) {
    ...UserTipFields
  }
}
    ${ea}`,en=X.gql`
    mutation UpdateUserTip($id: ID!, $title: String, $description: String, $content: String, $tags: [String!], $priority: Int, $externalUrl: String, $criteria: String, $ctaTrigger: String, $ctaLabel: String, $publishedAt: DateTime, $archived: Boolean) {
  updateUserTip(
    id: $id
    title: $title
    description: $description
    content: $content
    tags: $tags
    priority: $priority
    externalUrl: $externalUrl
    criteria: $criteria
    ctaTrigger: $ctaTrigger
    ctaLabel: $ctaLabel
    publishedAt: $publishedAt
    archived: $archived
  ) {
    ...UserTipFields
  }
}
    ${ea}`;var es=e.i(534141),eo=e.i(965097),eu=e.i(828322),ed=e.i(820228),ec=e.i(302973),ep=e.i(94516),em=e.i(789277),eg=e.i(301651),eh=e.i(528710),ex=e.i(585544),ef=e.i(19322),ej=e.i(456147);let eb=({initialTip:e,formRef:a})=>{let{formValues:i,errors:l,handleInputChange:n,handleDateChange:s,validateForm:o}=(e=>{let[t,a]=(0,r.useState)({id:e?.id||void 0,title:e?.title||"",description:e?.description||"",content:e?.content||"",tags:(e?.tags||[]).join(", "),priority:String(e?.priority||0),externalUrl:e?.externalUrl||"",criteria:e?.criteria||"",ctaTrigger:e?.ctaTrigger||"",ctaLabel:e?.ctaLabel||"",publishedAt:e?.publishedAt?new Date(e.publishedAt):null}),[i,l]=(0,r.useState)({}),n=(0,r.useCallback)(e=>t=>{a(r=>({...r,[e]:t.target.value}))},[]),s=(0,r.useCallback)(e=>{a(t=>({...t,publishedAt:e}))},[]);return{formValues:t,errors:i,handleInputChange:n,handleDateChange:s,resetForm:(0,r.useCallback)(e=>{a({id:e?.id||void 0,title:e?.title||"",description:e?.description||"",content:e?.content||"",tags:(e?.tags||[]).join(", "),priority:String(e?.priority||0),externalUrl:e?.externalUrl||"",criteria:e?.criteria||"",ctaTrigger:e?.ctaTrigger||"",ctaLabel:e?.ctaLabel||"",publishedAt:e?.publishedAt?new Date(e.publishedAt):null}),l({})},[]),validateForm:()=>{let e={};return t.title.trim()||(e.title="Title is required"),t.description.trim()||(e.description="Description is required"),t.priority&&isNaN(Number(t.priority))&&(e.priority="Priority must be a number"),t.externalUrl&&!(e=>{try{return new URL(e),!0}catch(e){return!1}})(t.externalUrl)&&(e.externalUrl="Please enter a valid URL"),t.ctaTrigger.trim()||t.externalUrl.trim()||(e.ctaTrigger="Either CTA Trigger or External URL is required",e.externalUrl="Either CTA Trigger or External URL is required"),l(e),0===Object.keys(e).length}}})(e);(0,r.useImperativeHandle)(a,()=>({formValues:i,validateForm:o}),[i,o]);let u=(0,ec.getLocalTimeZone)();return(0,t.jsxs)(Q.View,{clsx:ej.default.modalContent,gap:16,children:[(0,t.jsxs)(Q.View,{children:[(0,t.jsx)(G.Text,{children:"Title *"}),(0,t.jsx)(eh.Input,{value:i.title,onChange:n("title"),placeholder:"Tip title"}),l.title?(0,t.jsx)(G.Text,{color:"default",style:{color:B.tokens.accentNegativeStronger},children:l.title}):null]}),(0,t.jsxs)(Q.View,{children:[(0,t.jsx)(G.Text,{children:"Description *"}),(0,t.jsx)(eh.MultiLineInput,{value:i.description,onChange:n("description"),placeholder:"Short description of the tip",rows:2}),l.description?(0,t.jsx)(G.Text,{color:"default",style:{color:B.tokens.accentNegativeStronger},children:l.description}):null]}),(0,t.jsxs)(Q.View,{children:[(0,t.jsx)(G.Text,{children:"Criteria"}),(0,t.jsx)(eh.MultiLineInput,{value:i.criteria,onChange:n("criteria"),rows:2}),(0,t.jsx)(G.Text,{variant:"small",color:"dimmer",children:"Specific criteria or context for when this tip should be shown to users (optional and internal)"})]}),(0,t.jsxs)(Q.View,{children:[(0,t.jsx)(G.Text,{children:"External URL"}),(0,t.jsx)(eh.Input,{value:i.externalUrl,onChange:n("externalUrl"),placeholder:"e.g. https://example.com/documentation"}),(0,t.jsx)(G.Text,{variant:"small",color:"dimmer",children:"External link for additional resources. Either this or CTA Trigger is required."}),l.externalUrl?(0,t.jsx)(G.Text,{color:"default",style:{color:B.tokens.accentNegativeStronger},children:l.externalUrl}):null]}),(0,t.jsxs)(Q.View,{children:[(0,t.jsx)(G.Text,{children:"CTA Trigger"}),(0,t.jsx)(ef.Select,{"aria-label":"CTA Trigger",items:[{id:"",label:"None (empty)"},{id:"bonsai_tour",label:"Launch Bonsai tour"},{id:"auth_pane",label:"Open authentication pane"},{id:"database_pane",label:"Open database pane"},{id:"create_new_chat",label:"Create new agent chat"},{id:"security_scan_pane",label:"Open security scanner pane"}],defaultSelectedKey:i.ctaTrigger||"",onSelectionChange:e=>{n("ctaTrigger")({target:{value:""===e?"":String(e)}})},children:e=>(0,t.jsx)(ex.ListBoxItem,{id:e.id,label:e.label},e.id)}),(0,t.jsx)(G.Text,{variant:"small",color:"dimmer",children:"String identifier to match elements or actions in the codebase. Either this or External URL is required."}),l.ctaTrigger?(0,t.jsx)(G.Text,{color:"default",style:{color:B.tokens.accentNegativeStronger},children:l.ctaTrigger}):null]}),(0,t.jsxs)(Q.View,{children:[(0,t.jsx)(G.Text,{children:"CTA Label"}),(0,t.jsx)(eh.Input,{value:i.ctaLabel,onChange:n("ctaLabel"),placeholder:"e.g., Get Started, Learn More, Try Now"}),(0,t.jsx)(G.Text,{variant:"small",color:"dimmer",children:'Text to display on the call-to-action button. Leave empty to use default "Learn more".'})]}),(0,t.jsxs)(Q.View,{children:[(0,t.jsx)(G.Text,{children:"Tags"}),(0,t.jsx)(eh.Input,{value:i.tags,onChange:n("tags"),placeholder:"Enter tags separated by commas"}),(0,t.jsx)(G.Text,{variant:"small",color:"dimmer",children:'Comma-separated list of tags (e.g., "beginner, agent, workspace")'})]}),(0,t.jsxs)(Q.View,{children:[(0,t.jsx)(G.Text,{children:"Priority"}),(0,t.jsx)(eh.Input,{type:"number",value:i.priority,onChange:n("priority")}),(0,t.jsx)(G.Text,{variant:"small",color:"dimmer",children:"Lower numbers are higher priority (default: 0)"}),l.priority?(0,t.jsx)(G.Text,{color:"default",style:{color:B.tokens.accentNegativeStronger},children:l.priority}):null]}),(0,t.jsxs)(Q.View,{children:[(0,t.jsx)(G.Text,{children:"Published Date"}),(0,t.jsx)(eg.default,{granularity:"minute",hourCycle:24,value:i.publishedAt?(0,em.toCalendarDateTime)((0,ep.parseAbsolute)(i.publishedAt.toISOString(),u)):void 0,onChange:e=>s(e?e.toDate(u):null)}),(0,t.jsx)(G.Text,{variant:"small",color:"dimmer",children:"When the tip should be published. Leave empty for draft state."})]})]})};var ev=e.i(643484),ey=e.i(775007),eR=e.i(222826),ew=e.i(609912),eC=e.i(295231),eS=e.i(528326),eT=e.i(984119),ek=e.i(508454),eI=e.i(964228);let e_={LanguageTemplates:C.default,TemplateReplCategories2Assign:function(){let[e,a]=(0,r.useState)($.OrderBy.Recent),{data:i,loading:l,error:n}=(0,S.useCluiTemplateReplCategories2Query)(),{templates:s,loading:o,error:d,loadMore:c,hasMore:p,setSearchInputValue:m,searchInputValue:g}=(0,P.default)({orderBy:e,promotionStatus:O.PromotionStatus.Promoted,pageSize:20}),{targetRef:h}=(0,E.default)({onLoadMore:c,rootMargin:"0px 0px 300px 0px"});return d||n?(0,t.jsx)(Q.View,{children:d||n?.message}):l||i?(0,t.jsxs)(Q.View,{gap:32,children:[(0,t.jsx)(D.TemplatesHeader,{title:"Assign categories",description:"",searchInputValue:g,setSearchInputValue:m,orderBy:e,setOrderBy:a,showOrderBy:!0,variant:"higher"}),o||0!==s.length?null:(0,t.jsx)(Q.View,{css:[{alignSelf:"start"}],children:(0,t.jsx)(z.StatusBanner,{icon:(0,t.jsx)(I.default,{}),text:`No Templates found.${""!==g?" Try another search.":""}`})}),l?(0,t.jsx)(Q.View,{align:"center",justify:"center",py:16,children:(0,t.jsx)(u.default,{size:24})}):i&&i.templateCategories&&(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)(Q.View,{gap:16,children:s.map(e=>(0,t.jsx)(Y,{template:e,currentUser:i.currentUser??void 0,categories:i.templateCategories?.__typename==="TemplateCategoriesResults"?i.templateCategories.results:[]},e.id))}),(0,t.jsxs)(Q.View,{align:"center",justify:"center",py:16,children:[o?(0,t.jsx)(u.default,{size:24}):p&&(0,t.jsx)(N.IconButton,{tooltipBehavior:"hidden",alt:"Show more",onClick:c,children:(0,t.jsx)(T.default,{})}),(0,t.jsx)(Q.View,{innerRef:h})]})]})]}):(0,t.jsx)(Q.View,{children:"Could not load template categories"})},TemplateReplSubmissions:function(){let[e,a]=(0,r.useState)($.OrderBy.Recent),{data:i,loading:l,error:n}=(0,K.useCluiTemplateReplSubmissionsQuery)(),{templates:s,loading:o,error:d,loadMore:c,hasMore:p,setSearchInputValue:m,searchInputValue:g}=(0,P.default)({orderBy:e,promotionStatus:O.PromotionStatus.NotPromoted,pageSize:20}),{targetRef:h}=(0,E.default)({onLoadMore:c,rootMargin:"0px 0px 300px 0px"});return d||n?(0,t.jsx)(Q.View,{children:d||n?.message}):l||i?(0,t.jsxs)(Q.View,{gap:32,children:[(0,t.jsx)(D.TemplatesHeader,{title:"Template submissions",description:"",searchInputValue:g,setSearchInputValue:m,orderBy:e,setOrderBy:a,showOrderBy:!0,variant:"higher"}),o||0!==s.length?null:(0,t.jsx)(Q.View,{css:[{alignSelf:"start"}],children:(0,t.jsx)(z.StatusBanner,{icon:(0,t.jsx)(I.default,{}),text:`No Templates found.${""!==g?" Try another search.":""}`})}),l?(0,t.jsx)(Q.View,{align:"center",justify:"center",py:16,children:(0,t.jsx)(u.default,{size:24})}):s&&(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)(Q.View,{gap:16,children:s.map(e=>(0,t.jsx)(Z,{template:e,currentUser:i?.currentUser??void 0},e.id))}),(0,t.jsxs)(Q.View,{align:"center",justify:"center",py:16,children:[o?(0,t.jsx)(u.default,{size:24}):p&&(0,t.jsx)(N.IconButton,{tooltipBehavior:"hidden",alt:"Show more",onClick:c,children:(0,t.jsx)(T.default,{})}),(0,t.jsx)(Q.View,{innerRef:h})]})]})]}):(0,t.jsx)(Q.View,{children:"Could not load template submissions data"})},UserTipsManagementTable:e=>{var a;let i,[l,n]=(0,r.useState)(1),[s,o]=(0,r.useState)(!1),[d,c]=(0,r.useState)(!1),[p,g]=(0,r.useState)(null),h=(0,r.useRef)(null),x=(0,r.useRef)(null),j=(0,r.useMemo)(()=>{if(1!==l)return((l-1)*50).toString()},[l]),{data:b,loading:v,error:y}=(a={variables:{after:j,count:50,showArchived:s},fetchPolicy:"cache-and-network",notifyOnNetworkStatusChange:!0,ssr:!1},i={...er,...a},ee.useQuery(ei,i)),{createTip:R,updateTip:w,archiveTip:C,handleUnarchive:S,createLoading:T,updateLoading:k}=(({showArchived:e,cursor:t,itemsPerPage:a})=>{let i,l,[n,{loading:s}]=(i={...er,...void 0},f.useMutation(el,i)),[o,{loading:u}]=(l={...er,...void 0},f.useMutation(en,l)),d=(0,r.useCallback)(async r=>await n({variables:{title:r.title,description:r.description,content:r.content||null,tags:r.tags?r.tags.split(",").map(e=>e.trim()).filter(Boolean):[],priority:r.priority?parseInt(r.priority,10):null,externalUrl:r.externalUrl||null,criteria:r.criteria||null,ctaTrigger:r.ctaTrigger||null,ctaLabel:r.ctaLabel||null,publishedAt:r.publishedAt||null},refetchQueries:[{query:ei,variables:{after:t,count:a,showArchived:e}}]}),[n,t,a,e]),c=(0,r.useCallback)(async e=>{if(!e.id)throw Error("ID is required for updating a tip");return await o({variables:{id:e.id,title:e.title,description:e.description,content:e.content||null,tags:e.tags?e.tags.split(",").map(e=>e.trim()).filter(Boolean):[],priority:e.priority?parseInt(e.priority,10):null,externalUrl:e.externalUrl||null,criteria:e.criteria||null,ctaTrigger:e.ctaTrigger||null,ctaLabel:e.ctaLabel||null,publishedAt:e.publishedAt||null}})},[o]);return{createTip:d,updateTip:c,archiveTip:(0,r.useCallback)(async e=>await o({variables:{id:e,archived:!0}}),[o]),handleUnarchive:(0,r.useCallback)(r=>{r.id&&o({variables:{id:r.id,archived:!1},refetchQueries:["UserTipsManagementTable"],update:i=>{e&&function({cache:e,tipId:t,cursor:r,itemsPerPage:a,showArchived:i}){let l=e.readQuery({query:ei,variables:{after:r,count:a,showArchived:i}});l?.userTips?.items&&e.writeQuery({query:ei,variables:{after:r,count:a,showArchived:i},data:{userTips:{...l.userTips,items:l.userTips.items.filter(e=>e.id!==t)}}})}({cache:i,tipId:r.id,cursor:t,itemsPerPage:a,showArchived:!0})}})},[o,e,t,a]),createLoading:s,updateLoading:u}})({showArchived:s,cursor:j,itemsPerPage:50}),I=(0,r.useMemo)(()=>[...b?.userTips?.items||[]].sort((e,t)=>e.priority!==t.priority?e.priority-t.priority:new Date(e.timeCreated).getTime()-new Date(t.timeCreated).getTime()),[b]),E=(0,r.useMemo)(()=>b?.userTips?.pageInfo,[b]),U=(0,r.useCallback)(()=>{g(null),c(!0)},[]),A=(0,r.useCallback)(async()=>{if(h.current&&h.current.validateForm())try{await R(h.current.formValues),c(!1)}catch{}},[R]),L=(0,r.useCallback)(async()=>{if(x.current&&x.current.validateForm())try{await w(x.current.formValues),g(null)}catch{}},[w]),D=(0,r.useCallback)(()=>{g(null)},[]),P=[{key:"title",label:"Title",isRowHeader:!0},{key:"tags",label:"Tags"},{key:"timeCreated",label:"Created"},{key:"actions",label:"",alignment:"end"}];return y?(0,t.jsx)(Q.View,{clsx:eI.default.errorContainer,children:(0,t.jsxs)(G.Text,{color:"dimmer",children:["Error loading user tips: ",y.message]})}):(0,t.jsxs)(Q.View,{clsx:eI.default.container,children:[(0,t.jsxs)(Q.View,{row:!0,align:"center",justify:"space-between",clsx:eI.default.header,children:[(0,t.jsxs)(Q.View,{row:!0,align:"center",gap:16,children:[(0,t.jsx)(G.Text,{variant:"subheadDefault",children:"User Tips Management"}),(0,t.jsx)(Q.View,{row:!0,align:"center",gap:8,children:(0,t.jsxs)(Q.SpecializedView.label,{gap:4,row:!0,children:[(0,t.jsx)("input",{type:"checkbox",checked:s,onChange:e=>{o(e.target.checked),n(1)}}),(0,t.jsx)(G.Text,{children:"Show archived"})]})})]}),(0,t.jsx)(ev.Button,{text:"Create Tip",onClick:U,colorway:"primary",iconLeft:(0,t.jsx)(_.default,{})})]}),(0,t.jsx)(ew.IndexTable,{title:"User Tips",items:I,loading:v&&0===I.length,emptyState:(0,t.jsx)(ey.default,{title:v&&0===I.length?"Loading user tips...":"No user tips found",description:v&&0===I.length?"":"Get started by creating your first user tip",illustration:v&&0===I.length?(0,t.jsx)(u.default,{size:32,fill:B.tokens.foregroundDimmer}):(0,t.jsx)(eo.default,{size:32,fill:B.tokens.foregroundDimmer})}),columns:P,autoLayout:!0,children:e=>{var r;return(0,t.jsxs)(ek.TableRow,{id:e.id,columns:P,"data-archived":!!e.timeDeleted,clsx:eI.default.tableRow,children:[(0,t.jsx)(eT.TableCell,{children:(0,t.jsxs)(Q.View,{children:[e.externalUrl?(0,t.jsx)("a",{href:e.externalUrl,target:"_blank",rel:"noopener noreferrer",style:{cursor:"pointer",textDecoration:"underline",color:"inherit"},children:e.title}):(0,t.jsx)(G.Text,{children:e.title}),e.description?(0,t.jsx)(G.Text,{variant:"small",color:"dimmer",children:e.description.length>100?`${e.description.slice(0,100)}...`:e.description}):null,e.ctaLabel||e.ctaTrigger?(0,t.jsxs)(Q.View,{row:!0,gap:8,style:{marginTop:4},children:[e.ctaLabel?(0,t.jsxs)(G.Text,{variant:"small",color:"dimmer",children:["CTA: ",e.ctaLabel]}):null,e.ctaTrigger?(0,t.jsxs)(G.Text,{variant:"small",color:"dimmer",children:["Trigger: ",e.ctaTrigger]}):null]}):null]})}),(0,t.jsx)(eT.TableCell,{children:(0,t.jsx)(Q.View,{row:!0,wrap:!0,gap:4,children:(e.tags||[]).map(e=>e?(0,t.jsx)(q.Pill,{text:e},e):null)})}),(0,t.jsx)(eT.TableCell,{children:(0,t.jsx)(G.Text,{children:e.timeCreated&&(r=e.timeCreated)?(0,J.format)(new Date(r),"MM/dd/yy"):"-"})}),(0,t.jsx)(eT.TableCell,{children:(0,t.jsxs)(eC.PopupMenu,{trigger:(0,t.jsx)(N.IconButton,{alt:"Actions",size:24,children:(0,t.jsx)(eu.default,{})}),"aria-label":`Actions for ${e.title}`,children:[(0,t.jsx)(eC.MenuItem,{label:"Edit",icon:(0,t.jsx)(es.default,{}),onAction:()=>g(e)}),e.timeDeleted?(0,t.jsx)(eC.MenuItem,{label:"Restore",icon:(0,t.jsx)(ed.default,{}),onAction:()=>S(e)}):(0,t.jsx)(eC.MenuItem,{label:"Archive",icon:(0,t.jsx)(m.default,{}),onAction:()=>C(e.id)})]})})]},e.id)}}),E&&(E.hasNextPage||E.hasPreviousPage)?(0,t.jsx)(Q.View,{clsx:eI.default.paginationContainer,children:(0,t.jsx)(eR.default,{currentPage:l-1,pageSize:50,totalItems:50*l+50*!!E.hasNextPage,goToPreviousPage:()=>n(e=>Math.max(1,e-1)),goToNextPage:()=>{E.hasNextPage&&n(e=>e+1)}})}):null,(0,t.jsxs)(eS.Modal,{isOpen:d,onRequestClose:()=>c(!1),maxWidth:600,children:[(0,t.jsx)(eb,{formRef:h}),(0,t.jsxs)(Q.View,{row:!0,justify:"end",gap:8,clsx:eI.default.modalFooter,children:[(0,t.jsx)(ev.Button,{text:"Cancel",onClick:()=>c(!1),colorway:"negative",disabled:T}),(0,t.jsx)(ev.Button,{text:T?"Creating...":"Create",onClick:A,colorway:"primary",disabled:T})]})]}),(0,t.jsxs)(eS.Modal,{isOpen:null!==p,onRequestClose:D,maxWidth:600,children:[(0,t.jsx)(eb,{initialTip:p,formRef:x}),(0,t.jsxs)(Q.View,{row:!0,justify:"end",gap:8,clsx:eI.default.modalFooter,children:[(0,t.jsx)(ev.Button,{text:"Cancel",onClick:D,colorway:"negative",disabled:k}),(0,t.jsx)(ev.Button,{text:k?"Updating...":"Update",onClick:L,colorway:"primary",disabled:k})]})]})]})},DeleteTipInteractionsForm:w.default};var eE=e.i(174423),eU=e.i(53382);let eA=e=>{let a=(0,r.useMemo)(()=>e.columns.map(e=>({header:e.label,accessorKey:e.key})),[e.columns]),{getHeaderGroups:i,getRowModel:l,getState:n,getPageCount:s,previousPage:o,getCanPreviousPage:u,nextPage:d,getCanNextPage:c}=(0,eE.useReactTable)({columns:a,data:e.rows,getCoreRowModel:(0,eU.getCoreRowModel)(),getPaginationRowModel:(0,eU.getPaginationRowModel)(),initialState:{pagination:{pageIndex:0,pageSize:20}}}),p=[F.rcss.textAlign.left,F.rcss.p(8)];return(0,t.jsxs)("div",{css:[F.rcss.display.grid,{gridRowGap:B.tokens.space24}],children:[(0,t.jsxs)("table",{css:[F.rcss.display.block,F.rcss.width("100%")],children:[(0,t.jsx)("thead",{children:i().map(e=>(0,t.jsx)("tr",{children:e.headers.map(e=>(0,t.jsx)("th",{css:p,children:e.isPlaceholder?null:(0,eE.flexRender)(e.column.columnDef.header,e.getContext())},e.id))},e.id))}),(0,t.jsx)("tbody",{children:l().rows.map(e=>(0,t.jsx)("tr",{children:e.getVisibleCells().map(e=>(0,t.jsx)("td",{css:p,children:(0,eE.flexRender)(e.column.columnDef.cell,e.getContext())},e.id))},e.id))})]}),s()>1?(0,t.jsxs)("div",{css:[F.rcss.display.flex,F.rcss.align.center,F.rcss.justify.spaceBetween],children:[(0,t.jsx)(ev.Button,{size:"small",onClick:()=>{o()},disabled:!u(),text:"Previous"}),(0,t.jsx)("div",{css:[F.rcss.display.flex,F.rcss.flex.growAndShrink(1),F.rcss.align.center,F.rcss.justify.center],children:(0,t.jsxs)("div",{children:["Page"," ",(0,t.jsxs)("strong",{children:[n().pagination.pageIndex+1," of ",s()]})]})}),(0,t.jsx)(ev.Button,{size:"small",onClick:()=>{d()},disabled:!c(),text:"Next"})]}):null]})};var eL=e.i(338657),eD=e.i(37048),eP=e.i(180617);let e$=e=>{let{output:r}=e,a="json"in r&&r.json?(0,t.jsx)(R.default,{json:r.json}):null;if("CluiErrorOutput"===r.__typename)return(0,t.jsxs)(eD.VStack,{wrap:"nowrap",spacing:1,align:"stretch",children:[(0,t.jsxs)(eD.HStack,{spacing:1,children:[(0,t.jsx)(eL.default,{error:!0}),(0,t.jsx)("div",{children:r.error})]}),a]});if("CluiSuccessOutput"===r.__typename)return(0,t.jsxs)(eD.VStack,{wrap:"nowrap",spacing:1,align:"stretch",children:[(0,t.jsxs)(eD.HStack,{spacing:1,children:[(0,t.jsx)(eL.default,{success:!0}),(0,t.jsx)("div",{children:r.message})]}),a]});if("CluiMarkdownOutput"===r.__typename)return(0,t.jsx)(eP.default,{children:r.markdown});if("CluiTableOutput"===r.__typename)return(0,t.jsx)(eA,{columns:r.columns,rows:r.rows});if("CluiComponentOutput"===r.__typename){let e=e_[r.component];return e?(0,t.jsx)(e,{data:r.props}):(0,t.jsxs)(eD.HStack,{spacing:1,children:[(0,t.jsx)(eL.default,{}),(0,t.jsxs)("div",{children:["No component found for $",r.component]})]})}return(0,t.jsxs)(eD.HStack,{spacing:1,children:[(0,t.jsx)(eL.default,{}),(0,t.jsx)("div",{children:"no output"})]})},eO=e=>{let[a,i]=(0,r.useState)(null),l=(0,x.useApolloClient)(),n=(0,r.useMemo)(()=>(0,j.parseArgs)({args:a||e.args||{},command:e.command}),[e.args,e.command,a]),[s,{data:o,loading:u,error:d,called:c}]=(0,f.useMutation)(e.doc,{fetchPolicy:"no-cache"});return((0,r.useEffect)(()=>{c||n.missing.required||n.missing.optional&&!a||s({variables:n.variables}).then(async()=>{e.command.path.some(e=>"impersonate"===e)&&await (0,b.signOut)(l)})},[o,d,n,c,s,a,l,e.command.path]),d)?(0,t.jsx)(v.default,{error:d}):o?(0,t.jsx)(e$,{output:e.toOutput(o)}):n.missing.optional||n.missing.required||u?(0,t.jsx)(y.default,{isLoading:u,command:e.command,parsedVariables:n.variables,onSubmit:i}):null};e.s(["default",0,eO],477743);let eB=e=>{let[a,i]=(0,r.useState)(null),l=(0,r.useMemo)(()=>(0,j.parseArgs)({args:a||e.args||{},command:e.command}),[e.args,e.command,a]),[n,{data:s,loading:o,error:u,called:d}]=(0,et.useLazyQuery)(e.doc,{fetchPolicy:"network-only",ssr:!1});return((0,r.useEffect)(()=>{d||l.missing.required||!a&&l.missing.optional||n({variables:l.variables})},[l,n,d,a]),u)?(0,t.jsx)(v.default,{error:u}):s?(0,t.jsx)(e$,{output:e.toOutput(s)}):l.missing.optional||l.missing.required||o?(0,t.jsx)(y.default,{isLoading:o,command:e.command,parsedVariables:l.variables,onSubmit:i}):null};e.s(["default",0,eB],859194);var eV=e.i(228759);function eM({onRemove:e,children:r}){return(0,t.jsxs)(Q.View,{gap:8,children:[(0,t.jsx)(Q.View,{align:"end",children:(0,t.jsx)(N.IconButton,{onClick:e,alt:"Remove",children:(0,t.jsx)(k.default,{})})}),(0,t.jsx)(M.ShadesSurface,{clsx:eV.default.surfcae,p:16,children:r})]})}var eF=e.i(2001),eN=e.i(415541),eq=e.i(709485),ez=e.i(678852),eG=e.i(141738);let eQ={admin:(0,t.jsx)(d.default,{}),staff:(0,t.jsx)(o.default,{}),account:(0,t.jsx)(c.default,{}),team:(0,t.jsx)(g.default,{}),extension:(0,t.jsx)(n.default,{}),moderator:(0,t.jsx)(s.default,{}),trash:(0,t.jsx)(m.default,{}),org:(0,t.jsx)(g.default,{}),bpo:(0,t.jsx)(g.default,{})},eW=(e,t)=>{let r=e;for(let e of t){if(null==r||"object"!=typeof r)return;r=r[e]}return r};e.s(["CluiIconMap",0,eQ,"default",0,e=>{let[n,s]=(0,r.useState)([]);(0,r.useEffect)(()=>{n.length>0||window.scrollTo({top:0,left:0})},[n]);let o=(0,r.useCallback)(()=>{s([])},[]);(0,r.useEffect)(()=>{s([])},[e.value]);let d=function(e){let{data:n}=(0,i.useCurrentUserCluiQuery)({ssr:!1});return(0,r.useMemo)(()=>{let r;if(!n?.currentUser)return null;let i=JSON.parse(JSON.stringify(n.currentUser.clui));(0,h.forEach)(i,({command:e})=>{let t=e.path?.[e.path.length-1];e.path&&2===e.path.length&&t&&eQ[t]&&(e.icon=eQ[t])});let s=i.commands||{},o=(r=0,function({searchQuery:e,data:t,active:a,path:i}){if("group"===t.type)return null;let l=[];for(let e=1;e<i.length-1;e++){let t=i[e];"group"!==t.data.type&&l.push(t.data.label)}if(a&&(r=l.length),!e)return a?{score:1}:null;let n=e.replace(/^\s+/,"");if(!n)return a?{score:1}:null;let s=n.split(/\s+/),o=n.endsWith(" ");if(1===s.length&&!o){let e=eF.default.match(s[0],t.label);return e?{score:e.score,render:{ranges:e.ranges}}:null}let u=s.filter(Boolean),d=o?u:u.slice(0,-1),c=o?"":u[u.length-1],p=l.slice(r);if(a||d.length>p.length)return null;for(let e=0;e<d.length;e++)if(d[e]!==p[e])return null;if(!c)return d.length===p.length?{score:1}:null;let m=eF.default.match(c,t.label);return m?{score:m.score,render:{ranges:m.ranges}}:null}),u=function e(r,i){return Object.entries(r).map(([r,n])=>{let s=n.path&&2===n.path.length&&eQ[r]?eQ[r]:(0,t.jsx)(l.default,{}),o=n.description||"";if(n.commands&&Object.keys(n.commands).length>0){let t=e(n.commands,i);return{data:{type:"context",icon:s,label:r,description:o},match:i,commands:()=>t}}if("CluiOutput"===n.outputType){let e=n.query?eB:eO,l=n.query||n.mutation;if(l){let u=null,d=n.path;return{data:{type:"output",icon:s,label:r,description:o,renderOutput:()=>(u||(u=(0,a.parse)(l)),(0,t.jsx)(e,{command:n,doc:u,toOutput:e=>eW(e,d)}))},match:i}}return{data:{type:"output",icon:s,label:r,description:o},match:i}}return{data:{type:"action",icon:s,label:r,description:o,run:()=>{}},match:i}})}(s,o),d={data:{type:"action",icon:(0,t.jsx)(p.default,{}),label:"clear",description:"Clears screen",run:()=>{(0,eN.track)(eq.events.CLUI_COMMAND_SUBMITTED,{commandPath:"clear",commandType:"action"}),e()}},match:o};return{data:{type:"context",icon:(0,t.jsx)(l.default,{}),label:"CLUI",description:"Run a command"},commands:()=>[...u,d]}},[n,e])}(o),c=(0,r.useMemo)(()=>{if(!d)return null;if(!e.value)return{command:d};let t=function(e,t){if(!t)return[e];let r=t.trim().split(/\s+/),a=[e],i=e;for(let e of r){if(!i.commands)break;let t=i.commands({searchQuery:"",path:a,active:!0});if(t instanceof Promise)break;let r=t.find(t=>"group"!==t.data.type&&t.data.label===e);if(!r||"context"!==r.data.type)break;a.push(r),i=r}return a}(d,e.value);return{command:t.length>1?t:d}},[d,e.value]),m=(0,r.useCallback)(e=>{var r;if(!("output"===(r=e.data).type&&"renderOutput"in r))return;let a=e.path.slice(1).map(e=>"group"===e.data.type?e.data.key:e.data.label).filter(Boolean).join(" ");(0,eN.track)(eq.events.CLUI_COMMAND_SUBMITTED,{commandPath:a,commandType:"output"});let i=e.data.renderOutput(),l=Math.random().toString()+n.length,o=(0,t.jsx)(eM,{onRemove:()=>{s(e=>e.filter(e=>e.key!==l))},children:i},l);s(e=>[{key:l,node:o},...e])},[n.length]),g=(0,r.useRef)(null),x=(0,r.useRef)(n.length);(0,r.useEffect)(()=>{c&&x.current>0&&0===n.length&&g.current?.(),x.current=n.length},[c,n.length]);let f=(0,r.useRef)(!1);return(0,r.useEffect)(()=>{c&&!f.current&&(f.current=!0,g.current?.())},[c]),(0,t.jsx)("div",{className:eG.default.root,children:c?(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)(ez.CommandBar,{command:c.command,onSelect:m,focusRef:g,fullWidth:!0},e.value||""),(0,t.jsx)("div",{className:eG.default.output,children:n.map(e=>e.node)})]}):(0,t.jsx)("div",{className:eG.default.loading,children:(0,t.jsx)(u.default,{})})})},"getPath",0,eW],339487)},97678,e=>{e.v({root:"index-module__MurT_W__root"})},65910,e=>{e.v({iconLink:"InstallOnReplitFooter-module___Z-8zG__iconLink",textLink:"InstallOnReplitFooter-module___Z-8zG__textLink"})},132069,e=>{e.v({buttonLink:"NavItem-module__obNSla__buttonLink",centered:"NavItem-module__obNSla__centered"})},576592,789987,186894,111377,e=>{"use strict";var t=e.i(276385),r=e.i(389959),a=e.i(151027),i=e.i(295621),l=e.i(488081),n=e.i(895897),s=e.i(195206),o=e.i(339487),u=e.i(384001),d=e.i(190927),c=e.i(477743),p=e.i(859194),m=e.i(61732);function g({command:e}){let a=e.query??e.mutation,i=(0,r.useMemo)(()=>a?(0,d.parse)(a):null,[a]);if(!i)return null;let l=e.query?p.default:c.default;return(0,t.jsx)(m.View,{p:8,gap:16,children:(0,t.jsx)(l,{command:e,doc:i,toOutput:t=>(0,o.getPath)(t,e.path)})})}function h(e){return(0,r.useMemo)(()=>({data:{type:"context",icon:(0,t.jsx)(s.default,{}),label:"Commands"},commands:()=>e?.commands?Object.entries(e.commands).map(([e,r])=>(function e(r,a,i){let l=0===i?o.CluiIconMap[r]??(0,t.jsx)(s.default,{}):(0,t.jsx)(s.default,{});return void 0!==a.commands&&Object.keys(a.commands).length>0?{match:u.matchLabel,data:{type:"context",label:r,description:a.description??"",icon:l},commands:t=>t.active||t.searchQuery?Object.entries(a.commands??{}).map(([t,r])=>e(t,r,i+1)):[]}:{match:u.matchLabel,data:{type:"context",label:r,description:a.description??"",icon:l,view:(0,t.jsx)(g,{command:a})},commands:()=>[]}})(e,r,0)):[]}),[e])}var x=e.i(407617),f=e.i(735362);function j(){let e=(0,l.useRouter)();return(0,r.useMemo)(()=>({data:{type:"context",icon:(0,t.jsx)(t.Fragment,{}),label:"Staff"},commands:()=>[{match:u.matchLabel,data:{type:"action",icon:(0,t.jsx)(f.default,{}),label:"Run Evaluations",description:"Open the evaluations page to batch test Agent",run:()=>{e.push("/evaluations")}}}]}),[e])}var b=e.i(345836),v=e.i(921125);function y(){let e=(0,l.useRouter)();return(0,r.useCallback)(t=>{let{href:r,as:a}=(0,v.replLinkProps)(t);e.push(r,a)},[e])}var R=e.i(678852),w=e.i(97678);function C(){let e=function(){let{data:e}=(0,n.useGlobalPersonalRecentReplsQuery)({variables:{count:b.RECENT_REPLS_SIDEBAR_MENU_COUNT},fetchPolicy:"cache-and-network",ssr:!1}),a=e?.recentRepls,[i]=(0,n.useGlobalPersonalSearchLazyQuery)(),l=y(),s=(0,r.useMemo)(()=>a?.length?{data:{type:"context",label:"Recent",icon:(0,t.jsx)(t.Fragment,{})},commands:e=>e.searchQuery?[]:a.map(t=>(0,x.toReplResult)(e.searchQuery,t,l))}:null,[a,l]),o=j(),u=e?.currentUser?.isStaff,d=h(e?.currentUser?.clui),c=(0,r.useMemo)(()=>({data:{type:"group",key:"search"},commands:async e=>{if(""===e.searchQuery.trim())return[];let t=await i({variables:{search:e.searchQuery}}),r=t.data?.currentUser?.replSearch;return r?r.map(t=>(0,x.toReplResult)(e.searchQuery,t,l)):[]}}),[i,l]);return(0,r.useMemo)(()=>({data:{type:"context",label:"Search Apps",description:"Search Apps",icon:(0,t.jsx)(t.Fragment,{})},commands:()=>[...s?[s]:[],c,d,...u?[o]:[]]}),[s,c,d,u,o])}();return(0,t.jsx)(R.CommandBar,{autoFocus:!0,command:e})}function S({orgId:e}){let a=function(e){let{data:a}=(0,n.useGlobalOrgRecentReplsQuery)({variables:{orgId:e,count:b.RECENT_REPLS_SIDEBAR_MENU_COUNT},fetchPolicy:"cache-and-network",ssr:!1}),i=a?.currentUser?.org.__typename==="Org"?a.currentUser.org:null,l=i?.recentRepls.items,s=i?.name,o=a?.currentUser?.isStaff,[u]=(0,n.useGlobalOrgSearchLazyQuery)(),d=y(),c=j(),p=h(a?.currentUser?.clui),m=(0,r.useMemo)(()=>({data:{type:"group",key:"search"},commands:async t=>{if(""===t.searchQuery.trim())return[];let r=await u({variables:{orgId:e,replsInput:{filters:{title:{search:t.searchQuery}}}}}),a=r.data?.currentUser?.org.__typename==="Org"?r.data.currentUser.org:null,i=a?.repls.__typename==="ReplConnection"?a.repls.items:null;return i?i.map(e=>(0,x.toReplResult)(t.searchQuery,e,d)):[]}}),[e,u,d]),g=(0,r.useMemo)(()=>l?.length?{data:{type:"context",label:"Recent",icon:(0,t.jsx)(t.Fragment,{})},commands:e=>e.searchQuery?[]:l.map(t=>(0,x.toReplResult)(e.searchQuery,t,d))}:null,[l,d]);return(0,r.useMemo)(()=>({data:{type:"context",label:"Search Apps",description:"Search Apps"+(s?` in ${s}`:""),icon:(0,t.jsx)(t.Fragment,{})},commands:()=>[...g?[g]:[],m,p,...o?[c]:[]]}),[g,m,p,s,o,c])}(e);return(0,t.jsx)(R.CommandBar,{autoFocus:!0,command:a})}let T=(0,i.defaultKeyCombo)({cmdOrCtrl:!0,key:"k"});e.s(["GlobalSearch",0,function(){let{orgId:e}=(0,a.useCurrentUserStoredOrgContext)();return(0,t.jsx)(m.View,{clsx:w.default.root,children:e?(0,t.jsx)(S,{orgId:e}):(0,t.jsx)(C,{})})},"useGloablSearchState",0,function(){var e;let[t,a]=(0,r.useState)(!1);return e=(0,r.useCallback)(()=>a(e=>!e),[]),(0,r.useEffect)(()=>{let t=t=>{(0,i.getKeyCombination)(t)===T&&e()};return document.addEventListener("keydown",t),()=>{document.removeEventListener("keydown",t)}},[e]),[t,a]}],576592);var k=e.i(413974),I=e.i(256758),_=e.i(8047),E=e.i(513891),U=e.i(813707),A=e.i(489859),L=e.i(86145),D=e.i(488299),P=e.i(773222),$=e.i(798142);let O="perf-tools-lag-radar",B="perf-tools-fps-counter",V="analyticsInspector",M=(0,E.default)(()=>e.A(422935),{loadableGenerated:{modules:[198581]}}),F=(0,E.default)(()=>e.A(528701),{loadableGenerated:{modules:[576553]}}),N=()=>{let[e,a]=(0,r.useState)(!1),[i,l]=(0,r.useState)(!!A.default.get(O,"boolean")),[n,s]=(0,r.useState)(!!A.default.get(B,"boolean")),[o,u]=(0,r.useState)(!!A.default.get(V,"boolean"));return(0,r.useEffect)(()=>{A.default.set(O,i)},[i]),(0,r.useEffect)(()=>{A.default.set(B,n)},[n]),(0,r.useEffect)(()=>{A.default.set(V,o),window.dispatchEvent(new StorageEvent("storage",{key:V,newValue:String(o)}))},[o]),(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)(P.PopoverTrigger,{label:"Performance",isOpen:e,onOpenChange:a,children:[(0,t.jsx)(D.IconButton,{alt:"Performance",size:28,tooltipPlacement:"left-start",children:(0,t.jsx)(U.default,{})}),(0,t.jsxs)(m.View,{gap:4,p:8,children:[(0,t.jsxs)(m.View,{row:!0,gap:8,children:[(0,t.jsx)(L.Checkbox,{id:"lag-radar",name:"Lag Radar",checked:i,onChange:e=>{l(e)}}),(0,t.jsx)("label",{htmlFor:"lag-radar",children:"Lag Radar"})]}),(0,t.jsxs)(m.View,{row:!0,gap:8,children:[(0,t.jsx)(L.Checkbox,{id:"fps-counter",name:"FPS Counter",checked:n,onChange:e=>{s(e)}}),(0,t.jsx)("label",{htmlFor:"fps-counter",children:"FPS Counter"})]}),(0,t.jsxs)(m.View,{row:!0,gap:8,children:[(0,t.jsx)(L.Checkbox,{id:"analytics-inspector",name:"Analytics Inspector",checked:o,onChange:e=>{u(e)}}),(0,t.jsx)("label",{htmlFor:"analytics-inspector",children:"Analytics Inspector"})]})]})]}),i?(0,t.jsx)($.Portal,{children:(0,t.jsx)("div",{style:{position:"fixed",top:0,right:0,zIndex:Number.MAX_SAFE_INTEGER,pointerEvents:"none"},children:(0,t.jsx)(M,{})})}):void 0,n?(0,t.jsx)($.Portal,{children:(0,t.jsx)(F,{})}):void 0]})};var q=e.i(65910);e.s(["InstallOnReplitFooter",0,function({isStaffplorer:e}){return(0,t.jsxs)(m.View,{justify:"space-between",row:!0,pl:4,children:[(0,t.jsxs)(m.View,{row:!0,gap:2,align:"center",children:[(0,t.jsx)(_.Text,{color:"dimmest",variant:"small",children:"Install Replit on"}),(0,t.jsx)(k.default,{href:"/mobile",target:"_blank",clsx:q.default.iconLink,children:(0,t.jsx)(I.default,{})}),(0,t.jsxs)(m.View,{row:!0,gap:2,align:"center",children:[(0,t.jsx)(m.View,{px:2,children:(0,t.jsx)(_.Text,{color:"dimmest",variant:"small",children:"•"})}),(0,t.jsx)(k.default,{href:"https://docs.replit.com/updates",target:"_blank",clsx:q.default.textLink,children:"Changelog"})]})]}),(0,t.jsx)(m.View,{pl:8,children:e?(0,t.jsx)(N,{}):void 0})]})}],789987);var z=e.i(415541),G=e.i(709485),Q=e.i(419635),W=e.i(244945),H=e.i(132069);e.s(["NavItem",0,function(e){let r=(0,l.useRouter)(),i="function"==typeof e.active?e.active(r):e.active??!1,n=(0,a.getOrgTrackingContext)(e.orgId?{id:e.orgId}:void 0),s=e.disabled??!1,o=(0,t.jsx)(Q.ButtonLink,{clsx:[H.default.buttonLink,{[H.default.centered]:e.centered}],disabled:s,variant:e.variant??(i?void 0:"nofill"),onClick:t=>{var r;s?t.preventDefault():(e.onClick?.(t),r=e.label,(0,z.track)(G.events.NAV_ITEM_CLICK,{target:r,source:"sidebar",isWorkspace:!1,context:n}))},onMouseEnter:e.onMouseEnter,"aria-current":i?"page":void 0,"data-cy":e.dataCy,tabIndex:0,href:e.href,as:e.as,iconLeft:e.icon,text:e.label,iconRight:e.tag?(0,t.jsx)(m.View,{children:e.tag}):void 0});return(0,t.jsx)(m.View,{tag:"li",justify:"space-between",row:!0,grow:!0,shrink:!0,children:s&&e.disabledTooltipText?(0,t.jsx)(W.Tooltip,{tooltip:e.disabledTooltipText,placement:"right",children:(e,r)=>(0,t.jsx)("div",{ref:r,...e,style:{pointerEvents:"auto",flexGrow:1,flexShrink:1,minWidth:0},children:(0,t.jsx)("div",{style:{pointerEvents:"none"},children:o})})}):o})}],186894);var Y=e.i(360118),K=e.i(914359),Z=e.i(643484);e.s(["SidebarReferralButton",0,()=>{let[e,a]=(0,r.useState)(!1);return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)(Z.Button,{variant:"outlined",size:"small",iconLeft:(0,t.jsx)(Y.default,{}),text:"Refer & Earn",onClick:()=>{a(!0),(0,z.track)(G.events.NAV_ITEM_CLICK,{target:"referral_link",source:"sidebar",isWorkspace:!1,context:"personal"})},stretch:!0,dataCy:"sidebar-referral-btn"}),(0,t.jsx)(K.ReferralLinkModal,{isOpen:e,onClose:()=>a(!1),trackingContext:"sidebar"})]})}],111377)},76298,e=>{e.v({pill:"navItems-module__vGHY-a__pill"})},477814,e=>{"use strict";var t=e.i(276385),r=e.i(182409),a=e.i(953436),i=e.i(943172),l=e.i(761201);let n={self:e.i(76298).default.pill},s={as:"/~",href:"/home",label:"Home",icon:(0,t.jsx)(a.default,{})},o={as:"/repls",href:"/replsDashboard",label:`My ${l.REPL_DISPLAY_NAME.plural}`,icon:(0,t.jsx)(i.default,{})},u={as:"/my-published-apps",href:"/hostingDeployments",label:`Published ${l.REPL_DISPLAY_NAME.pluralLower}`,icon:(0,t.jsx)(r.default,{})};e.s(["deploymentsItem",0,u,"homeItem",0,s,"navItemPillCss",0,n,"replsItem",0,o])},349525,e=>{e.v({content:"index-module__SJkCTa__content",footer:"index-module__SJkCTa__footer",header:"index-module__SJkCTa__header",hideWhenCollapsed:"index-module__SJkCTa__hideWhenCollapsed",isOpen:"index-module__SJkCTa__isOpen",planUsageMonitor:"index-module__SJkCTa__planUsageMonitor",root:"index-module__SJkCTa__root"})},330971,717595,e=>{"use strict";var t=e.i(276385),r=e.i(488081),a=e.i(389959),i=e.i(14154),l=e.i(923242),n=e.i(917255),s=e.i(965097),o=e.i(40916),u=e.i(346781),d=e.i(255701),c=e.i(357253),p=e.i(76112),m=e.i(394572),g=e.i(908628),h=e.i(749556),x=e.i(334028),f=e.i(612343),j=e.i(761201),b=e.i(765826),v=e.i(681650),y=e.i(445807),R=e.i(897395),w=e.i(151027),C=e.i(908796),S=e.i(410458),T=e.i(730497),k=e.i(856010),I=e.i(776065),_=e.i(415541),E=e.i(709485),U=e.i(378371),A=e.i(926233),L=e.i(33602),D=e.i(448942),P=e.i(416004),$=e.i(289038),O=e.i(276887),B=e.i(63811),V=e.i(127384),M=e.i(576592),F=e.i(789987),N=e.i(186894),q=e.i(765269),z=e.i(345836),G=e.i(111377),Q=e.i(953436),W=e.i(61935),H=e.i(943172),Y=e.i(744006),K=e.i(477814);let Z=e=>t=>t.pathname===e;function J(e,r,a=!1){let{sidebarItems:{homeItem:i,replsItem:l,deploymentsItem:n,usageItem:s,connectorsItem:o}}=function({org:e,isSubscribed:r=!1}={}){var a;let i,l,n,s=e?(0,D.orgLinks)({slug:e.slug}):void 0,o=(0,T.useFlag)({controlName:"flag-free-plan",default:!1}),u=o&&!r&&!e,d=(a=e?.id,n=!(l=(0,y.useUsageActionRequired)(a)).loading&&l.actionRequired,{as:"/usage",href:"/usage",label:"Usage",icon:(0,t.jsx)(p.default,{}),tag:n?(0,t.jsx)(Y.Pill,{clsx:K.navItemPillCss.self,text:"Action required",colorway:"yellow"}):void 0}),c=s?{...s.home,label:"Home",icon:(0,t.jsx)(Q.default,{})}:K.homeItem,m=s?{...s.repls,icon:(0,t.jsx)(H.default,{}),label:j.REPL_DISPLAY_NAME.plural}:{href:"/replsDashboard",as:"/repls",label:`My ${j.REPL_DISPLAY_NAME.plural}`,icon:(0,t.jsx)(H.default,{}),routerPath:"/replsDashboard",active:e=>"/replsDashboard"===e.pathname},g=`Published ${j.REPL_DISPLAY_NAME.plural}`,h=s?{...K.deploymentsItem,...s.deployments,label:g}:{...K.deploymentsItem,label:g};return!o||r||e?s?i={...s.connectors,icon:(0,t.jsx)(W.default,{}),label:"Integrations"}:s||(i={href:"/integrations",as:"/integrations",label:"Integrations",icon:(0,t.jsx)(W.default,{}),routerPath:"/integrations"}):i=void 0,{sidebarItems:{homeItem:c,replsItem:m,deploymentsItem:h,usageItem:u?void 0:d,connectorsItem:i}}}({org:e,isSubscribed:a});return{home:{...i,active:i.routerPath?Z(i.routerPath):Z(i.href.toString())},repls:{...l,active:!!l.routerPath&&Z(l.routerPath)},deployments:n?{...n,active:n.routerPath?Z(n.routerPath):Z(n.href.toString())}:void 0,connectors:o?{...o,active:o.routerPath?Z(o.routerPath):Z(o.href.toString())}:void 0,usage:r&&s?{...s,active:Z(s.href.toString())}:void 0}}var X=e.i(547523);function ee(e){return!!(0,X.useBreakpoint)("tabletMin")||e}e.s(["useSidebarOpenState",0,ee],717595);var et=e.i(480028),er=e.i(919073),ea=e.i(643484),ei=e.i(488299),el=e.i(528326),en=e.i(8047),es=e.i(61732),eo=e.i(121668),eu=e.i(349525);let ed=(0,et.cvarsFrom)("index.module.css",["--sidebar-width","--content-width","--sidebar-z-index","--header-height","--border-color"]);function ec({orgSlug:e}){let r=(0,$.useOrgGroupNavItems)({orgSlug:e});return(0,t.jsx)(es.View,{tag:"ul",gap:2,children:r.map(e=>(0,t.jsx)(N.NavItem,{...e,active:e.active??!1},`nav-item-${e.label}`))})}let ep=({currentOrg:e,isUsingLegacyPersonalContext:a,isSubscribed:i=!1,isUnifiedPlansEnabled:n=!1})=>{let{home:s,repls:u,deployments:c,usage:p,connectors:g}=J(e,a,i),h=(0,B.usePrefetchFolderList)(),x=(0,r.useRouter)(),b=(0,w.useIsCurrentOrgEnterprise)(),{disableImport:v,disableIntegrations:y}=(0,S.default)(e?.id),R="Disabled by your enterprise admin",C=n&&b&&e?.authorizations.viewOrgAnalytics?.isAuthorized,T=e?(0,D.orgLinks)({slug:e.slug}).analytics:void 0,k=e?(0,D.orgLinks)({slug:e.slug}).groups:void 0;return(0,t.jsxs)(es.View,{gap:16,children:[(0,t.jsxs)(es.View,{gap:8,children:[(0,t.jsx)(N.NavItem,{active:!1,icon:(0,t.jsx)(o.default,{}),centered:!0,label:"Create something new",dataCy:"sidebar-new-repl-btn",variant:"outlined",href:{pathname:e?`/t/${e.slug}`:"/home",query:{create:!0}},as:e?`/t/${e.slug}`:"/~",onClick:()=>{(0,_.track)(E.events.OPEN_REPL_CREATION_PAGE,{source:"global sidebar",context:(0,w.getOrgTrackingContext)(e)})}}),(0,t.jsx)(N.NavItem,{active:!1,icon:(0,t.jsx)(m.default,{}),centered:!0,label:"Import code or design",dataCy:"sidebar-import-btn",variant:"outlined",disabled:v,disabledTooltipText:R,href:{pathname:"/import"},as:"/import",onClick:()=>{(0,_.track)(E.events.OPEN_IMPORT_PAGE,{source:"global sidebar",href:window.location.href,context:(0,w.getOrgTrackingContext)(e)})}})]}),(0,t.jsxs)(es.View,{tag:"ul","aria-label":"Pages",gap:2,children:[(0,t.jsx)(N.NavItem,{...s,active:s.active??!1}),(0,t.jsxs)(z.RecentReplsPopover,{children:[(e,r)=>(0,t.jsx)(es.View,{grow:!0,shrink:!0,innerRef:r,...e,children:(0,t.jsx)(N.NavItem,{...u,active:u.active??!1,label:j.REPL_DISPLAY_NAME.plural,onMouseEnter:()=>h(),disableTooltip:!0})}),e?(0,t.jsx)(z.OrgSidebarRecentRepls,{orgId:e.id}):(0,t.jsx)(z.SidebarRecentRepls,{})]}),c?(0,t.jsx)(N.NavItem,{...c,active:c.active??!1}):null,g?(0,t.jsx)(N.NavItem,{...g,active:g.active??!1,disabled:y,disabledTooltipText:R}):null,p&&!n?(0,t.jsx)(N.NavItem,{...p,active:p.active??!1}):null,n&&b&&k?(0,t.jsx)(N.NavItem,{...k,label:"Groups",icon:(0,t.jsx)(f.default,{}),active:eg(k.routerPath)}):null,C&&T?(0,t.jsx)(N.NavItem,{...T,label:"Analytics",icon:(0,t.jsx)(l.default,{}),active:eg(T.routerPath)}):null,n?(0,t.jsx)(N.NavItem,{label:"Settings",icon:(0,t.jsx)(d.default,{}),active:!1,href:"#",onClick:e=>{e.preventDefault(),(0,I.updatePathWithQueryParams)({router:x,params:[{mode:"add",key:A.SETTINGS_SHOW_PARAM,value:"true"}]})}}):null]})]})},em=({currentOrg:e,isUsingLegacyPersonalContext:r})=>{let[i,l]=(0,a.useState)(!1),{home:n,repls:s}=J(e,r);return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)(es.View,{gap:6,children:[(0,t.jsx)(ea.Button,{variant:"outlined",colorway:"primary",text:"Request a Member Seat",onClick:()=>l(!0),iconLeft:(0,t.jsx)(h.default,{})}),(0,t.jsxs)(es.View,{tag:"ul","aria-label":"Pages",gap:2,children:[(0,t.jsx)(N.NavItem,{...n,active:n.active??!1}),(0,t.jsx)(N.NavItem,{...s,active:s.active??!1,label:`All ${j.REPL_DISPLAY_NAME.plural}`})]})]}),(0,t.jsx)(P.default,{isOpen:i,orgId:e?.id,orgName:e?.name,onClose:()=>l(!1),onSuccess:()=>l(!1)})]})},eg=e=>t=>t.pathname===e,eh=({org:e})=>{let{slug:r}=e,a=(0,D.orgLinks)({slug:r}),i=e.authorizations.viewUsage.isAuthorized&&e.authorizations.viewSubscription.isAuthorized,n=e.authorizations.viewOrgAnalytics?.isAuthorized,s=e.authorizations.viewOrgSecurity?.isAuthorized;return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)(es.View,{p:6,children:(0,t.jsx)(en.Text,{variant:"small",color:"dimmest",height:"singleLine",children:"Manage Organization"})}),(0,t.jsxs)(es.View,{tag:"ul","aria-label":"Manage Workspace",gap:2,children:[(0,t.jsx)(N.NavItem,{...a.members,label:"Members",icon:(0,t.jsx)(x.default,{}),active:eg(a.members.routerPath)}),(0,t.jsx)(N.NavItem,{...a.groups,label:"Groups",icon:(0,t.jsx)(f.default,{}),active:eg(a.groups.routerPath)}),i?(0,t.jsx)(ex,{...a.usage,orgId:e.id,active:eg(a.usage.routerPath)}):null,n?(0,t.jsx)(N.NavItem,{...a.analytics,label:"Analytics",icon:(0,t.jsx)(l.default,{}),active:eg(a.analytics.routerPath)}):null,s?(0,t.jsx)(N.NavItem,{...a.security,label:"Security",icon:(0,t.jsx)(c.default,{}),active:eg(a.security.routerPath)}):null,(0,t.jsx)(N.NavItem,{...a.profile,label:"Profile",icon:(0,t.jsx)(g.default,{}),active:eg(a.profile.routerPath)}),(0,t.jsx)(N.NavItem,{...a.settings,label:"Settings",icon:(0,t.jsx)(d.default,{}),active:e=>e.pathname===a.settings.routerPath||e.pathname===`${a.settings.routerPath}/[[...tab]]`})]})]})},ex=e=>{let r=(0,y.useUsageActionRequired)(e.orgId),a=!r.loading&&r.actionRequired;return(0,t.jsx)(N.NavItem,{...e,icon:(0,t.jsx)(p.default,{}),tag:a?(0,t.jsx)(Y.Pill,{text:"Action required",colorway:"yellow"}):void 0,label:"Usage"})};function ef(e){let[r,a]=(0,M.useGloablSearchState)();return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)(ei.IconButton,{...e,alt:"Search",size:28,onClick:()=>a(!0),children:(0,t.jsx)(u.default,{})}),(0,t.jsx)(el.Modal,{noPadding:!0,hideCloseButton:!0,isOpen:r,onRequestClose:()=>a(!1),children:(0,t.jsx)(M.GlobalSearch,{})})]})}e.s(["EXPANDED_SIDEBAR_WIDTH",0,240,"Sidebar",0,function(e){let a,l,o,u=(0,r.useRouter)(),d=ee(e.isOpen),c=e.isOpen?240:42,p={[ed.sidebarWidth]:c+"px",[ed.contentWidth]:"240px",[ed.sidebarZIndex]:V.SIDEBAR_Z_INDEX.toString(),[ed.headerHeight]:V.APP_HEADER_HEIGHT+"px"},{currentUser:m}=e,{orgId:g,orgRole:h}=(0,w.useCurrentUserStoredOrgContext)(),x=void 0===g,f=!m.isSubscribed&&x,j=!g&&m.isSubscribed,y=h===C.SystemOrgGroupType.SystemViewers,{data:S,loading:A}=(0,i.useLayoutSidebarGetOrgQuery)({variables:{orgId:g??""},skip:!g}),D=S?.getOrg?.__typename==="Org"?S.getOrg:void 0,P=!!g&&A,$=(0,T.useFlag)({controlName:b.REFERRAL_PROMO_FEATURE_FLAG}),B=!!(m.isSubscribed&&!m.userSubscription?.isTrial),M=(0,v.getPromoProgramConfig)(B),z=(0,k.useIsUnifiedPlanEnabled)(x?{currentUser:m}:{org:D}),Q=(0,k.useIsUnifiedPlanEnabledForAnyOrg)(m),W="CurrentUserOrganizationConnection"===m.orgs.__typename&&m.orgs.items.some(e=>(0,O.isEnterpriseOrg)(e.org.dealContext));return D?(a=D.name,l=D.image,o=D.id):(P?(a="",l=void 0):(a=m.firstName??m.username,l=m.image),o=void 0),(0,t.jsxs)(er.ShadesSurface,{border:{side:"right"},elevate:"1x",tag:"nav",clsx:[eu.default.root,{[eu.default.isOpen]:d}],style:p,children:[(0,t.jsx)(es.View,{clsx:eu.default.header,p:6,row:!0,gap:6,align:"center",justify:"end",children:(0,t.jsx)(ef,{})}),(0,t.jsxs)(es.View,{clsx:eu.default.content,px:6,grow:!0,shrink:!0,gap:16,children:[Q?(0,t.jsx)(es.View,{clsx:eu.default.hideWhenCollapsed,children:(0,t.jsx)(R.OwnerPill,{ownerName:a,image:l,currentOrgId:o,isNewDesignEnabled:Q,alignment:"start",stretch:!0})}):null,e.sidebarType===L.SidebarType.Index?(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)(t.Fragment,{children:y&&D?(0,t.jsx)(em,{currentOrg:D,isUsingLegacyPersonalContext:x}):(0,t.jsx)(ep,{currentOrg:D,isUsingLegacyPersonalContext:x,isSubscribed:m.isSubscribed,isUnifiedPlansEnabled:z})}),(0,t.jsx)(es.View,{clsx:eu.default.hideWhenCollapsed,children:z||x||!D?null:(0,t.jsx)(eh,{org:D})})]}):(0,t.jsx)(ec,{orgSlug:"string"==typeof u.query.orgSlug?u.query.orgSlug:D?.slug})]}),e.sidebarType===L.SidebarType.Index?(0,t.jsxs)(es.View,{p:12,gap:6,clsx:eu.default.footer,children:[!g&&$&&!W&&d?(0,t.jsx)(es.View,{pb:4,children:(0,t.jsx)(eo.PromoCard,{title:M.sidebarPill.title,label:M.sidebarPill.label,onClick:()=>{(0,_.track)(E.events.NAV_ITEM_CLICK,{target:M.sidebarPill.trackingTarget,source:"sidebar",isWorkspace:!1,context:"personal"}),(0,I.updatePathWithQueryParams)({router:u,params:[{mode:"add",key:U.REFERRAL_SHOW_PARAM,value:"true"}]})}})}):null,(0,t.jsxs)(es.View,{clsx:eu.default.hideWhenCollapsed,tag:"ul",gap:2,children:[(0,t.jsx)(N.NavItem,{href:"https://learn.replit.com/",label:"Learn",icon:(0,t.jsx)(s.default,{}),active:!1}),(0,t.jsx)(N.NavItem,{href:"https://docs.replit.com",label:"Documentation",icon:(0,t.jsx)(n.default,{}),active:!1})]}),(0,t.jsxs)(es.View,{clsx:eu.default.hideWhenCollapsed,gap:6,children:[f?(0,t.jsx)(es.View,{clsx:eu.default.planUsageMonitor,children:(0,t.jsx)(q.default,{})}):null,j?(0,t.jsx)(G.SidebarReferralButton,{}):null]}),(0,t.jsx)(es.View,{clsx:eu.default.hideWhenCollapsed,children:(0,t.jsx)(F.InstallOnReplitFooter,{isStaffplorer:m.isStaff&&m.isExplorer})})]}):null]})}],330971)}]);

//# debugId=80790123-f952-251c-2095-710ec5e4f415
//# sourceMappingURL=0c5b.p_-k4el6.js.map
