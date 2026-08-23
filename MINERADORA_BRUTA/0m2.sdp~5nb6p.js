;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="8d0314da-df6f-63ba-7c27-40377bed923a")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,875744,e=>{e.v({root:"RoleBadge-module__zj-yvq__root"})},389133,e=>{"use strict";var r=e.i(276385),t=e.i(712903),i=e.i(177037),s=e.i(596139),a=e.i(480028),l=e.i(744006),n=e.i(244945),o=e.i(875744);let c=({tagline:e,name:t,color:i,iconLeft:s})=>{let a=(0,r.jsx)(l.Pill,{text:t,colorway:i,iconLeft:s,clsx:o.default.root,variant:"muted",compact:!0});return e?(0,r.jsx)(n.Tooltip,{isDisabled:!e,tooltip:e,children:a}):a},u=()=>(0,r.jsx)(c,{name:s.corePlanName,color:"brand",iconLeft:(0,r.jsx)(t.default,{size:12,color:i.brandOrange})});e.s(["CoreBadge",0,u,"DefaultBadge",0,c,"RoleBadge",0,{Default:c,Admin:({tagline:e})=>(0,r.jsx)(c,{tagline:e??"Admin",name:"Admin",color:"yellow"}),Detective:({tagline:e})=>(0,r.jsx)(c,{tagline:e??"Detective",name:"Detective",color:"green"}),Featured:({tagline:e})=>(0,r.jsx)(c,{tagline:e??"Verified",name:"Verified",color:"blue"}),Hacker:({tagline:e})=>(0,r.jsx)(c,{tagline:e??`${s.hackerPlanName} users are subscribed to Replit's paid ${s.hackerPlanName} Plan.`,name:s.hackerPlanName,color:"green"}),Core:u,Pro:()=>(0,r.jsx)(c,{name:s.proPlanName,color:"blue",iconLeft:(0,r.jsx)(t.default,{size:12,color:a.tokens.blueStrongest})}),LanguageJammer:({tagline:e})=>(0,r.jsx)(c,{tagline:e??"Language Jammer",name:"Language Jammer",color:"purple"}),ReplitRep:({tagline:e})=>(0,r.jsx)(c,{tagline:e??"Replit Rep",name:"Replit Rep",color:"magenta"}),ReplitRepEdu:({tagline:e})=>(0,r.jsx)(c,{tagline:e??"Replit Rep EDU",name:"Replit Rep EDU",color:"green"}),Patron:({tagline:e})=>(0,r.jsx)(c,{tagline:e??"Patron",name:"Patron",color:"purple"}),Pythonista:({tagline:e})=>(0,r.jsx)(c,{tagline:e??"Pythonista",name:"Pythonista",color:"teal"})}])},449859,e=>{"use strict";var r,t=e.i(276385),i=e.i(389133),s=((r={}).Admin="ADMIN",r.Detective="DETECTIVE",r.Featured="FEATURED",r.LanguageJammer="LANGUAGE_JAMMER",r.Moderator="MODERATOR",r.ReplitRep="REPLIT_REP",r.ReplitRepEdu="REPLIT_REP_EDU",r.Patron="PATRON",r.Pythonista="PYTHONISTA",r.Student="STUDENT",r.Teacher="TEACHER",r.Hacker="hacker",r.HackerPro="hacker_pro",r.Pro="pro",r);e.s(["RUIUserRoles",()=>s,"UserRoleBadge",0,({userRole:e,tagline:r,name:s})=>{switch(e){case"DETECTIVE":return(0,t.jsx)(i.RoleBadge.Detective,{tagline:r});case"MODERATOR":return null;case"LANGUAGE_JAMMER":return(0,t.jsx)(i.RoleBadge.LanguageJammer,{tagline:r});case"FEATURED":return(0,t.jsx)(i.RoleBadge.Featured,{tagline:r});case"ADMIN":return(0,t.jsx)(i.RoleBadge.Admin,{tagline:r});case"REPLIT_REP":return(0,t.jsx)(i.RoleBadge.ReplitRep,{tagline:r});case"REPLIT_REP_EDU":return(0,t.jsx)(i.RoleBadge.ReplitRepEdu,{tagline:r});case"PATRON":return(0,t.jsx)(i.RoleBadge.Patron,{tagline:r});case"PYTHONISTA":return(0,t.jsx)(i.RoleBadge.Pythonista,{tagline:r});case"hacker":return(0,t.jsx)(i.RoleBadge.Hacker,{tagline:r});case"hacker_pro":return(0,t.jsx)(i.RoleBadge.Core,{});case"pro":return(0,t.jsx)(i.RoleBadge.Pro,{});default:return(0,t.jsx)(i.RoleBadge.Default,{tagline:r,name:s})}}])},21875,e=>{"use strict";var r=e.i(276385),t=e.i(871579),i=e.i(825419),s=e.i(488299),a=e.i(744006),l=e.i(8047),n=e.i(449859),o=e.i(61732);let c={[n.RUIUserRoles.Admin]:"Admin",[n.RUIUserRoles.Moderator]:"Community Moderator",[n.RUIUserRoles.Teacher]:"Teacher",[n.RUIUserRoles.Student]:"Student"};e.s(["User",0,function({src:e,username:n,email:u,fullName:d,displayName:p,small:g,role:m,localRole:x,plan:h,className:f,style:R}){return(0,r.jsxs)(o.View,{row:!0,gap:8,align:"center",shrink:!0,className:f,style:R,children:[(0,r.jsx)(i.Avatar,{src:e,username:n??u,fullName:d,size:g?24:32,layout:"intrinsic"}),(0,r.jsxs)(o.View,{grow:!0,shrink:!0,row:!0,gap:4,align:"center",children:[void 0!==p?(0,r.jsxs)(o.View,{className:"UserInfo",gap:4,children:[(0,r.jsx)(l.Text,{multiline:!1,children:p}),(0,r.jsxs)(l.Text,{variant:"small",color:"dimmest",multiline:!1,translate:"no",children:[n?`@${n}`:"",u?`${u}`:""]})]}):(0,r.jsx)(l.Text,{multiline:!1,translate:"no",children:n}),void 0!==h&&(0,r.jsx)(s.IconButton,{alt:"plan subscriber",colorway:"primary",children:(0,r.jsx)(t.default,{})}),void 0!==m&&(0,r.jsx)(a.Pill,{colorway:"primary",text:c[m]}),void 0!==x&&(0,r.jsx)(a.Pill,{text:x})]})]})}])},276887,e=>{"use strict";var r=e.i(908796),t=e.i(569910),i=e.i(596139);e.s(["convertToSalesLedPlanNameIfApplicable",0,function(e,t){if(e===`Replit ${i.replitTeamsPlanName}`){if(t?.dealType===r.OrgDealType.Enterprise)return(0,i.getEnterprisePlanDisplayName)(!1);if(t?.dealType===r.OrgDealType.EnterpriseTrial)return(0,i.getEnterprisePlanDisplayName)(!0);if(t?.dealType===r.OrgDealType.Trial)return`Replit ${i.replitTeamsPlanName} Trial`}return e},"getFormattedOrgWorkspaceName",0,({isInOrg:e,ownerName:r,maxNameLength:t=20})=>{if(!r)return"Personal Workspace";let i=r.trim();return i.length>t&&!e?"Personal Workspace":e?`${i} Workspace`:`${i}'s Workspace`},"isCappedPlan",0,function(e){return e===r.PlanId.CoreV3||e===r.PlanId.Pro},"isEnterpriseOrg",0,function(e){return e?.dealType===r.OrgDealType.Enterprise||e?.dealType===r.OrgDealType.EnterpriseTrial},"orgGroupToDisplayName",0,function(e){switch(e){case r.SystemOrgGroupType.SystemAdmins:return"Admin";case r.SystemOrgGroupType.SystemMembers:return"Member";case r.SystemOrgGroupType.SystemGuests:return"Guest";case r.SystemOrgGroupType.SystemViewers:return"Viewer";default:(0,t.default)(e)}}])},192915,e=>{"use strict";var r=e.i(276385),t=e.i(157630);let i=e=>({href:{pathname:"/profile",query:{username:"string"==typeof e?e:e.username}},as:"string"==typeof e?`/@${e}`:e.url});e.s(["UserLink",0,({user:e,children:s})=>(0,r.jsx)(t.default,{...i(e),prefetch:!1,children:s}),"userLinkProps",0,i])},66982,e=>{"use strict";var r=e.i(276385),t=e.i(389959);e.i(2001);var i=e.i(480028);e.s(["ExactMatchSubString",0,({source:e,match:t})=>{if(!e.toLowerCase().includes(t.toLowerCase()))return(0,r.jsx)(r.Fragment,{children:e});let[i,s]=e.split(RegExp(`${t.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")}(.+)?`,"i"));return(0,r.jsx)(r.Fragment,{children:[i,(0,r.jsx)("b",{children:e.substr(i.length,t.length)},t),s]})},"HighlightMatches",0,({source:e,matches:s,matchStyle:a={fontWeight:500,color:i.tokens.foregroundDefault},style:l={color:i.tokens.foregroundDimmest,maxWidth:"100%",wordWrap:"break-word"}})=>{let n,o=0,c=[],u=function(e){return(0,r.jsx)("span",{style:a,children:e})};return s.forEach(({column:r,length:t})=>{c.push(e.slice(o,r)),c.push(u(e.slice(r,r+t))),o=r+t}),c.push(e.slice(o)),n=c.map((e,i)=>(0,r.jsx)(t.Fragment,{children:e},i)),(0,r.jsx)("span",{style:l,children:n})}])},374652,e=>{"use strict";var r=e.i(135173),t=e.i(480028);e.s(["getBorderColor",0,({replCount:e,limit:i=r.STARTER_PLAN_REPL_LIMIT})=>e/i>=.25?t.tokens.blueDimmest:t.tokens.greyDimmest,"getFillColor",0,({replCount:e,limit:i=r.STARTER_PLAN_REPL_LIMIT})=>e/i>=.25?t.tokens.blueDimmer:t.tokens.greyDimmer])},181389,931737,562888,e=>{"use strict";var r=e.i(973245),t=e.i(5004);let i=r.gql`
    fragment TemplateReplCardFooterUser on User {
  id
  username
  fullName
  image
  url
}
    `,s=r.gql`
    fragment TemplateReplCardFooterTeam on Team {
  id
  username
  image
  url
}
    `,a=r.gql`
    fragment TemplateReplCardRepl on Repl {
  id
  iconUrl
  title
  description(plainText: true)
  releasesForkCount
  templateLabel
  likeCount
  url
  owner {
    ... on User {
      id
      ...TemplateReplCardFooterUser
    }
    ... on Team {
      id
      ...TemplateReplCardFooterTeam
    }
  }
  deployment {
    id
    activeRelease {
      id
    }
  }
  publishedAs
  templateCategories {
    id
    title
  }
}
    ${i}
${s}`;e.s(["TemplateReplCardReplFragmentDoc",0,a],931737);let l=r.gql`
    fragment TemplateSelector2Repl on Repl {
  id
  url
  title
  iconUrl
  templateLabel
  nixedLanguage
  isPrivate
  isRenamed
  likeCount
  description(plainText: true)
  deployment {
    id
    activeRelease {
      id
    }
  }
  owner {
    ... on User {
      id
      username
    }
    ... on Team {
      id
      username
    }
  }
  slug
  ...TemplateReplCardRepl
}
    ${a}`;e.s(["TemplateSelector2ReplFragmentDoc",0,l],562888);var n=e.i(304277);e.i(566901);var o=e.i(951262);let c={},u=r.gql`
    fragment CreateReplFormRepl on Repl {
  id
  ...TemplateSelector2Repl
}
    ${l}`,d=r.gql`
    fragment CreateReplFormCurrentUser on CurrentUser {
  id
  url
  image
  username
  fullName
  isStaff: hasRole(role: REPLIT_STAFF)
  hasAgentRepl {
    ... on HasAgentRepl {
      hasAgentRepl
    }
  }
  replCount {
    ... on ReplCount {
      count
    }
  }
  ...ReplOwnerCurrentUser
  teams {
    id
    ...ReplOwnerTeam
  }
  favoriteCreateReplOptions {
    ... on Repl {
      id
      ...CreateReplFormRepl
    }
  }
}
    ${t.ReplOwnerCurrentUserFragmentDoc}
${t.ReplOwnerTeamFragmentDoc}
${u}`,p=r.gql`
    query CreateReplForm {
  currentUser {
    id
    ...CreateReplFormCurrentUser
  }
}
    ${d}`,g=r.gql`
    query CreateReplFormInitialRepl($replId: String!) {
  getRepl(id: $replId) {
    ... on Repl {
      id
      ...CreateReplFormRepl
    }
  }
}
    ${u}`,m=r.gql`
    mutation CreateReplFormCreateRepl($input: CreateReplInput!, $isTitleAutoGenerated: Boolean!) {
  createRepl(input: $input, isTitleAutoGenerated: $isTitleAutoGenerated) {
    ... on Repl {
      ...CreateReplFormRepl
    }
    ... on UserError {
      message
    }
  }
}
    ${u}`;e.s(["CreateReplFormCurrentUserFragmentDoc",0,d,"CreateReplFormReplFragmentDoc",0,u,"useCreateReplFormCreateReplMutation",0,function(e){let r={...c,...e};return o.useMutation(m,r)},"useCreateReplFormInitialReplQuery",0,function(e){let r={...c,...e};return n.useQuery(g,r)},"useCreateReplFormQuery",0,function(e){let r={...c,...e};return n.useQuery(p,r)}],181389)},109459,215814,e=>{"use strict";var r=e.i(276385),t=e.i(389959),i=e.i(480028),s=e.i(919073);function a({children:e,className:t,innerRef:l}){return(0,r.jsx)(s.ShadesSurface,{className:t,tag:"ul",innerRef:l,css:[{zIndex:999,maxHeight:300,position:"absolute",overflowY:"auto",width:"100%",left:0,top:i.tokens.space8,border:"1px solid",borderColor:i.tokens.outlineDimmest,listStyle:"none"}],br:8,children:e})}let l=(0,t.forwardRef)((e,t)=>(0,r.jsx)(a,{innerRef:t,...e}));l.displayName="Menu",e.s(["default",0,l],109459);var n=e.i(983420),o=e.i(967629),c=e.i(723517),u=e.i(691636),d=e.i(8047),p=e.i(61732),g=e.i(66982);let m=({highlighted:e,selected:r,taller:t})=>(0,o.css)([u.rcss.rowWithGap(8),u.rcss.align.center,u.rcss.p(8),u.rcss.borderRadius(4),{cursor:"pointer",height:t?"auto":i.tokens.space32,border:"0 !important"},e&&!r&&[c.interactive.nofill,{background:i.tokens.interactiveBackground}],r&&{backgroundColor:i.tokens.accentPrimaryDimmer,color:i.tokens.foregroundDefault,":hover":{backgroundColor:i.tokens.accentPrimaryDefault}},e&&r&&[u.rcss.backgroundColor.accentPrimaryDefault]]);e.s(["default",0,function(e){let t=e.filter?(0,r.jsx)(g.ExactMatchSubString,{source:e.title,match:e.filter}):e.title;return e.subtitle?(0,r.jsxs)(p.View,{css:m(e),children:[e.icon?(0,r.jsx)(n.IconProvider,{size:e.subtitle?24:16,children:e.icon}):null,(0,r.jsxs)(p.View,{gap:4,grow:!0,shrink:!0,children:[(0,r.jsx)(d.Text,{height:"singleLine",multiline:!1,children:t}),(0,r.jsx)(d.Text,{multiline:!1,height:"singleLine",variant:"small",color:e.selected?void 0:"dimmer",children:e.subtitle})]})]}):(0,r.jsxs)(p.View,{css:m(e),children:[e.icon?(0,r.jsx)(n.IconProvider,{size:e.subtitle?24:16,children:e.icon}):null,(0,r.jsx)(d.Text,{css:{flexShrink:1},multiline:!1,children:t})]})}],215814)},696664,e=>{"use strict";var r=e.i(973245),t=e.i(319801);let i=r.gql`
    fragment ReplViewReplActionsCurrentUser on CurrentUser {
  isModerator: hasRole(role: MODERATOR)
  isAdmin: hasRole(role: ADMIN)
}
    `,s=r.gql`
    fragment UnpublishReplRepl on Repl {
  id
  likeCount
  publishedAs
}
    `,a=r.gql`
    fragment ReplViewReplActionsPermissions on Repl {
  id
  publishedAs
  owner {
    ... on User {
      id
      username
    }
    ... on Team {
      id
      username
    }
  }
  templateReview {
    id
    promoted
  }
  authorizations {
    editFileContents {
      isAuthorized
    }
    publish {
      isAuthorized
    }
  }
  ...UnpublishReplRepl
  ...ReplLinkRepl
}
    ${s}
${t.ReplLinkReplFragmentDoc}`;e.s(["ReplViewReplActionsCurrentUserFragmentDoc",0,i,"ReplViewReplActionsPermissionsFragmentDoc",0,a])},59897,e=>{"use strict";var r=e.i(973245),t=e.i(696664),i=e.i(931737),s=e.i(304277);e.i(566901);let a={},l=r.gql`
    fragment CluiTemplateReplCurrentUser on CurrentUser {
  id
  ...ReplViewReplActionsCurrentUser
}
    ${t.ReplViewReplActionsCurrentUserFragmentDoc}`,n=r.gql`
    fragment CluiTemplateReplListRepl on Repl {
  templateCategories {
    id
    title
  }
  ...TemplateReplCardRepl
  ...ReplViewReplActionsPermissions
}
    ${i.TemplateReplCardReplFragmentDoc}
${t.ReplViewReplActionsPermissionsFragmentDoc}`,o=r.gql`
    query CluiTemplateReplSubmissions {
  currentUser {
    ...CluiTemplateReplCurrentUser
  }
}
    ${l}`;e.s(["CluiTemplateReplCurrentUserFragmentDoc",0,l,"CluiTemplateReplListReplFragmentDoc",0,n,"useCluiTemplateReplSubmissionsQuery",0,function(e){let r={...a,...e};return s.useQuery(o,r)}])},729092,e=>{"use strict";let r={padding:!0,symbols:["","K","M","G","T","P","E"]};e.s(["abbreviateNumber",0,function(e,t=1,i={padding:!1}){Array.isArray(i)&&(i={symbols:i});let{symbols:s,padding:a}=Object.assign({},r,i),l=Math.sign(e)>=0,n=Math.log10(e=Math.abs(e))/3|0;if(0===n)return(l?"":"-")+e.toString();let o=s[n];if(!o)throw RangeError();let c=(e/10**(3*n)).toFixed(t);return a||(c=String(Number(c))),(l?"":"-")+c+o}])},665439,e=>{e.v({icon:"OfficialIcon-module__5xUwQq__icon",iconBig:"OfficialIcon-module__5xUwQq__iconBig",iconSmall:"OfficialIcon-module__5xUwQq__iconSmall"})},421145,e=>{"use strict";var r=e.i(276385),t=e.i(183035),i=e.i(61732),s=e.i(665439);e.s(["default",0,function({big:e}){return(0,r.jsx)(i.View,{clsx:[s.default.icon,e?s.default.iconBig:s.default.iconSmall],children:(0,r.jsx)(t.default,{"aria-label":"Official",size:e?void 0:12})})}])},908904,e=>{"use strict";var r=e.i(276385),t=e.i(157630),i=e.i(113388),s=e.i(40916),a=e.i(761201),l=e.i(729092),n=e.i(421145),o=e.i(192915),c=e.i(967629),u=e.i(480028),d=e.i(723517),p=e.i(691636),g=e.i(766299),m=e.i(643484),x=e.i(744006),h=e.i(8047),f=e.i(21875),R=e.i(61732),w=e.i(183555),y=e.i(921125),j=e.i(365757);function C({count:e,children:t,tooltip:i}){let s=(0,l.abbreviateNumber)(e);return(0,r.jsxs)(R.View,{"aria-label":i,"data-microtip-position":"left",role:"tooltip",css:[{userSelect:"none"}],row:!0,gap:4,align:"center",children:[t,(0,r.jsx)(h.Text,{color:"dimmest",multiline:!1,children:s})]})}function T({owner:e,onLinkClick:i}){return null===e?(0,r.jsx)(f.User,{small:!0,src:null,username:"[deleted]"}):(0,r.jsx)(t.default,{...(0,o.userLinkProps)(e),css:[p.rcss.viewStyle,p.rcss.rowWithGap(4),p.rcss.position.relative,d.interactive.nofill,{color:"inherit",flexShrink:1,zIndex:1}],onClick:i,children:(0,r.jsx)(f.User,{small:!0,username:e.username,fullName:"fullName"in e?e.fullName:void 0,src:e?.image||null})})}let v=(0,c.css)({"::after":{borderRadius:u.tokens.space8,content:'""',position:"absolute",top:0,right:0,bottom:0,left:0,display:"block",zIndex:1}});e.s(["OwnerLink",0,T,"default",0,function({repl:e,onReplLinkClick:o,onOwnerLinkClick:c,linkToRepl:f=!0,hideCategory:b=!1,forkable:k=!1,..._}){let P=(0,w.useForkContext)(),S=(0,g.useIdSeed)(),U=S("title"),D=S("description");return(0,r.jsxs)(R.View,{..._,tag:"article",tabIndex:-1,css:[p.rcss.position.relative,f&&d.interactive.filledAndOutlined,!f&&[{border:"1px solid "+u.tokens.outlineDimmest},p.rcss.borderRadius(8)]],grow:!0,shrink:!0,p:12,"aria-labelledby":U,"aria-describedby":D,gap:8,children:[(0,r.jsxs)(R.View,{row:!0,gap:8,justify:"space-between",align:"start",children:[(0,r.jsx)(j.default,{surface:!0,iconUrl:e.iconUrl,alt:"",css:[{backgroundColor:d.interactive.filled.backgroundColor}]}),!b&&e.templateCategories.length&&e.templateCategories[0]?(0,r.jsx)(x.Pill,{text:e.templateCategories[0].title,translate:"no"}):null,k?(0,r.jsx)(m.Button,{text:P.isForking?"Forking...":"Use Framework",onClick:()=>P.fork(),disabled:P.isForking,iconLeft:(0,r.jsx)(i.default,{}),variant:"outlined",css:[{zIndex:2}]}):null]}),(0,r.jsxs)(R.View,{row:!0,gap:8,align:"center",id:U,children:[f?(0,r.jsx)(t.default,{...(0,y.replViewLinkProps)(e),css:[{color:"inherit"},p.rcss.focusRingOnAfter,v,p.rcss.flex.shrink(1)],onClick:o,children:(0,r.jsx)(h.Text,{variant:"subheadBig",maxLines:1,translate:"no",children:e.templateLabel})}):(0,r.jsx)(h.Text,{variant:"subheadBig",css:[p.rcss.flex.shrink(1)],maxLines:1,translate:"no",children:e.templateLabel}),e.owner?.username===a.OFFICIAL_TEMPLATE_USERNAME?(0,r.jsx)(n.default,{}):null]}),(0,r.jsx)(R.View,{css:[{minHeight:66}],grow:!0,shrink:!0,justify:"end",children:(0,r.jsx)(h.Text,{color:"dimmest",maxLines:3,id:D,multiline:!1,children:e.description||"--"})}),(0,r.jsxs)(R.View,{row:!0,gap:8,justify:"space-between",children:[(0,r.jsx)(T,{owner:e.owner||null,onLinkClick:c}),(0,r.jsx)(R.View,{row:!0,gap:8,children:(0,r.jsx)(C,{count:e.releasesForkCount,tooltip:1===e.releasesForkCount?"1 repl uses this template":`${(0,l.abbreviateNumber)(e.releasesForkCount)} repls use this template`,children:(0,r.jsx)(s.default,{color:u.tokens.foregroundDimmest})})})]})]})}])},373104,849492,e=>{"use strict";var r=e.i(389959),t=e.i(908796),i=e.i(973245),s=e.i(931737),a=e.i(181389),l=e.i(59897),n=e.i(304277);e.i(566901);let o={},c=i.gql`
    fragment UseTemplatesTemplate on Repl {
  id
  ...TemplateReplCardRepl
  ...CreateReplFormRepl
  ...CluiTemplateReplListRepl
}
    ${s.TemplateReplCardReplFragmentDoc}
${a.CreateReplFormReplFragmentDoc}
${l.CluiTemplateReplListReplFragmentDoc}`,u=i.gql`
    query UseTemplates($options: TemplateRepls2QueryOptions!) {
  templateRepls2(options: $options) {
    ... on TemplateReplSearchConnection {
      items {
        __typename
        id
        ...UseTemplatesTemplate
      }
      pageInfo {
        hasNextPage
      }
      orderBy
      promotionStatus
      searchQuery
      total
      category
    }
    ... on UserError {
      message
    }
  }
}
    ${c}`;var d=e.i(619158);e.s(["default",0,function({orderBy:e=t.TemplateRepls2OrderBy.Forks,pageSize:i=12,promotionStatus:s=t.TemplateRepls2PromotionStatus.All,initialSearchValue:a="",ssr:l=!0,noBatch:c=!1,categoryId:p,debounceDuration:g="short"}){var m;let x,[h,f]=(0,r.useState)(a),R=(0,d.default)(h,"short"===g?50:200),{data:w,loading:y,error:j,fetchMore:C}=(m={variables:{options:{searchQuery:R,after:0,orderBy:e,count:i,promotionStatus:s,category:p}},notifyOnNetworkStatusChange:!0,ssr:l,context:{noBatch:c}},x={...o,...m},n.useQuery(u,x)),T=(0,r.useCallback)(async()=>{w?.templateRepls2.__typename!=="TemplateReplSearchConnection"||!w?.templateRepls2.pageInfo.hasNextPage||y||await C({variables:{options:{searchQuery:R,after:w.templateRepls2.items.length,count:i,orderBy:e,promotionStatus:s,category:p}}})},[w,C,R,e,i,y,s,p]),v=w?.templateRepls2.__typename==="TemplateReplSearchConnection"?w.templateRepls2.items:[],b=w?.templateRepls2.__typename==="UserError"?w?.templateRepls2.message:void 0;return{setSearchInputValue:f,searchInputValue:h,loadMore:T,loading:y,hasMore:w?.templateRepls2.__typename==="TemplateReplSearchConnection"&&w.templateRepls2.pageInfo.hasNextPage,error:j?"Something went wrong. Try refreshing the page.":b,templates:v,searchQuery:R}}],373104),e.s(["OrderBy",()=>t.TemplateRepls2OrderBy],849492)},79949,e=>{"use strict";var r=e.i(908796);e.s(["PromotionStatus",()=>r.TemplateRepls2PromotionStatus])},648552,e=>{"use strict";var r=e.i(389959),t=e.i(908796),i=e.i(672220),s=e.i(320216),a=e.i(151027),l=e.i(933302);e.s(["useOrgSwitcher",0,function(){let{showError:e}=(0,s.default)(),n=(0,l.useSyncStatsigOrgContext)(),o=(0,a.useSetOptimisticOrg)(),[c]=(0,i.useCurrentUserOrgContextUpdateOrgContextMutation)({refetchQueries:[{query:i.CurrentUserOrgContextDocument}],onCompleted(r){r.updateOrgContext&&"Org"!==r.updateOrgContext.__typename&&e("Something went wrong switching workspaces. Please try again.")},onError(){e("Something went wrong switching workspaces. Please try again.")}});return(0,r.useCallback)(e=>{let r=e.type===t.OrgstypeEnumType.Personal,i=r?{orgId:void 0,orgSlug:void 0,orgRole:void 0,orgDealContext:void 0}:{orgId:e.id,orgSlug:e.slug,orgRole:e.orgRole,orgDealContext:e.orgDealContext};n(i.orgId,r?void 0:e.orgDealContext.dealType),o(i),c({variables:{input:{orgId:i.orgId}}})},[n,o,c])}])},294827,e=>{"use strict";var r=e.i(908796),t=e.i(973245),i=e.i(304277);e.i(566901);let s={},a=t.gql`
    fragment PersonalWorkspacesDisabledCurrentUser on CurrentUser {
  id
  personalWorkspacesDisabled
}
    `,l=t.gql`
    query PersonalWorkspacesDisabled {
  currentUser {
    ...PersonalWorkspacesDisabledCurrentUser
  }
}
    ${a}`;e.s(["usePersonalWorkspacesDisabled",0,function(){let e,{data:t}=(e={...s,...void 0},i.useQuery(l,e)),a=t?.currentUser,n=a?.personalWorkspacesDisabled??r.PersonalWorkspacesDisabledMode.None,o=n!==r.PersonalWorkspacesDisabledMode.None;return{shouldHidePersonalWorkspace:n===r.PersonalWorkspacesDisabledMode.Personal||n===r.PersonalWorkspacesDisabledMode.Full,restrictionMode:n,isRestrictedDomain:o}}],294827)},752533,e=>{e.v({dropdownAvatarAndName:"AvatarDropdown-module__n3A4ZW__dropdownAvatarAndName",dropdownItem:"AvatarDropdown-module__n3A4ZW__dropdownItem",dropdownItemSelected:"AvatarDropdown-module__n3A4ZW__dropdownItemSelected",orgNameText:"AvatarDropdown-module__n3A4ZW__orgNameText",overflowIndicator:"AvatarDropdown-module__n3A4ZW__overflowIndicator",sectionHeader:"AvatarDropdown-module__n3A4ZW__sectionHeader",workspaceContainerWrapper:"AvatarDropdown-module__n3A4ZW__workspaceContainerWrapper",workspaceDropdownContainer:"AvatarDropdown-module__n3A4ZW__workspaceDropdownContainer"})},795859,e=>{"use strict";var r=e.i(276385),t=e.i(420180),i=e.i(389959),s=e.i(908796),a=e.i(183035),l=e.i(320216),n=e.i(648552),o=e.i(294827),c=e.i(955410),u=e.i(448942),d=e.i(276887),p=e.i(406664),g=e.i(825419),m=e.i(744006),x=e.i(8047),h=e.i(61732),f=e.i(752533);let R=({currentUser:e,selected:t,onClick:i})=>{let s=(0,p.useCreateInteractive)({variant:"listItem"});return(0,r.jsxs)(h.View,{clsx:[s.clsx,t?f.default.dropdownItemSelected:f.default.dropdownItem],style:s.style,onClick:i,row:!0,align:"center",justify:t?"space-between":void 0,px:8,py:4,children:[(0,r.jsxs)(h.View,{clsx:f.default.dropdownAvatarAndName,row:!0,align:"center",gap:8,children:[(0,r.jsx)(g.Avatar,{src:e.image,username:e.username,fullName:e.fullName,size:20}),(0,r.jsx)(x.Text,{variant:"text",color:t?"default":"dimmer",multiline:!1,clsx:f.default.orgNameText,children:"Personal"})]}),(0,r.jsx)(h.View,{align:"center",row:!0,children:t?(0,r.jsx)(a.default,{size:16}):null})]})},w=({selected:e,org:i,currentOrgId:o,groupType:R,isNewPillStyle:w=!1,onRoute:y})=>{let j=(0,p.useCreateInteractive)({variant:"listItem"}),{showError:C}=(0,l.default)(),{trackClick:T}=(0,c.useTrackClick)(),v=(0,n.useOrgSwitcher)(),{name:b,slug:k}=i,{home:_}=(0,u.orgLinks)({slug:k}),P=(0,t.useRouter)();return(0,r.jsxs)(h.View,{clsx:[j.clsx,e?f.default.dropdownItemSelected:f.default.dropdownItem],style:j.style,onClick:()=>{e||T({productArea:"workspaces",target:"switch_workspace_item",properties:{previous_workspace_type:o?"shared":"personal",target_workspace_type:"shared"}}),i.currentUserRole?(v({type:s.OrgType.Team,id:i.id,slug:i.slug,orgRole:i.currentUserRole,orgDealContext:i.dealContext}),y()):C("Something went wrong, please try again."),P.push(_.href)},row:!0,align:"center",justify:e?"space-between":void 0,px:8,py:4,children:[(0,r.jsxs)(h.View,{clsx:f.default.dropdownAvatarAndName,row:!0,align:"center",gap:8,children:[(0,r.jsx)(g.Avatar,{src:i.image??null,username:b,fullName:i.name,size:20}),(0,r.jsxs)(h.View,{row:!0,align:"center",gap:8,children:[(0,r.jsx)(x.Text,{variant:"text",color:e?"default":"dimmer",multiline:!1,translate:"no",clsx:f.default.orgNameText,children:b}),R&&w?(0,r.jsx)(m.Pill,{text:(0,d.orgGroupToDisplayName)(R),compact:!0}):null,R&&!w?(0,r.jsx)(x.Text,{variant:"small",color:"dimmest",children:(0,d.orgGroupToDisplayName)(R)}):null]})]}),(0,r.jsx)(h.View,{align:"center",row:!0,children:e?(0,r.jsx)(a.default,{size:16}):null})]})};e.s(["OrgDropdown",0,({currentUser:e,currentOrgId:a,loading:l=!1,hasOrgs:u=!1,onRoute:d})=>{let p=(0,t.useRouter)(),g=(0,i.useRef)(null),[m,y]=(0,i.useState)(!1),{shouldHidePersonalWorkspace:j}=(0,o.usePersonalWorkspacesDisabled)(),{trackClick:C}=(0,c.useTrackClick)(),T=(0,n.useOrgSwitcher)();return((0,i.useEffect)(()=>{let e=()=>{if(g.current){let{scrollHeight:e,clientHeight:r,scrollTop:t}=g.current;y(e>r&&!(t+r>=e-1))}};e(),window.addEventListener("resize",e);let r=g.current;return r&&r.addEventListener("scroll",e),()=>{window.removeEventListener("resize",e),r&&r.removeEventListener("scroll",e)}},[]),e?.orgs&&"CurrentUserOrganizationConnection"===e.orgs.__typename&&!l&&u)?(0,r.jsx)(r.Fragment,{children:(0,r.jsxs)(h.View,{children:[(0,r.jsx)(h.View,{clsx:f.default.sectionHeader,row:!0,align:"center",p:8,children:(0,r.jsx)(x.Text,{variant:"small",color:"dimmest",children:"Switch Workspace"})}),(0,r.jsxs)(h.View,{clsx:f.default.workspaceContainerWrapper,children:[(0,r.jsxs)(h.View,{innerRef:g,clsx:f.default.workspaceDropdownContainer,children:[j?null:(0,r.jsx)(R,{currentUser:e,selected:void 0===a,onClick:()=>{a&&C({productArea:"workspaces",target:"switch_workspace_item",properties:{previous_workspace_type:"shared",target_workspace_type:"personal"}}),T({type:s.OrgType.Personal}),p.push("/home","/~",{shallow:!1})}}),e.orgs.items.map(({org:e,type:t})=>(0,r.jsx)(w,{org:e,groupType:t,selected:e.id===a,currentOrgId:a,onRoute:d},e.id))]}),m?(0,r.jsx)(h.View,{clsx:f.default.overflowIndicator}):null]})]})}):null},"OrgDropdownItem",0,w,"PersonalDropdownItem",0,R])},793410,e=>{e.v({placeholder:"DefaultOrgIcon-module__jpmNua__placeholder"})},897395,644756,e=>{"use strict";var r=e.i(276385),t=e.i(389959),i=e.i(973245),s=e.i(85085),a=e.i(884033),l=e.i(304277);e.i(566901);let n={},o=i.gql`
    query GetOwnerPillOrgs {
  currentUser {
    id
    ...OrgSwitcherCurrentUser
  }
}
    ${s.OrgSwitcherCurrentUserFragmentDoc}`;function c(e){let r={...n,...e};return l.useQuery(o,r)}let u=i.gql`
    query GetOwnerPillWorkspaceDropdown {
  currentUser {
    ...WorkspaceDropdownCurrentUser
  }
}
    ${a.WorkspaceDropdownCurrentUserFragmentDoc}`;function d(e){let r={...n,...e};return l.useQuery(u,r)}e.s(["GetOwnerPillOrgsDocument",0,o,"useGetOwnerPillOrgsQuery",0,c,"useGetOwnerPillWorkspaceDropdownQuery",0,d],644756);var p=e.i(167392),g=e.i(568430),m=e.i(269848),x=e.i(151027),h=e.i(612343),f=e.i(61732),R=e.i(793410);let w=()=>(0,r.jsx)(f.View,{align:"center",justify:"center",br:"full",clsx:R.default.placeholder,children:(0,r.jsx)(h.default,{size:12})});var y=e.i(276887),j=e.i(825419),C=e.i(643484),T=e.i(773222),v=e.i(795859),b=e.i(420180),k=e.i(908796),_=e.i(40916),P=e.i(596139),S=e.i(856010),U=e.i(648552),D=e.i(294827),A=e.i(955410);e.i(450717);var I=e.i(242917),O=e.i(480028),E=e.i(406664),L=e.i(919073),F=e.i(744006),M=e.i(8047),N=e.i(158323),W=e.i(752533);let B=({onClick:e,showCoreBadge:t=!1})=>{let i=(0,E.useCreateInteractive)({variant:"listItem"});return(0,r.jsxs)(f.View,{clsx:[i.clsx,W.default.dropdownItem],style:i.style,onClick:e,row:!0,align:"center",justify:t?"space-between":void 0,px:8,py:4,gap:16,children:[(0,r.jsxs)(f.View,{clsx:W.default.dropdownAvatarAndName,row:!0,align:"center",gap:8,children:[(0,r.jsx)(f.View,{row:!0,align:"center",justify:"center",px:2,children:(0,r.jsx)(_.default,{color:O.tokens.foregroundDimmest,size:16})}),(0,r.jsx)(M.Text,{variant:"text",color:"dimmer",multiline:!1,children:"Create workspace"})]}),t?(0,r.jsx)(N.default,{plan:P.corePlanName,size:"small"}):null]})},V=({currentOrgId:e,onRoute:i,currentUser:s,onlyUnifiedPlanEnabled:a=!1})=>{let l=(0,b.useRouter)(),n=(0,t.useRef)(null),[o,c]=(0,t.useState)(!1),{shouldHidePersonalWorkspace:u}=(0,D.usePersonalWorkspacesDisabled)(),{show:d}=(0,I.useGlobalModal)(),{trackClick:p}=(0,A.useTrackClick)(),g=(0,U.useOrgSwitcher)();(0,t.useEffect)(()=>{let e=()=>{if(n.current){let{scrollHeight:e,clientHeight:r,scrollTop:t}=n.current;c(e>r&&!(t+r>=e-1))}};return e(),window.addEventListener("resize",e),()=>window.removeEventListener("resize",e)},[s]);let m=(0,S.useIsUnifiedPlanEnabled)({currentUser:s}),x=(e,r)=>{if(p({productArea:"workspaces",target:"open_create_workspace_modal_button",properties:{canCreateWorkspace:r}}),m&&!r){i(),d("MembershipPurchaseModal",{analyticsContext:{upgrade:{context:"header_avatar"}}});return}i(),d("CreateWorkspaceModal",{customerId:e})};(0,t.useEffect)(()=>{let e=()=>{if(n.current){let{scrollHeight:e,clientHeight:r,scrollTop:t}=n.current;c(e>r&&!(t+r>=e-1))}},r=n.current;if(r)return r.addEventListener("scroll",e),()=>r.removeEventListener("scroll",e)},[s]);let h=s.customer.orgs;if("OrgConnection"!==h.__typename||"CustomerConnection"!==s.customers.__typename)return null;let R=s.customers.items.filter(e=>e.id!==s.customer.id&&(!a||e.isUnifiedPlanEnabled));return(0,r.jsx)(r.Fragment,{children:(0,r.jsxs)(f.View,{clsx:W.default.workspaceContainerWrapper,children:[(0,r.jsxs)(f.View,{innerRef:n,clsx:W.default.workspaceDropdownContainer,children:[!a||m?(0,r.jsxs)(r.Fragment,{children:[u?null:(0,r.jsx)(f.View,{clsx:W.default.sectionHeader,row:!0,align:"center",p:8,children:(0,r.jsx)(M.Text,{variant:"small",color:"dimmest",children:"Your workspaces"})}),u?null:(0,r.jsx)(v.PersonalDropdownItem,{currentUser:s,selected:void 0===e,onClick:()=>{e&&p({productArea:"workspaces",target:"switch_workspace_item",properties:{previous_workspace_type:"shared",target_workspace_type:"personal"}}),g({type:k.OrgType.Personal}),l.push("/home","/~",{shallow:!1})}}),h.items.map(t=>(0,r.jsx)(v.OrgDropdownItem,{org:t,selected:t.id===e,currentOrgId:e,isNewPillStyle:!0,onRoute:i},t.id)),s.customer.isUnifiedPlanEnabled&&!u&&s.customer.authorizations.createWorkspace.code!==k.CustomerAuthorizationCode.ScimEnabled&&s.customer.authorizations.createWorkspace.code!==k.CustomerAuthorizationCode.WorkosEnabled?(0,r.jsx)(B,{onClick:()=>x(s.customer.id,s.customer.authorizations.createWorkspace.isAuthorized),showCoreBadge:!s.customer.authorizations.createWorkspace.isAuthorized}):null]}):null,R.map(t=>{if("OrgConnection"!==t.orgs.__typename)return null;let s=t.orgs.items,a=t.name?.trim()||"",l=t.authorizations.createWorkspace.isAuthorized;return(0,r.jsxs)(L.ShadesSurface,{elevate:!1,border:{side:"top"},background:!1,children:[a?(0,r.jsxs)(f.View,{clsx:W.default.sectionHeader,row:!0,align:"center",gap:8,p:8,children:[(0,r.jsx)(M.Text,{variant:"small",color:"dimmest",children:a}),l?(0,r.jsx)(F.Pill,{text:"Admin",compact:!0}):null]}):null,s.map(t=>(0,r.jsx)(v.OrgDropdownItem,{org:t,selected:t.id===e,currentOrgId:e,groupType:!l&&t.currentUserRole?t.currentUserRole:void 0,isNewPillStyle:!0,onRoute:i},t.id)),l&&t.isUnifiedPlanEnabled?(0,r.jsx)(B,{onClick:()=>x(t.id,l)}):null]},t.id)})]}),o?(0,r.jsx)(f.View,{clsx:W.default.overflowIndicator}):null]})})};e.s(["OwnerPill",0,function({ownerName:e,image:i,currentOrgId:s,isNewDesignEnabled:a=!1,loading:l=!1,onlyUnifiedPlanEnabled:n,alignment:o,stretch:u}){let h,[f,R]=(0,t.useState)(!1),b=(0,x.useCurrentUserStoredOrgContext)(),k=!a,{data:_}=c({skip:!k}),{data:P}=d({skip:k,fetchPolicy:"cache-and-network",ssr:!1});if(k&&!_)return null;let S=_?.currentUser,U=S?.orgs,D=U?.__typename==="CurrentUserOrganizationConnection"?U.items:[];if(k&&(!S||U?.__typename!=="CurrentUserOrganizationConnection")||k&&!D.length)return null;let A=(0,r.jsx)(j.Avatar,{src:i??null,username:e,size:24}),I=(0,y.getFormattedOrgWorkspaceName)({ownerName:e,isInOrg:!!s});return h=!k&&P?.currentUser?(0,r.jsx)(V,{currentOrgId:b.orgId,currentUser:P.currentUser,onRoute:()=>{R(!1)},onlyUnifiedPlanEnabled:n}):k&&S?(0,r.jsx)(v.OrgDropdown,{currentUser:S,currentOrgId:b.orgId,loading:!1,hasOrgs:D.length>0,onRoute:()=>{R(!1)}}):(0,r.jsx)(r.Fragment,{}),(0,r.jsxs)(T.PopoverTrigger,{isOpen:f,onOpenChange:R,placement:"bottom",label:"Switch Workspace",style:{marginLeft:"-6px"},children:[(0,r.jsx)(C.Button,{style:{paddingLeft:4},borderRadius:"full",iconLeft:l?(0,r.jsx)(m.default,{}):s?i?A:(0,r.jsx)(w,{}):A,iconRight:f?(0,r.jsx)(g.default,{}):(0,r.jsx)(p.default,{}),text:l?"":I,loading:l,alignment:o,stretch:u}),h]})}],897395)},22834,e=>{"use strict";var r=e.i(276385),t=e.i(389959),i=e.i(480028),s=e.i(462229),a=e.i(691636),l=e.i(8047),n=e.i(244945),o=e.i(61732);let c=(0,s.cssRecord)({usageString:[a.rcss.fontSize(12)],title:[a.rcss.fontSize(12),a.rcss.fontWeight.medium],meterWrapper:[a.rcss.minWidth(42)],icon:[a.rcss.color.foregroundDimmest]});e.s(["UsageMeterWrapper",0,({icon:e,usageString:i,title:s,tooltip:a,children:u})=>(0,r.jsxs)(o.View,{grow:!0,row:!0,gap:8,align:"center",children:[(0,r.jsx)(o.View,{css:c.icon,children:(0,t.cloneElement)(e,{css:c.icon})}),(0,r.jsxs)(o.View,{grow:!0,gap:2,children:[(0,r.jsx)(l.Text,{height:"singleLine",color:"dimmer",css:c.title,children:s}),(0,r.jsx)(o.View,{row:!0,align:"center",gap:4,children:(0,r.jsx)(l.Text,{color:"dimmest",height:"singleLine",css:c.usageString,children:i})})]}),(0,r.jsx)(o.View,{css:c.meterWrapper,children:a?(0,r.jsx)(n.Tooltip,{tooltip:a,children:u}):u})]}),"getPercentageBorderColor",0,function({decimal:e}){return e>.25?i.tokens.blueDimmest:i.tokens.greyDimmest},"getPercentageFillColor",0,function({decimal:e}){return e>.25?i.tokens.blueDimmer:i.tokens.greyDimmer}])},882263,e=>{"use strict";var r=e.i(973245),t=e.i(304277);e.i(566901);let i={},s=r.gql`
    query GetCloudFreeUsage {
  currentUser {
    id
    cloudFreeUsageLimits {
      ... on FreemiumCloudUsageLimits {
        usage
        limit
        nextCreditsAt
      }
      ... on Error {
        message
      }
    }
  }
}
    `;e.s(["useGetCloudFreeUsage",0,function({skip:e}={}){var r;let a,{data:l,loading:n,error:o,refetch:c}=(r={skip:e},a={...i,...r},t.useQuery(s,a));return{loading:n,error:o,cloudUsage:l?.currentUser?.cloudFreeUsageLimits.__typename==="FreemiumCloudUsageLimits"?l?.currentUser?.cloudFreeUsageLimits:void 0,refetch:c}}],882263)},765269,e=>{"use strict";var r=e.i(276385),t=e.i(596139),i=e.i(135173),s=e.i(3466),a=e.i(929773),l=e.i(934440),n=e.i(882263),o=e.i(462229),c=e.i(691636),u=e.i(8047),d=e.i(61732),p=e.i(103490),g=e.i(480028),m=e.i(201894),x=e.i(22834);let h=(0,o.cssRecord)({measureBar:[c.rcss.height(10),c.rcss.borderRadius(2),c.rcss.overflow("visible")],measureBarProgress:[c.rcss.borderRadius(2),{marginTop:-1,marginLeft:-1,boxSizing:"content-box"}]}),f=({used:e=0,quota:t=1,loading:i})=>{let s=Math.min(1,e/t);return(0,r.jsx)(x.UsageMeterWrapper,{title:"Agent credits",icon:(0,r.jsx)(p.default,{}),usageString:i?"Loading...":`${Math.floor(100*s)}% used`,children:(0,r.jsx)(m.MeasureBar,{className:"measureBar",total:1,tooltipHidden:!0,current:s,loading:i,css:[h.measureBar,{".measureBarProgress":[c.rcss.border({color:(0,x.getPercentageBorderColor)({decimal:s})}),h.measureBarProgress]}],color:(0,x.getPercentageFillColor)({decimal:s}),backgroundColor:g.tokens.backgroundHigher})})};var R=e.i(490262);let w=(0,o.cssRecord)({measureBar:[c.rcss.height(10),c.rcss.borderRadius(2),c.rcss.overflow("visible")],measureBarProgress:[c.rcss.borderRadius(2),{marginTop:-1,marginLeft:-1,boxSizing:"content-box"}]}),y=({used:e=0,quota:t=1,loading:i})=>{let s=Math.min(1,e/t);return(0,r.jsx)(x.UsageMeterWrapper,{title:"Cloud credits",icon:(0,r.jsx)(R.default,{}),usageString:i?"Loading...":`${Math.floor(100*s)}% used`,children:(0,r.jsx)(m.MeasureBar,{className:"measureBar",total:1,tooltipHidden:!0,current:s,loading:i,css:[w.measureBar,{".measureBarProgress":[c.rcss.border({color:(0,x.getPercentageBorderColor)({decimal:s})}),w.measureBarProgress]}],color:(0,x.getPercentageFillColor)({decimal:s}),backgroundColor:g.tokens.backgroundHigher})})};var j=e.i(919073),C=e.i(108431);let T=2/3,v=({publicRepls:e,agentUsage:s,showReplsLimit:l=!0})=>{let n,o=(0,a.useReplLimit)(),c="data"===o.type?o.starterPlanReplLimit:i.STARTER_PLAN_REPL_LIMIT,u=(n=[],l&&n.push({type:"Apps",percentage:e/c}),n.push({type:`${t.freePlanName} plan usage`,percentage:s}),n),p=u.filter(e=>e.percentage>1),g=u.filter(e=>1===e.percentage),m=u.filter(e=>e.percentage>=.85&&e.percentage<1),x=u.filter(e=>e.percentage>=T&&e.percentage<.85),h=null;return p.length>0?h=(0,r.jsx)(j.ShadesSurface,{colorShade:"themeError",br:"container",children:(0,r.jsx)(C.StatusBanner,{text:"You've exceeded your usage limit"})}):g.length>0?h=(0,r.jsx)(j.ShadesSurface,{colorShade:"themeError",br:"container",children:(0,r.jsx)(C.StatusBanner,{text:"You've reached your usage limit"})}):m.length>0?h=(0,r.jsx)(j.ShadesSurface,{colorShade:"themeBrandInverted",br:"container",children:(0,r.jsx)(C.StatusBanner,{text:"You're nearing your usage limit"})}):x.length>0&&(h=(0,r.jsx)(j.ShadesSurface,{colorShade:"themeWarning",br:"container",children:(0,r.jsx)(C.StatusBanner,{text:"Approaching your usage limit"})})),h?(0,r.jsx)(d.View,{pb:4,children:h}):null};var b=e.i(806930),k=e.i(374652);let _=(0,o.cssRecord)({measureBar:[c.rcss.height(10),c.rcss.borderRadius(2),c.rcss.overflow("visible"),{pointerEvents:"none"}],measureBarProgress:[c.rcss.borderRadius(2),{marginTop:-1,marginLeft:-1,boxSizing:"content-box"}]}),P=({publicRepls:e,loading:t})=>{let s=e??0,l=(0,a.useReplLimit)(),n="data"===l.type?l.starterPlanReplLimit:i.STARTER_PLAN_REPL_LIMIT;return(0,r.jsx)(x.UsageMeterWrapper,{title:"Free Apps",tooltip:`You can create ${Math.max(0,n-s)} more Apps for free. Upgrade to create unlimited Public and Private Apps.`,icon:(0,r.jsx)(b.default,{}),usageString:t?"Loading...":`${s}/${n} created`,children:(0,r.jsx)(m.MeasureBar,{total:n,current:s,loading:t,color:(0,k.getFillColor)({replCount:s,limit:n}),tooltipHidden:!0,css:[_.measureBar,{".measureBarProgress":[c.rcss.border({color:(0,k.getBorderColor)({replCount:s,limit:n})}),_.measureBarProgress]}],backgroundColor:g.tokens.backgroundHigher})})},S=(0,o.cssRecord)({header:[c.rcss.display.flex,c.rcss.flex.row,c.rcss.justify.spaceBetween,c.rcss.align.center,c.rcss.pb(4),{alignSelf:"stretch"}],fontMedium:c.rcss.fontWeight.medium}),U=({publicRepls:e,replsLimitLoading:i,agentUsage:a,showReplsLimit:l=!0,cloudUsage:n})=>{let o=0;return a?.usage!==void 0&&a?.limit!==void 0&&a.limit>0&&(o=a.usage/a.limit),(0,r.jsxs)(d.View,{px:12,pt:12,pb:12,gap:8,children:[(0,r.jsx)(d.View,{css:S.header,children:(0,r.jsx)(u.Text,{css:S.fontMedium,color:"dimmer",height:"singleLine",children:"Your Starter Plan"})}),(0,r.jsx)(v,{publicRepls:e,agentUsage:o,showReplsLimit:l}),(0,r.jsxs)(d.View,{pb:4,gap:8,children:[l?(0,r.jsx)(P,{publicRepls:e,loading:i}):null,(0,r.jsx)(f,{used:a?.usage,quota:a?.limit,loading:a.loading})]}),(0,r.jsx)(d.View,{pb:4,gap:8,children:(0,r.jsx)(y,{used:n?.usage,quota:n?.limit,loading:n.loading})}),(0,r.jsx)(s.default,{dataCy:"sidebar-upgrade-btn",context:"sidebar",text:`Upgrade to Replit ${t.corePlanName}`,colorway:"primary",variant:"default",modalHeadingText:`Upgrade to Replit ${t.corePlanName}`,redirectPath:"/home"})]})};e.s(["PlanUsageMonitorUI",0,U,"default",0,()=>{let e,t,s=(0,a.useReplLimit)(),o="loading"===s.type,{agentUsage:c,agentUsageV2:u,loading:d}=(0,l.useGetAgentFreeUsage)(),{cloudUsage:p,loading:g}=(0,n.useGetCloudFreeUsage)(),m="data"===s.type?s.replCount:0,x=m/("data"===s.type?s.starterPlanReplLimit:i.STARTER_PLAN_REPL_LIMIT);return u?(e=u.usage,t=u.limit):(e=c?.usage,t=c?.limit),(0,r.jsx)(U,{agentUsage:{usage:e,limit:t,loading:d},publicRepls:m,replsLimitLoading:o,showReplsLimit:x>=.25,cloudUsage:{usage:p?.usage,limit:p?.limit,loading:g}})}],765269)},748538,e=>{"use strict";var r=e.i(973245),t=e.i(951262);let i={},s=r.gql`
    fragment EditReplFormRepl on Repl {
  id
  title
  description
  imageUrl
  iconUrl
  isPrivate
  owner {
    __typename
  }
  templateInfo {
    iconUrl
    imageUrl
  }
  authorizations {
    editMetadata {
      isAuthorized
      code
      message
    }
    editVisibility {
      isAuthorized
      code
      message
    }
  }
  org {
    id
    type
  }
}
    `,a=r.gql`
    mutation EditReplFormEdit($input: UpdateReplInput!) {
  updateRepl(input: $input) {
    repl {
      id
      ...EditReplFormRepl
    }
  }
}
    ${s}`;e.s(["EditReplFormReplFragmentDoc",0,s,"useEditReplFormEditMutation",0,function(e){let r={...i,...e};return t.useMutation(a,r)}])},781258,80593,e=>{"use strict";var r=e.i(973245),t=e.i(304277);e.i(566901);var i=e.i(951262);let s={},a=r.gql`
    fragment TransferReplToOrgDialogRepl on Repl {
  id
  title
  slug
  owner {
    ... on User {
      id
      username
    }
    ... on Team {
      id
      username
    }
  }
}
    `,l=r.gql`
    query TransferReplToOrgDialogOrgs {
  currentUser {
    id
    orgs(count: 30) {
      __typename
      ... on CurrentUserOrganizationConnection {
        items {
          org {
            id
            name
            slug
            image
            type
          }
          type
        }
      }
      ... on Error {
        message
      }
    }
  }
}
    `,n=r.gql`
    mutation TransferReplToOrgDialogTransfer($orgId: String!, $replIds: [String!]!) {
  transferReplToOrganization(input: {orgId: $orgId, replIds: $replIds}) {
    ... on TransferReplToOrganizationSuccess {
      runId
      results {
        replId
        success
        error
      }
      successCount
      errorCount
    }
    ... on UnauthorizedError {
      message
    }
    ... on UserError {
      message
    }
    ... on TooManyRequestsError {
      message
    }
  }
}
    `;e.s(["TransferReplToOrgDialogReplFragmentDoc",0,a,"useTransferReplToOrgDialogOrgsQuery",0,function(e){let r={...s,...e};return t.useQuery(l,r)},"useTransferReplToOrgDialogTransferMutation",0,function(e){let r={...s,...e};return i.useMutation(n,r)}],781258);let o={},c=r.gql`
    fragment LeaveMultiplayerReplDialogRepl on Repl {
  id
  title
}
    `,u=r.gql`
    mutation LeaveMultiplayerReplDialogRemove($id: String!) {
  removeSharedRepl(replId: $id) {
    id
  }
}
    `;e.s(["LeaveMultiplayerReplDialogReplFragmentDoc",0,c,"useLeaveMultiplayerReplDialogRemoveMutation",0,function(e){let r={...o,...e};return i.useMutation(u,r)}],80593)},145275,e=>{e.v({paginationRow:"IndexPagination-module__t95pHW__paginationRow",surface:"IndexPagination-module__t95pHW__surface"})},222826,e=>{"use strict";var r=e.i(276385),t=e.i(389959),i=e.i(656077),s=e.i(927600),a=e.i(269848),l=e.i(919073),n=e.i(488299),o=e.i(334353),c=e.i(8047),u=e.i(61732),d=e.i(145275);e.s(["default",0,({currentPage:e,pageSize:p,totalItems:g,goToNextPage:m,goToPreviousPage:x})=>{let{loading:h}=(0,t.useContext)(o.IndexContext),f=Math.max(Math.ceil(g/p),1),R=(0,t.useRef)(null),w=(0,t.useRef)(40);return(0,t.useLayoutEffect)(()=>{R.current&&(w.current=R.current.offsetHeight+1)},[R]),(0,r.jsx)(l.ShadesSurface,{clsx:d.default.surface,style:{minHeight:w.current},innerRef:R,elevate:!1,children:(0,r.jsx)(u.View,{clsx:d.default.paginationRow,row:!0,gap:8,p:8,align:"center",justify:"center",children:h?(0,r.jsx)(a.default,{}):(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(n.IconButton,{alt:"Previous page",disabled:0===e,onClick:x,children:(0,r.jsx)(i.default,{})}),(0,r.jsxs)(c.Text,{variant:"small",color:"dimmer",children:["Page ",e+1," of ",f]}),(0,r.jsx)(n.IconButton,{alt:"Next page",disabled:e>=f-1,onClick:m,children:(0,r.jsx)(s.default,{})})]})})})}])},906595,e=>{e.v({root:"ReplResult-module__xjVmeG__root"})},407617,e=>{"use strict";var r=e.i(276385),t=e.i(157630),i=e.i(389959),s=e.i(2001),a=e.i(595996),l=e.i(480028),n=e.i(61732),o=e.i(618457),c=e.i(921125),u=e.i(906595);let d=(0,l.cvarsFrom)("ReplResult.module.css",["--height"]);function p({repl:e,height:l,isActive:g,searchQuery:m}){let{title:x}=e,h=(0,i.useMemo)(()=>m?s.default.match(m,x):null,[m,x]);return(0,r.jsx)(t.default,{...(0,c.replLinkProps)(e),children:(0,r.jsxs)(n.View,{clsx:u.default.root,row:!0,gap:6,px:6,style:{[d.height]:l+"px"},align:"center",children:[(0,r.jsx)(a.default,{alt:e.title,size:32,iconUrl:e.iconUrl}),(0,r.jsx)(n.View,{grow:!0,shrink:!0,gap:2,translate:"no",children:(0,r.jsx)(o.HighlightMatches,{text:e.title,highlight:h?.ranges,dimmed:!g})})]})})}e.s(["ReplResult",0,p,"toReplResult",0,function(e,t,i){var s,l;return{match:(s=e,l=t,()=>({score:1,render:{height:44,content:(0,r.jsx)(p,{repl:l,height:44,searchQuery:s})}})),data:{type:"action",label:t.title,icon:(0,r.jsx)(a.default,{alt:t.title,size:16,iconUrl:t.iconUrl}),run:()=>i(t)}}}])},877925,e=>{e.v({clickable:"PromoCard-module__J8rxZW__clickable",subtitle:"PromoCard-module__J8rxZW__subtitle",title:"PromoCard-module__J8rxZW__title"})},121668,e=>{"use strict";var r=e.i(276385),t=e.i(336187),i=e.i(406664),s=e.i(919073),a=e.i(8047),l=e.i(61732),n=e.i(877925);function o({title:e,label:i}){return(0,r.jsxs)(l.View,{gap:4,px:16,py:12,children:[(0,r.jsxs)(l.View,{row:!0,align:"center",gap:6,children:[(0,r.jsx)(t.default,{size:16}),(0,r.jsx)(a.Text,{clsx:n.default.title,children:e})]}),(0,r.jsx)(a.Text,{clsx:n.default.subtitle,children:i})]})}function c({title:e,label:t,onClick:a}){let l=(0,i.useCreateInteractive)({variant:"nofill"});return(0,r.jsx)(s.ShadesSurface,{tag:"button",type:"button",colorShade:"themeNotice",elevate:"2x",border:"subtle",br:8,clsx:[l.clsx,n.default.clickable],style:l.style,onClick:a,children:(0,r.jsx)(o,{title:e,label:t})})}e.s(["PromoCard",0,function({onClick:e,title:t,label:i}){return e?(0,r.jsx)(c,{title:t,label:i,onClick:e}):(0,r.jsx)(s.ShadesSurface,{colorShade:"themeNotice",elevate:"2x",border:"subtle",br:8,children:(0,r.jsx)(o,{title:t,label:i})})}])},33602,e=>{"use strict";var r,t=e.i(908796),i=e.i(462229),s=e.i(691636),a=e.i(127384);let l=(0,i.cssRecord)({pageHeader:[s.rcss.flex.row,s.rcss.justify.spaceBetween,s.rcss.align.center],pageHeaderOrgName:[s.rcss.maxWidth(240)],pageHeaderActions:[s.rcss.rowWithGap(8),s.rcss.align.center],pageTitle:[s.rcss.rowWithGap(8),s.rcss.align.center,s.rcss.flex.growAndShrink(1)],pageTitleText:[s.rcss.maxWidth("100%"),s.rcss.flex.growAndShrink(1)],pageContent:[s.rcss.colWithGap(32)],pageSection:[s.rcss.colWithGap(12)],pageSidebarOffset:[{paddingLeft:a.SIDEBAR_WIDTH}],sidebarSectionHeaderText:[s.rcss.p(8),s.rcss.px(16),{fontWeight:500}],indexTableWrapper:[s.rcss.display.flex,s.rcss.position.relative,s.rcss.justify.spaceBetween,s.rcss.overflow("auto"),s.rcss.width("100%")],onboardingSurface:[s.rcss.p(12),s.rcss.borderRadius(),s.rcss.border()],tooltipWrapper:[s.rcss.rowWithGap(8),s.rcss.align.center],searchBar:[s.rcss.maxWidth(400)]});t.SystemOrgGroupType.SystemAdmins,t.SystemOrgGroupType.SystemMembers,t.SystemOrgGroupType.SystemGuests;var n=((r={}).Index="Index",r.OrgGroup="OrgGroup",r);e.s(["NUM_ORGS_PER_PAGE",0,20,"SidebarType",()=>n,"orgStyles",0,l,"sortSystemGroups",0,e=>[t.Org_GroupstypeEnumType.SystemAdmins,t.Org_GroupstypeEnumType.SystemMembers,t.Org_GroupstypeEnumType.SystemGuests].reduce((r,t)=>{let i=e.find(e=>e.type===t);return i&&r.push(i),r},[])])}]);

//# debugId=8d0314da-df6f-63ba-7c27-40377bed923a
//# sourceMappingURL=0hee.f_r9uw~z.js.map
