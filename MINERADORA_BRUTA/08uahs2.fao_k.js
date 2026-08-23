;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="ca47ec81-97c0-d303-efbb-222805c63c0c")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,767025,e=>{e.v({highlight:"OrgGroupSearch-module__tfaGqG__highlight"})},959787,e=>{"use strict";var t=e.i(276385),r=e.i(389959),i=e.i(162372),a=e.i(908796),l=e.i(973245),n=e.i(130902),o=e.i(304277);e.i(566901);let s={},u=l.gql`
    query OrgGroupSearch($orgId: String, $input: OrgGroupsInput) {
  currentUser {
    __typename
    id
    org(orgId: $orgId) {
      __typename
      ... on Org {
        id
        groups(input: $input) {
          __typename
          ... on OrgGroupConnection {
            pageInfo {
              hasNextPage
              nextCursor
            }
            items {
              ...OrgGroupsOrgGroup
            }
          }
          ... on UserError {
            message
          }
        }
      }
      ... on NotFoundError {
        message
      }
    }
  }
}
    ${n.OrgGroupsOrgGroupFragmentDoc}`;var d=e.i(602686),c=e.i(269848),p=e.i(346781),g=e.i(612343),m=e.i(619158),f=e.i(480028),h=e.i(462229),x=e.i(691636),v=e.i(825419),w=e.i(488299),y=e.i(528710),j=e.i(108431),b=e.i(8047),R=e.i(61732),I=e.i(767025);let _=[x.rcss.p(8),x.rcss.cursor.pointer],S=(0,h.cssRecord)({container:[x.rcss.position.relative],rightIcon:[x.rcss.position.absolute,x.rcss.right(8),x.rcss.top("50%"),{transform:"translateY(-50%)"}],dropdownMenu:[x.rcss.width("100%"),x.rcss.position.absolute,x.rcss.zIndex(1),x.rcss.top("100%"),x.rcss.left(0),x.rcss.backgroundColor.backgroundDefault,x.rcss.maxHeight(300),x.rcss.overflow("auto"),x.rcss.borderRadius(4),x.rcss.border({color:f.tokens.foregroundDimmest}),{borderTop:"0 none"}],result:[..._],activeResult:[..._,x.rcss.backgroundColor.accentPrimaryDimmer],closeIconButton:[{"&:hover":{backgroundColor:`${f.tokens.backgroundHighest} !important`}}],userMultiplayerIcon:[x.rcss.backgroundColor.outlineDimmest,x.rcss.borderRadius(4)],userDisplayName:[x.rcss.fontWeight.medium]}),F=({text:e,highlight:r})=>{if(!r)return(0,t.jsx)(t.Fragment,{children:e});let i=r.replace(/[.*+?^${}()|[\]\\]/g,"\\$&"),a=e.split(RegExp(`(${i})`,"gi"));return(0,t.jsx)(t.Fragment,{children:a.map((e,i)=>e.toLowerCase()===r.toLowerCase()?(0,t.jsx)("span",{clsx:I.default.highlight,children:e},i):(0,t.jsx)("span",{children:e},i))})},T=({individualMember:e,searchQuery:r})=>{let i=e?.user;if(!i)return null;let a=e?.user?.displayName??"",l=e?.email??"";return(0,t.jsxs)(R.View,{row:!0,gap:8,align:"center",children:[(0,t.jsx)(v.Avatar,{size:24,src:i?.image,username:`${i?.displayName}`,fullName:i?.fullName}),(0,t.jsxs)(b.Text,{children:[(0,t.jsx)(F,{text:a,highlight:r})," (",(0,t.jsx)(F,{text:l,highlight:r}),")"]})]})},C=e=>e?e.type===a.OrgGroupType.SystemIndividual?e.individualMember?.email||e.name:e.name||"":"";e.s(["default",0,({inputId:e,orgId:l,types:n,selectedGroups:f,value:h,setValue:x,onSelect:v,onClear:I,placeholder:_="Find an existing group...",hideSearchIcon:F=!1,hideEmptyResults:D=!1})=>{var A;let k,[U,E]=(0,r.useState)([]),O=(0,m.default)(h.trim(),250),{data:P,loading:z,error:V}=(A={variables:{orgId:l,input:{count:10,types:n,filters:{name:{search:O}}}},ssr:!1,skip:!O,fetchPolicy:"cache-and-network",onCompleted:e=>{e?.currentUser?.org?.__typename!=="Org"||e?.currentUser?.org?.groups?.__typename!=="OrgGroupConnection"||E(e.currentUser.org.groups.items.filter(e=>!f.some(t=>e.id===t.id)))}},k={...s,...A},o.useQuery(u,k)),B=P&&P.currentUser&&"Org"!==P.currentUser.org.__typename?P.currentUser.org.message:void 0,L=P&&P.currentUser&&"Org"===P.currentUser.org.__typename&&"OrgGroupConnection"!==P.currentUser.org.groups.__typename?P.currentUser.org.groups.message:void 0,$=V?.message,M=B??L??$;return(0,r.useEffect)(()=>{0===h.length&&0!==U.length&&E([])},[h.length,U.length]),(0,t.jsx)(R.View,{css:S.container,children:(0,t.jsx)(i.default,{onSelect:e=>{e&&(v(e),x(C(e)))},itemToString:e=>C(e),initialHighlightedIndex:0,defaultHighlightedIndex:0,children:({getInputProps:r,getItemProps:i,getMenuProps:l,isOpen:n,highlightedIndex:o,getRootProps:s})=>(0,t.jsxs)(R.View,{...s({refKey:"innerRef"}),children:[(0,t.jsx)(y.Input,{...r({id:e,ref:null,value:h,onChange:e=>{x(e.currentTarget.value)},placeholder:_,autoComplete:"off"})}),z||0!==h.length||F?null:(0,t.jsx)(p.default,{css:S.rightIcon}),z?(0,t.jsx)(R.View,{css:S.rightIcon,children:(0,t.jsx)(c.default,{})}):null,!z&&h.length>0?(0,t.jsx)(R.View,{css:S.rightIcon,children:(0,t.jsx)(w.IconButton,{css:S.closeIconButton,alt:"Clear",tooltipBehavior:"hidden",onClick:()=>{x(""),I&&I()},children:(0,t.jsx)(d.default,{})})}):null,(0,t.jsxs)(R.View,{tag:"ul",...l({refKey:"innerRef"}),children:[M?(0,t.jsx)(R.View,{tag:"ul",css:S.dropdownMenu,children:(0,t.jsx)(R.View,{tag:"li",css:S.result,children:(0,t.jsx)(j.StatusBanner,{colorway:"negative",text:M})})}):null,n&&U&&U.length?(0,t.jsx)(R.View,{css:S.dropdownMenu,p:4,children:U.map((e,r)=>(0,t.jsx)(R.View,{tag:"li",...i({item:e,index:r}),css:r===o?S.activeResult:S.result,children:e.type===a.OrgGroupType.SystemIndividual?(0,t.jsx)(T,{individualMember:e.individualMember,searchQuery:O}):(0,t.jsxs)(R.View,{row:!0,gap:8,align:"center",children:[(0,t.jsx)(R.View,{css:S.userMultiplayerIcon,p:6,children:(0,t.jsx)(g.default,{size:12})}),(0,t.jsx)(b.Text,{height:"singleLine",multiline:!1,css:S.userDisplayName,children:e.name})]})},e.id))}):null,!D&&n&&!z&&O.length>0&&0===U.length?(0,t.jsx)(R.View,{tag:"ul",css:S.dropdownMenu,children:(0,t.jsx)(R.View,{tag:"li",css:S.result,children:(0,t.jsxs)(b.Text,{height:"singleLine",color:"dimmer",multiline:!1,children:['No results found for "',h,'"']})})}):null]})]})})})}],959787)},453891,e=>{"use strict";var t=e.i(969407),r=e.i(908796),i=e.i(379334),a=e.i(768773);e.s(["useDeploymentLink",0,function(e){let l=(0,t.useIsSSR)(),n=e?.currentBuild?.provider;if(!e||!n)return{href:"",displayUrl:""};let o=!l&&window.location.hostname.endsWith("rp-humain.com");if(n===r.HostingBuildProvider.DatabricksApp)return{href:"",displayUrl:""};let s=!l&&"replit.com"!==window.location.hostname&&!o,u=`${e.replitAppSubdomain}${(0,a.getProviderInternalDomain)({provider:n,flaggedInternalDomain:o?i.HUMAIN_DEPLOYMENTS_DOMAIN:i.DEPLOYMENTS_DEFAULT_DOMAIN,isStaging:s})}`,d=e.domains2?.find(e=>e.state===r.HostingDeploymentDomainState.Verified)??null;return d?{href:`https://${d.domain}`,displayUrl:d.domain}:{href:`https://${u}`,displayUrl:u}}])},131344,e=>{"use strict";var t=e.i(276385),r=e.i(269848),i=e.i(643484),a=e.i(8047),l=e.i(61732);let n=l.SpecializedView.form;e.s(["default",0,function(e){return(0,t.jsxs)(n,{gap:24,onSubmit:t=>{t.preventDefault(),e.onConfirm()},children:[(0,t.jsx)(a.Header,{variant:"headerDefault",level:2,children:e.title}),"string"==typeof e.children?(0,t.jsx)(a.Text,{children:e.children}):e.children,(0,t.jsxs)(l.View,{row:!0,gap:12,justify:"end",children:[(0,t.jsx)(i.Button,{type:"button",onClick:e.onCancel,text:e.cancelLabel??"Cancel"}),(0,t.jsx)(i.Button,{type:"submit",disabled:e.loading,iconLeft:e.loading?(0,t.jsx)(r.default,{}):e.confirmIcon,colorway:e.isDestructive?"negative":"primary",text:e.confirmLabel||"Confirm"})]})]})}])},345219,66083,e=>{"use strict";var t,r=e.i(871752),i=((t=i||{}).ArrayBuffer="ARRAY_BUFFER",t.BinaryString="BINARY_STRING",t.DataURL="DATA_URL",t.Text="TEXT",t);let a=(e,t)=>e instanceof window.File?new Promise((r,i)=>{let a=new window.FileReader;switch(a.onload=t=>{t.target?.result?r(t.target.result):i(Error(`Failed to read file "${e.name}"`))},a.onerror=i,t){case"ARRAY_BUFFER":a.readAsArrayBuffer(e);break;case"BINARY_STRING":a.readAsBinaryString(e);break;case"DATA_URL":a.readAsDataURL(e);break;case"TEXT":a.readAsText(e)}}):Promise.all(Array.from(e).filter(e=>!!e).map(e=>a(e,t))),l=e=>a(e,"DATA_URL");async function n(e){let t=await l(e);if(e.size>1e7)throw Error("This image is over the 10MB maximum");if(!t)throw Error("Expected file");return t}async function o(e,t){return await (0,r.postJson)("/data/images/upload",{image:e,context:t})}e.s(["readFileAsArrayBuffer",0,e=>a(e,"ARRAY_BUFFER"),"readFileAsDataURL",0,l],66083),e.s(["ACCEPTABLE_IMAGE_UPLOAD_TYPES",0,["image/png","image/jpeg","image/gif","image/webp"],"UPLOAD_LIMIT_BYTES",0,1e7,"postImage",0,o,"readImageAsDataURL",0,n],345219)},349597,956264,e=>{"use strict";var t,r=((t={}).AdminTutorialUpdate="admin-tutorial-update",t.CommunityPost="community-post",t.ProfileImage="profile-image",t.ProfileCoverImage="profile-cover-image",t.OrgProfileImage="org-profile-image",t.TemplateIcon="template-icon",t.ReplIcon="repl-icon",t.ReplCoverImage="repl-cover-image",t.TrainingProfileImage="training-profile-image",t.AgentInboxLogo="agent-inbox-logo",t);e.s(["DEFAULT_REPL_ICON",0,"https://icons-util.replit.app/C:/IOTEC/_SANITIZADA/bash.svg","ImageUploadContexts",()=>r],349597);var i=e.i(389959),a=e.i(345219);e.s(["default",0,function({onUploadPreview:e,onUpload:t,onError:r}){let[l,n]=(0,i.useState)(!1);return{isLoading:l,uploadImage:(0,i.useCallback)(async(i,l)=>{let o;if(n(!0),"image/svg+xml"===i.type)return r(Error("SVG images are not allowed")),!1;try{o=await (0,a.readImageAsDataURL)(i)}catch(e){return r(Error(`This image is over the ${a.UPLOAD_LIMIT_BYTES/1e6}MB maximum`)),!1}e({dataUrl:o});let s=null;try{s=await (0,a.postImage)(o,l)}catch(i){let t="Something went wrong";return t=i.message.toLowerCase().includes("entity too large")?"This image is over the 1MB maximum":i.message,e({dataUrl:""}),n(!1),r(Error(t)),!1}let{id:u,url:d}=s;if("number"!=typeof u)throw Error("Expected id");if("string"!=typeof d)throw Error("Expected url");n(!1);try{await t({id:u,url:d})}catch(e){return r(e),!1}return!0},[r,t,e])}}],956264)},924325,e=>{"use strict";var t=e.i(276385),r=e.i(269848),i=e.i(491194),a=e.i(643484),l=e.i(8047),n=e.i(61732);e.s(["default",0,e=>(0,t.jsxs)(n.View,{gap:24,children:[(0,t.jsxs)(l.Header,{variant:"headerDefault",level:2,children:["Delete ",e.name||e.entityType,"?"]}),(0,t.jsxs)(n.View,{gap:8,children:[(0,t.jsxs)(l.Text,{children:["Are you sure you want to delete"," ",e.description?e.description:`this ${e.entityType}`,"? This cannot be undone."]}),"App"===e.entityType?(0,t.jsx)(l.Text,{children:"Some Apps may take a few minutes to finish deleting."}):null]}),(0,t.jsxs)(n.View,{row:!0,gap:12,justify:"end",children:[(0,t.jsx)(a.Button,{text:"Cancel",onClick:e.hideModal}),(0,t.jsx)(a.Button,{dataCy:"delete-modal-confirm-button",disabled:e.isDeleting,iconLeft:e.isDeleting?(0,t.jsx)(r.default,{}):(0,t.jsx)(i.default,{}),onClick:()=>{e.delete(),e.hideModal()},text:`Yes, delete ${e.confirmDescription?e.confirmDescription:`this ${e.entityType}`}`,colorway:"negative"})]})]})])},750866,e=>{e.v({imageSurface:"ReplCoverImageIcon-module__ZOl4NW__imageSurface"})},300881,e=>{e.v({titleTimeWrapper:"OrgFeaturedRepls-module__5pNb7W__titleTimeWrapper"})},627184,761843,e=>{"use strict";var t=e.i(276385),r=e.i(413974),i=e.i(898039),a=e.i(50814),l=e.i(389959),n=e.i(983420),o=e.i(919073),s=e.i(727223),u=e.i(750866);function d({width:e,height:r,alt:i,imageUrl:a,style:c}){let p=(0,l.useContext)(n.IconContext),{width:g=p.size??32,height:m=p.size??32,alt:f=p.alt??""}={width:e,height:r,alt:i},h=g<32?4:8;return(0,t.jsx)(o.ShadesSurface,{clsx:u.default.imageSurface,style:{borderRadius:h,width:g,height:m,...c},p:8,children:(0,t.jsx)(s.default,{alt:f,src:a,width:g,height:m,objectFit:"contain"})})}e.s(["default",0,d],761843);var c=e.i(967629),p=e.i(480028),g=e.i(462229),m=e.i(723517),f=e.i(691636),h=e.i(643484),x=e.i(8047),v=e.i(61732),w=e.i(183555),y=e.i(365757),j=e.i(300881);let b=({repl:e,hideForkButton:l})=>{let n=(0,w.useForkContext)(),{title:s,description:u,iconUrl:c,timeUpdated:p,publicForkCount:g,url:m}=e,f=`${m}/view`;return(0,t.jsxs)(o.ShadesSurface,{css:I.featureCardWrapper,tabIndex:-1,elevate:!1,children:[(0,t.jsx)(v.View,{css:I.imageWrapper,children:(0,t.jsx)(d,{alt:e.title,imageUrl:e.imageUrl??e.templateInfo?.imageUrl,width:135,height:135,style:{borderRadius:"4px 0px 0px 4px"}})}),(0,t.jsxs)(v.View,{css:I.detailsColumn,grow:!0,shrink:!0,children:[(0,t.jsxs)(v.View,{grow:!0,pt:8,row:!0,align:"start",justify:"space-between",children:[(0,t.jsx)(r.default,{href:f,css:_.link,target:"_blank",children:(0,t.jsxs)(v.View,{css:I.titleWithIcon,grow:!0,shrink:!0,row:!0,gap:12,align:"center",children:[(0,t.jsx)(y.default,{surface:!0,alt:s,size:32,iconUrl:c}),(0,t.jsxs)(v.View,{shrink:!0,clsx:j.default.titleTimeWrapper,children:[(0,t.jsx)(x.Text,{variant:"headerDefault",color:"default",multiline:!1,children:s}),(0,t.jsxs)(x.Text,{variant:"small",color:"dimmest",multiline:!1,children:["Updated ",(0,a.ago)(p)]})]})]})}),l?null:(0,t.jsxs)(v.View,{css:I.forkCount,pt:8,row:!0,gap:8,align:"center",children:[(0,t.jsx)(v.View,{children:g}),(0,t.jsx)(h.Button,{className:"forkButton",variant:"nofill",css:I.forkButton,text:n.isForking?"Remixing...":"Remix",isDisabled:n.isForking,onClick:()=>{n.isForking||n.fork()},disabled:n.isForking,iconLeft:(0,t.jsx)(i.default,{})})]})]}),(0,t.jsx)(v.View,{grow:2,children:(0,t.jsx)(x.Text,{color:"dimmer",maxLines:2,children:u})})]})]})},R=(0,c.css)({"::after":{borderRadius:p.tokens.space8,content:'""',position:"absolute",top:0,right:0,bottom:0,left:0,display:"block",zIndex:1}}),I=(0,g.cssRecord)({featureCardWrapper:[f.rcss.position.relative,f.rcss.rowWithGap(16),f.rcss.height(135),f.rcss.overflow("hidden"),m.interactive.filledAndOutlined,f.rcss.pr(16),{width:"100%"}],detailsColumn:[{width:"100%"}],titleWithIcon:[f.rcss.minWidth(0),f.rcss.mr(8)],forkCount:[f.rcss.color.foregroundDimmer],forkButton:[f.rcss.zIndex(2),f.rcss.hover({backgroundColor:p.tokens.interactiveBackgroundActive})],imageWrapper:[f.rcss.width(135),{[f.media.max(550)]:[f.rcss.width(110)]}]}),_=(0,g.cssRecord)({link:[R,f.rcss.focusRingOnAfter,f.rcss.flex.growAndShrink(1),f.rcss.minWidth(0)]});e.s(["FeaturedReplCard",0,b,"default",0,({featuredRepls:e})=>e?(0,t.jsxs)(v.View,{gap:8,children:[(0,t.jsx)(x.Text,{variant:"subheadBig",color:"default",children:"Featured Apps"}),(0,t.jsx)(v.View,{gap:16,children:e.items.map((e,r)=>(0,t.jsx)(w.ForkContextProvider,{forkParams:{trackingData:{forkSource:"orgFeaturedRepl"}},repl:e.repl,children:(0,t.jsx)(b,{repl:e.repl,index:r})},e.repl.id))})]}):null],627184)},56233,e=>{"use strict";var t=e.i(973245);let r=t.gql`
    fragment ReplListBoxItemRepl on Repl {
  id
  title
  iconUrl
  isFeaturedRepl
  description(plainText: true)
}
    `;var i=e.i(951262),a=e.i(304277);e.i(566901);let l={},n=t.gql`
    fragment OrgFeaturedReplsSearchReplItem on Repl {
  __typename
  id
  ...ReplListBoxItemRepl
  org {
    id
  }
}
    ${r}`,o=t.gql`
    fragment OrgFeaturedReplsSearchInputRepls on ReplConnection {
  items {
    ...OrgFeaturedReplsSearchReplItem
  }
  pageInfo {
    hasNextPage
    nextCursor
  }
}
    ${n}`,s=t.gql`
    mutation OrgFeaturedReplsUpdate($input: UpdateOrgFeaturedReplInput!) {
  updateOrgFeaturedRepl(input: $input) {
    ... on Org {
      id
      __typename
      featuredRepls {
        __typename
        ... on OrgFeaturedReplConnection {
          items {
            repl {
              ...OrgFeaturedReplsSearchReplItem
            }
          }
        }
      }
    }
    ... on Error {
      __typename
      message
    }
  }
}
    ${n}`,u=t.gql`
    mutation OrgFeaturedReplsDelete($input: RemoveOrgFeaturedReplInput!) {
  removeOrgFeaturedRepl(input: $input) {
    ... on Org {
      id
      __typename
      featuredRepls {
        __typename
        ... on OrgFeaturedReplConnection {
          items {
            repl {
              ...OrgFeaturedReplsSearchReplItem
            }
          }
        }
      }
    }
    ... on Error {
      __typename
      message
    }
  }
}
    ${n}`,d=t.gql`
    query OrgFeaturedReplsSearchInputList($searchTerm: String!, $orgId: String!, $cursor: String) {
  currentUser {
    __typename
    id
    org(orgId: $orgId) {
      __typename
      ... on Org {
        id
        repls(
          input: {filters: {title: {search: $searchTerm}, visibility: public}, cursor: $cursor}
        ) {
          __typename
          ... on ReplConnection {
            ...OrgFeaturedReplsSearchInputRepls
          }
          ... on UserError {
            message
          }
        }
      }
      ... on NotFoundError {
        message
      }
    }
  }
}
    ${o}`;e.s(["useOrgFeaturedReplsDeleteMutation",0,function(e){let t={...l,...e};return i.useMutation(u,t)},"useOrgFeaturedReplsSearchInputListQuery",0,function(e){let t={...l,...e};return a.useQuery(d,t)},"useOrgFeaturedReplsUpdateMutation",0,function(e){let t={...l,...e};return i.useMutation(s,t)}],56233)},464804,e=>{"use strict";var t=e.i(973245);let r=t.gql`
    fragment FeaturedReplCardRepl on Repl {
  id
  title
  description
  iconUrl
  timeUpdated
  imageUrl
  url
  templateInfo {
    imageUrl
  }
  publicForkCount
}
    `;e.i(304277);var i=e.i(566901);let a={},l=t.gql`
    fragment FeaturedReplPreviewRepl on Repl {
  id
  ...FeaturedReplCardRepl
}
    ${r}`,n=t.gql`
    query FeaturedReplPreviewReplInfo($replId: String!) {
  getRepl(id: $replId) {
    ... on Repl {
      id
      isFeaturedRepl
    }
  }
}
    `;e.s(["FeaturedReplPreviewReplFragmentDoc",0,l,"useFeaturedReplPreviewReplInfoLazyQuery",0,function(e){let t={...a,...e};return i.useLazyQuery(n,t)}],464804)},934174,e=>{"use strict";var t=e.i(276385),r=e.i(464804),i=e.i(56233),a=e.i(320216),l=e.i(627184),n=e.i(643484),o=e.i(8047),s=e.i(61732);e.s(["default",0,({isFeatured:e,repl:u,orgId:d,onCompleted:c})=>{let{showError:p,showConfirm:g}=(0,a.default)(),[m,{loading:f}]=(0,i.useOrgFeaturedReplsUpdateMutation)({onError:()=>{p("Something unexpected happened")},onCompleted:e=>{"Org"===e.updateOrgFeaturedRepl.__typename?(g("Profile updated successfully"),v()):p(e.updateOrgFeaturedRepl.message)}}),[h,{loading:x}]=(0,i.useOrgFeaturedReplsDeleteMutation)({onError:()=>{p("Something unexpected happened")},onCompleted:e=>{"Org"===e.removeOrgFeaturedRepl.__typename?(g("Removed featured App"),v()):p(e.removeOrgFeaturedRepl.message)}}),[v]=(0,r.useFeaturedReplPreviewReplInfoLazyQuery)({variables:{replId:u.id},fetchPolicy:"network-only",ssr:!1});return d?(0,t.jsxs)(s.View,{justify:"center",gap:16,children:[(0,t.jsx)(o.Text,{variant:"headerDefault",children:e?"Remove from featured repls":"Feature App on your profile"}),(0,t.jsx)(o.Text,{variant:"text",children:e?"Do you want to remove this App from the Featured section?":"Display this App at the top of your workspace's profile. Only public Apps can be featured."}),(0,t.jsx)(l.FeaturedReplCard,{repl:u,index:0,hideForkButton:!0}),(0,t.jsxs)(s.View,{row:!0,justify:"space-between",align:"center",children:[(0,t.jsx)(n.Button,{text:"Cancel",onClick:c}),(0,t.jsx)(n.Button,{colorway:"primary",text:e?"Remove":"Feature on profile",onClick:()=>{e?h({variables:{input:{orgId:d,replId:u.id}}}):m({variables:{input:{orgId:d,replId:u.id}}}),c()},loading:f||x})]})]}):null}])},334938,729422,e=>{"use strict";var t=e.i(932200),r=e.i(2800),i=e.i(248033),a=e.i(493800),l=e.i(167768),n=e.i(138715),o=e.i(99906),s=e.i(278052),u=e.i(434080),d=e.i(593678),c=e.i(352019),p=e.i(389959),g=e.i(48309);let m=new Map;function f(e,t){let r=m.get(e);if(!r){let t=new Set,i=e=>{for(let r of t)r(e)};r={listener:i,handlers:t},m.set(e,r),document.addEventListener(e,i)}return r.handlers.add(t),()=>{r.handlers.delete(t),0===r.handlers.size&&(document.removeEventListener(e,r.listener),m.delete(e))}}var h=e.i(624071),x=e.i(330666),v=e.i(649239),w=e.i(780673),y=e.i(58646),j=e.i(716768),b=e.i(896346);let R=(0,p.createContext)(null),I=(0,p.forwardRef)(function(e,m){var I;let{isDisabled:_=!1}=e;[e,m]=(0,t.useContextProps)(e,m,R);let S=(0,v.useObjectRef)(m),F=(0,p.useRef)(null),{dropProps:T,dropButtonProps:C,isDropTarget:D}=(0,a.useDrop)({...e,ref:F,hasDropButton:!0}),{buttonProps:A}=(0,l.useButton)(C||{},F),{hoverProps:k,isHovered:U}=(0,n.useHover)(e),{focusProps:E,isFocused:O,isFocusVisible:P}=(0,o.useFocusRing)(),z=(0,s.useLocalizedStringFormatter)((I=r.default)&&I.__esModule?I.default:I,"react-aria-components"),V=(0,w.useSlotId)(),B=e["aria-label"]||z.format("dropzoneLabel"),L=[V,e["aria-labelledby"]].filter(Boolean).join(" "),$=(0,y.useLabels)({"aria-label":B,"aria-labelledby":L}),{clipboardProps:M}=function(e){let{isDisabled:t}=e,r=(0,p.useRef)(!1),{focusProps:i}=(0,g.useFocus)({onFocusChange:e=>{r.current=e}}),a=(0,d.useEffectEvent)(t=>{r.current&&e.getItems&&t.preventDefault()}),l=(0,d.useEffectEvent)(t=>{if(r.current&&e.getItems&&(t.preventDefault(),t.clipboardData)){var i;(0,u.writeToDataTransfer)(t.clipboardData,e.getItems({action:"copy"})),null==(i=e.onCopy)||i.call(e)}}),n=(0,d.useEffectEvent)(t=>{r.current&&e.onCut&&e.getItems&&t.preventDefault()}),o=(0,d.useEffectEvent)(t=>{r.current&&e.onCut&&e.getItems&&(t.preventDefault(),t.clipboardData&&((0,u.writeToDataTransfer)(t.clipboardData,e.getItems({action:"cut"})),e.onCut()))}),s=(0,d.useEffectEvent)(t=>{r.current&&e.onPaste&&t.preventDefault()}),m=(0,d.useEffectEvent)(t=>{if(r.current&&e.onPaste&&(t.preventDefault(),t.clipboardData)){let r=(0,u.readFromDataTransfer)(t.clipboardData);e.onPaste(r)}});return(0,p.useEffect)(()=>{if(!t)return(0,c.chain)(f("beforecopy",a),f("copy",l),f("beforecut",n),f("cut",o),f("beforepaste",s),f("paste",m))},[t,a,l,n,o,s,m]),{clipboardProps:i}}({isDisabled:_,onPaste:t=>{var r;return null==(r=e.onDrop)?void 0:r.call(e,{type:"drop",items:t,x:0,y:0,dropOperation:"copy"})}}),G=(0,t.useRenderProps)({...e,values:{isHovered:U,isFocused:O,isFocusVisible:P,isDropTarget:D,isDisabled:_},defaultClassName:"react-aria-DropZone"}),N=(0,j.filterDOMProps)(e);return delete N.id,p.default.createElement(t.Provider,{values:[[i.TextContext,{id:V,slot:"label"}]]},p.default.createElement("div",{...(0,h.mergeProps)(T,k,N),...G,slot:e.slot||void 0,ref:S,onClick:e=>{var t,r;let i=e.target;for(;i&&(null==(t=S.current)?void 0:t.contains(i))&&!(0,b.isFocusable)(i);){if(i===S.current){null==(r=F.current)||r.focus();break}i=i.parentElement}},"data-hovered":U||void 0,"data-focused":O||void 0,"data-focus-visible":P||void 0,"data-drop-target":D||void 0,"data-disabled":_||void 0},p.default.createElement(x.VisuallyHidden,null,p.default.createElement("button",{...(0,h.mergeProps)(A,E,M,$),ref:F})),G.children))});e.s(["DropZone",0,I],334938);var _=e.i(964304),S=e.i(867711);let F=(0,p.forwardRef)(function(e,t){let{onSelect:r,acceptedFileTypes:i,allowsMultiple:a,defaultCamera:l,children:n,acceptDirectory:o,...s}=e,u=(0,v.useObjectRef)(t),d=(0,j.filterDOMProps)(s);return p.default.createElement(p.default.Fragment,null,p.default.createElement(S.PressResponder,{onPress:()=>{var e,t;(null==(e=u.current)?void 0:e.value)&&(u.current.value=""),null==(t=u.current)||t.click()}},n),p.default.createElement(_.Input,{...d,type:"file",ref:u,style:{display:"none"},accept:null==i?void 0:i.toString(),onChange:e=>null==r?void 0:r(e.target.files),capture:l,multiple:a,webkitdirectory:o?"":void 0}))});e.s(["FileTrigger",0,F],729422)},530118,e=>{e.v({dropZone:"FileUploadInput-module__Z2lIGa__dropZone"})},186416,e=>{"use strict";var t=e.i(276385),r=e.i(389959),i=e.i(334938),a=e.i(729422),l=e.i(530118);let n=(0,r.forwardRef)(function(e,r){return(0,t.jsx)(i.DropZone,{ref:r,...e,className:l.default.dropZone})});e.s(["FileUploadInput",0,({acceptedFileTypes:e,allowsMultiple:r=!1,acceptDirectory:i=!1,dropZoneDisabled:l=!1,children:o,onDrop:s,onSelect:u,...d})=>(0,t.jsx)(n,{onDrop:s,isDisabled:l,children:(0,t.jsx)(a.FileTrigger,{acceptedFileTypes:e,allowsMultiple:r,acceptDirectory:i,onSelect:u,...d,children:o})})])},50814,e=>{"use strict";var t=e.i(562782);let r={millisecond:1,second:1e3,minute:6e4,hour:36e5,day:864e5,week:6048e5,month:2592e6,year:31536e6},i={millisecond:"ms",month:"mo"};e.s(["ago",0,function(e,a=!1,l=3e4){let n=Math.round,o=" ago",s=function(e,r){if(a){let t=i[r]||r.substring(0,1);return`${e}${t}`}return`${(0,t.default)(r,e,!0)}${o}`},u=Date.now()-new Date(e).getTime();if(u<0&&(u*=-1,o=" from now"),l&&u<=l)return"now";let d="millisecond";for(let e in r){if(n(u)<r[e])return s(n(u/r[d]),d);d=e}return s(n(u/r.year),"year")}])},629443,e=>{e.v({clickableAvatar:"StackedAvatars-module__8Jz18q__clickableAvatar",countCircle:"StackedAvatars-module__8Jz18q__countCircle",overflowTrigger:"StackedAvatars-module__8Jz18q__overflowTrigger",root:"StackedAvatars-module__8Jz18q__root",tooltipText:"StackedAvatars-module__8Jz18q__tooltipText"})},565931,e=>{"use strict";var t=e.i(276385),r=e.i(480028),i=e.i(406664),a=e.i(919073),l=e.i(825419),n=e.i(643484),o=e.i(295231),s=e.i(244945),u=e.i(61732),d=e.i(629443);let c=(0,r.cvarsFrom)("StackedAvatars.module.css",["--size","--font-size","--tooltip-font-size"]),p={12:{fontSize:8,listGap:2,iconTextGap:2,tooltipAvatarSize:12,tooltipFontSize:8,borderPadding:1},16:{fontSize:10,listGap:2,iconTextGap:2,tooltipAvatarSize:16,tooltipFontSize:10,borderPadding:1},24:{fontSize:12,listGap:4,iconTextGap:4,tooltipAvatarSize:16,tooltipFontSize:12,borderPadding:2},32:{fontSize:14,listGap:4,iconTextGap:4,tooltipAvatarSize:16,tooltipFontSize:14,borderPadding:2},40:{fontSize:16,listGap:8,iconTextGap:4,tooltipAvatarSize:24,tooltipFontSize:14,borderPadding:2},48:{fontSize:24,listGap:8,iconTextGap:4,tooltipAvatarSize:24,tooltipFontSize:14,borderPadding:2}},g=e=>e.username;function m({user:e,size:r,borderPadding:i,onUserClick:n,getUserLabel:o}){let c=o(e),p=(0,t.jsx)(a.ShadesSurface,{elevate:!1,br:"full",p:i,children:(0,t.jsx)(l.Avatar,{size:r,src:e.image||null,username:e.username,fullName:e.fullName,backgroundColor:e.color})});return n?(0,t.jsx)(s.Tooltip,{tooltip:c,children:(r,i)=>(0,t.jsx)(u.View,{...r,innerRef:i,tag:"button",type:"button",clsx:d.default.clickableAvatar,onClick:()=>n(e),"aria-label":c,children:p})}):(0,t.jsx)(s.Tooltip,{tooltip:c,children:p})}function f({overflowUsers:e,overflowCount:r,size:c,tooltipListGap:g,tooltipIconTextGap:m,cssVarsStyles:h,zIndex:x,onUserClick:v,getUserLabel:w}){let y=(0,i.useCreateInteractive)({variant:"filled",borderRadius:"50%"});if(v){let i=`${r} more ${1===r?"user":"users"}`;return(0,t.jsx)(u.View,{align:"center",justify:"center",px:2,tag:"li",style:{zIndex:x},children:(0,t.jsx)(o.PopupMenu,{trigger:(0,t.jsxs)(n.BaseButton,{clsx:[d.default.overflowTrigger,d.default.countCircle,y.clsx],style:y.style,"aria-label":i,children:["+",r]}),"aria-label":i,placement:"bottom end",children:e.map(e=>(0,t.jsx)(o.BaseMenuItem,{id:e.id,textValue:w(e),onAction:()=>v(e),children:(0,t.jsxs)(u.View,{row:!0,gap:8,align:"center",children:[(0,t.jsx)(l.Avatar,{size:p[c]?.tooltipAvatarSize||c,src:e.image||null,username:e.username,fullName:e.fullName,backgroundColor:e.color}),(0,t.jsx)(u.View,{grow:!0,shrink:!0,children:w(e)})]})},e.id))})})}return(0,t.jsx)(s.Tooltip,{tooltip:(0,t.jsx)(u.View,{gap:g,style:h,children:e.map(e=>(0,t.jsxs)(u.View,{row:!0,gap:m,align:"center",children:[(0,t.jsx)(l.Avatar,{size:p[c]?.tooltipAvatarSize||c,src:e.image||null,username:e.username,fullName:e.fullName,backgroundColor:e.color}),(0,t.jsx)(u.View,{clsx:d.default.tooltipText,grow:!0,shrink:!0,children:w(e)})]},e.username))}),children:(e,i)=>(0,t.jsx)(u.View,{...e,innerRef:i,align:"center",justify:"center",px:2,tag:"li",style:{zIndex:x},children:(0,t.jsx)(a.ShadesSurface,{align:"center",justify:"center",clsx:d.default.countCircle,elevate:"2x",children:(0,t.jsxs)(u.View,{children:["+",r]})})})})}e.s(["default",0,function({activeUsers:e,visibleNumOfUsers:r=3,size:i=24,onUserClick:a,getUserLabel:l=g}){let n=e.length,o=p[i]?.listGap??8,s=p[i]?.iconTextGap??8,h=p[i]?.borderPadding??2,x=i+2*h,v={[c.size]:x+"px",[c.fontSize]:(p[i]?.fontSize??i)+"px",[c.tooltipFontSize]:(p[i]?.tooltipFontSize??14)+"px"},w=n>r,y=e.slice(0,w?r-1:r),j=w?e.slice(r-1):[];return(0,t.jsxs)(u.View,{tag:"ul",clsx:d.default.root,row:!0,style:v,children:[y.map((e,r)=>(0,t.jsx)(u.View,{tag:"li",style:{zIndex:r+1},children:(0,t.jsx)(m,{user:e,size:i,borderPadding:h,onUserClick:a,getUserLabel:l})},e.id)),w?(0,t.jsx)(f,{overflowUsers:j,overflowCount:n-r+1,size:i,tooltipListGap:o,tooltipIconTextGap:s,cssVarsStyles:v,zIndex:y.length,onUserClick:a,getUserLabel:l}):null]})}])},892158,e=>{"use strict";var t=e.i(276385),r=e.i(413974),i=e.i(389959),a=e.i(405411),l=e.i(983420),n=e.i(406664),o=e.i(480028),s=e.i(488299),u=e.i(61732),d=e.i(755021);let c=(0,o.cvarsFrom)("IconButton.module.css",["--size"]),p=u.SpecializedView.a,g=(0,i.forwardRef)(function({alt:e,children:i,colorway:a,disabled:o,size:u=s.defaultIconSize,as:g,href:m,prefetch:f,replace:h,scroll:x,shallow:v,className:w,dataCy:y,variant:j,filled:b,...R},I){let _=(0,n.useCreateInteractive)({variant:j??(b?"filled":"nofill"),colorway:a,disabled:o}),S={disabled:o,style:{[c.size]:u+"px",..._.style},clsx:[d.default.root,_.clsx],ref:I,...R},F=(0,t.jsx)(l.IconProvider,{alt:e,size:s.IconSizeMap[u],children:i});return o?(0,t.jsx)(p,{"data-cy":y,"aria-disabled":o,className:w,role:"link",...S,children:F}):(0,t.jsx)(r.default,{"data-cy":y,className:w,role:"link",as:g,href:m,prefetch:f,replace:h,scroll:x,shallow:v,...S,children:F})}),m=(0,i.forwardRef)(function({alt:e,tooltipBehavior:r,tooltipPlacement:i,tooltipContents:l,...n},o){return(0,t.jsxs)(a.TooltipTrigger,{isDisabled:"hidden"===r,children:[(0,t.jsx)(g,{alt:e,ref:o,...n}),(0,t.jsx)(s.IconButtonTooltip,{placement:i,children:l??e})]})});e.s(["IconButtonLink",0,m])},545757,e=>{e.v({button:"ReplIconInput-module__Mwm2NG__button"})},399997,e=>{"use strict";var t=e.i(276385),r=e.i(389959),i=e.i(973245),a=e.i(951262);let l={},n=i.gql`
    mutation ReplIconUpdate($input: UpdateReplInput!) {
  updateRepl(input: $input) {
    repl {
      id
      iconUrl
    }
  }
}
    `;var o=e.i(349597),s=e.i(956264),u=e.i(320216),d=e.i(345219),c=e.i(766299),p=e.i(643484),g=e.i(186416),m=e.i(8047),f=e.i(244945),h=e.i(61732),x=e.i(365757),v=e.i(545757);e.s(["default",0,({replId:e,authz:i,initialIconUrl:w,originIconUrl:y})=>{var j;let b,{showError:R,showConfirm:I}=(0,u.default)(),_=(0,c.useIdSeed)()("repl-icon"),[S,F]=(0,r.useState)(w),[T,{loading:C}]=(j={onError:()=>{R("Something unexpected happened")},onCompleted:e=>{e.updateRepl.repl&&I("App icon updated successfully")}},b={...l,...j},a.useMutation(n,b)),D=S!==y,A=(0,s.default)({onUpload:async({url:t})=>{await T({variables:{input:{id:e,iconUrl:t}}}),F(t)},onUploadPreview:()=>{I("Uploading App icon")},onError:e=>R(e.message)});return(0,r.useEffect)(()=>{F(w)},[w]),(0,t.jsxs)(h.View,{gap:4,children:[(0,t.jsx)("label",{htmlFor:_,children:(0,t.jsx)(m.Text,{variant:"small",color:"dimmer",multiline:!1,children:"App icon"})}),(0,t.jsxs)(h.View,{row:!0,gap:16,align:"center",children:[(0,t.jsx)(x.default,{alt:"",size:32,iconUrl:S??""}),(0,t.jsx)(h.View,{grow:!0,shrink:!0,row:!0,gap:16,children:(0,t.jsx)(h.View,{grow:!0,shrink:!0,basis:0,children:(0,t.jsx)(g.FileUploadInput,{onSelect:e=>{e&&e.length>0&&A.uploadImage(e[0],o.ImageUploadContexts.ReplIcon)},acceptedFileTypes:d.ACCEPTABLE_IMAGE_UPLOAD_TYPES,dropZoneDisabled:!0,children:(0,t.jsx)(f.Tooltip,{tooltip:"Not allowed to update icon",isDisabled:i.isAuthorized,children:(0,t.jsx)(p.Button,{text:D?"Replace icon":"Upload icon",disabled:!i.isAuthorized,clsx:v.default.button,size:"small",loading:C})})})})})]})]})}],399997)}]);

//# debugId=ca47ec81-97c0-d303-efbb-222805c63c0c
//# sourceMappingURL=02xkc920~ovxn.js.map
