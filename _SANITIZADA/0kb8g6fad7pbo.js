;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="fec26b46-5882-fb4f-fc6c-ab88bfe0b99e")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,441503,e=>{"use strict";var t=e.i(276385),r=e.i(389959),i=e.i(992785),a=e.i(400218),n=e.i(973245),l=e.i(613141);let s={},o=n.gql`
    fragment OrgPresenceSessionUser on User {
  id
  username
  fullName
  image
  url
}
    `,d=n.gql`
    fragment OrgPresenceSessionRepl on Repl {
  id
  title
  url
  nextPagePathname
}
    `,u=n.gql`
    fragment OrgPresenceSessionItem on OrgPresenceSession {
  id
  user {
    ...OrgPresenceSessionUser
  }
  repl {
    ...OrgPresenceSessionRepl
  }
}
    ${o}
${d}`,c=n.gql`
    subscription OrgPresence($input: OrgReplPresenceSessionEventsInput!) {
  orgReplPresenceSessionEvents(input: $input) {
    __typename
    ... on OrgPresenceSessionInitEvent {
      sessions {
        ...OrgPresenceSessionItem
      }
    }
    ... on OrgPresenceSessionPingEvent {
      session {
        ...OrgPresenceSessionItem
      }
    }
    ... on OrgPresenceSessionLeaveEvent {
      sessionId
    }
  }
}
    ${u}`;function p(e){let t={...s,...e};return l.useSubscription(c,t)}e.i(242933);var g=e.i(279606);e.i(925218);var m=e.i(112077);function f(e,t){let{id:r,repl:i,user:a}=t;if(!a||!i){let t=e.findIndex(e=>e.id===r);-1!==t&&e.splice(t,1);return}let n={id:r,repl:i,user:a},l=e.findIndex(e=>e.id===r);-1===l?e.push(n):e.splice(l,1,n)}function h(e,t){switch(t.__typename){case"OrgPresenceSessionInitEvent":for(let r of(e.length=0,t.sessions))f(e,r);break;case"OrgPresenceSessionPingEvent":f(e,t.session);break;case"OrgPresenceSessionLeaveEvent":{let r=e.findIndex(e=>e.id===t.sessionId);if(-1===r)return;e.splice(r,1)}}}let x=[],v=(0,r.createContext)(null);e.s(["ReplPresenceProvider",0,function({orgId:e,children:i}){let n=(0,r.useMemo)(()=>({current:[]}),[]),l=(0,m.useCreateObservable)({});p({variables:{input:{orgId:e}},onData(e){let t=e.data.data?.orgReplPresenceSessionEvents;t&&(n.current=(0,a.produce)(n.current,e=>{h(e,t)}),l.set(function(e){let t={};for(let r of e){let e=r.repl.id,i=t[e];i||(i=new Map,t[e]=i),i.set(r.user.id,r.user)}let r={};for(let[e,i]of Object.entries(t))r[e]=[...i.values()].sort((e,t)=>e.id-t.id);return r}(n.current)))}});let s=(0,r.useMemo)(()=>g.Observable.from(l),[l]);return(0,t.jsx)(v.Provider,{value:s,children:i})},"useOrgPresenceSessions",0,({orgId:e,projectId:t})=>{let[i,n]=(0,r.useState)([]);return(0,r.useEffect)(()=>{n([])},[e,t]),p({variables:{input:{orgId:e,projectId:t}},onData(e){let t=e.data.data?.orgReplPresenceSessionEvents;t&&n(e=>(0,a.produce)(e,e=>{h(e,t)}))}}),i},"useReplPresenceUsers",0,function(e){let t=(0,r.useContext)(v);return(0,r.useMemo)(()=>t?t.select(t=>t[e]??x,i.default):null,[t,e])}],441503)},234504,480912,e=>{"use strict";var t=e.i(276385),r=e.i(389959),i=e.i(973245),a=e.i(613141);let n={},l=i.gql`
    subscription CurrentUserReplAgentStatuses {
  currentUserReplAgentStatuses {
    replId
    statusV2
    label
    updatedAt
    appImageUrl
  }
}
    `;e.i(242933);var s=e.i(279606);e.i(925218);var o=e.i(112077);let d=(0,r.createContext)(null);function u(){let e=(0,r.useContext)(d);if(null===e)throw Error("useCurrentUserAgentStatus must be used within an AgentStatusProvider");return e}e.s(["AgentStatusContext",0,d,"AgentStatusProvider",0,function({children:e}){let i,u=(0,o.useCreateObservable)(new Map);i={...n,fetchPolicy:"no-cache",onData:({data:{data:e}})=>{(e=>{if(!e?.currentUserReplAgentStatuses)return;let t=new Map(e.currentUserReplAgentStatuses.map(e=>[e.replId,{statusV2:e.statusV2,label:e.label,updatedAt:e.updatedAt,appImageUrl:e.appImageUrl}]));u.set(t)})(e)}},a.useSubscription(l,i);let c=(0,r.useMemo)(()=>s.Observable.from(u),[u]);return(0,t.jsx)(d.Provider,{value:c,children:e})},"default",0,u],234504);var c=e.i(992785);e.s(["useReplAgentStatus",0,function(e){let t=u();return(0,r.useMemo)(()=>t.select(t=>{let r=t.get(e.id);return r?{status:r.statusV2,label:r.label,appImageUrl:r.appImageUrl}:e.latestAgentStatus?{status:e.latestAgentStatus.statusV2,label:e.latestAgentStatus.label,appImageUrl:e.latestAgentStatus.appImageUrl}:null},c.default),[t,e.id,e.latestAgentStatus])}],480912)},517414,317349,e=>{"use strict";var t=e.i(973245),r=e.i(951262);let i={},a=t.gql`
    fragment DeleteReplDialogRepl on Repl {
  id
  title
}
    `,n=t.gql`
    mutation DeleteReplDialogReplDelete($id: String!) {
  deleteRepl(id: $id) {
    id
  }
}
    `;e.s(["DeleteReplDialogReplFragmentDoc",0,a,"useDeleteReplDialogReplDeleteMutation",0,function(e){let t={...i,...e};return r.useMutation(n,t)}],317349);var l=e.i(748538),s=e.i(781258),o=e.i(80593);let d={},u=t.gql`
    fragment ComponentsReplActionsFeaturedRepl on Repl {
  id
  isPrivate
  isFeaturedRepl
  publicForkCount
  timeUpdated
  org {
    id
  }
}
    `,c=t.gql`
    fragment ComponentsReplActions on Repl {
  id
  url
  title
  slug
  user {
    id
    username
  }
  ...DeleteReplDialogRepl
  ...EditReplFormRepl
  ...ComponentsReplActionsFeaturedRepl
  ...TransferReplToOrgDialogRepl
  ...LeaveMultiplayerReplDialogRepl
  owner {
    __typename
    ... on Team {
      id
    }
    ... on User {
      id
    }
  }
  org {
    id
  }
  isStarred
  isCurrentUserStarred
  isStackTemplate
  authorizations {
    deleteRepl {
      isAuthorized
    }
    editFolder {
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
    ${a}
${l.EditReplFormReplFragmentDoc}
${u}
${s.TransferReplToOrgDialogReplFragmentDoc}
${o.LeaveMultiplayerReplDialogReplFragmentDoc}`,p=t.gql`
    mutation ReplActionsUpdateRepl($input: UpdateReplInput!) {
  updateRepl(input: $input) {
    repl {
      id
      isStarred
    }
  }
}
    `,g=t.gql`
    mutation ReplActionsToggleReplPin($input: ToggleReplPinInput!) {
  toggleReplPin(input: $input) {
    ... on Repl {
      id
      isCurrentUserStarred
    }
    ... on Error {
      message
    }
  }
}
    `,m=t.gql`
    mutation AddOrgStackTemplate($orgId: String!, $replId: String!, $order: Float) {
  addOrgStackTemplate(orgId: $orgId, replId: $replId, order: $order) {
    success
    message
    repl {
      id
      isStackTemplate
    }
  }
}
    `,f=t.gql`
    mutation RemoveOrgStackTemplate($orgId: String!, $replId: String!) {
  removeOrgStackTemplate(orgId: $orgId, replId: $replId) {
    success
    message
    repl {
      id
      isStackTemplate
    }
  }
}
    `,h=t.gql`
    mutation ReplActionsMoveToFolder($replIds: [String!]!, $folderIds: [String!]!, $destFolderId: String!) {
  moveItemsToFolder(
    replIds: $replIds
    folderIds: $folderIds
    destFolderId: $destFolderId
  ) {
    ... on Repl {
      __typename
      id
      folderId
    }
  }
}
    `;e.s(["ComponentsReplActionsFragmentDoc",0,c,"useAddOrgStackTemplateMutation",0,function(e){let t={...d,...e};return r.useMutation(m,t)},"useRemoveOrgStackTemplateMutation",0,function(e){let t={...d,...e};return r.useMutation(f,t)},"useReplActionsMoveToFolderMutation",0,function(e){let t={...d,...e};return r.useMutation(h,t)},"useReplActionsToggleReplPinMutation",0,function(e){let t={...d,...e};return r.useMutation(g,t)},"useReplActionsUpdateReplMutation",0,function(e){let t={...d,...e};return r.useMutation(p,t)}],517414)},828378,e=>{e.v({button:"ReplCoverImageInput-module__I_Nioa__button"})},79433,801346,e=>{"use strict";var t=e.i(276385),r=e.i(389959),i=e.i(748538),a=e.i(183035),n=e.i(399245),l=e.i(269848),s=e.i(995691),o=e.i(416298),d=e.i(371884),u=e.i(320216),c=e.i(667116),p=e.i(973245),g=e.i(951262);let m={},f=p.gql`
    mutation ReplCoverImageUpdate($input: UpdateReplInput!) {
  updateRepl(input: $input) {
    repl {
      id
      imageUrl
    }
  }
}
    `;var h=e.i(349597),x=e.i(956264),v=e.i(345219),j=e.i(761843),R=e.i(766299),b=e.i(643484),y=e.i(186416),S=e.i(8047),T=e.i(244945),_=e.i(61732),C=e.i(828378);let k=({replId:e,authz:i,initialImageUrl:a,originImageUrl:n})=>{var l;let s,{showError:o,showConfirm:d}=(0,u.default)(),c=(0,R.useIdSeed)()("cover-image"),[p,k]=(0,r.useState)(a),[A,{loading:w}]=(l={onError:()=>{o("Something unexpected happened")},onCompleted:e=>{e.updateRepl.repl&&d("App cover image updated successfully")}},s={...m,...l},g.useMutation(f,s)),I=p!==n,O=(0,x.default)({onUpload:async({url:t})=>{await A({variables:{input:{id:e,imageUrl:t}}}),k(t)},onUploadPreview:()=>{d("Uploading repl cover image")},onError:e=>o(e.message)});(0,r.useEffect)(()=>{k(a)},[a]);let U=async()=>{await A({variables:{input:{id:e,imageUrl:null}}})};return(0,t.jsxs)(_.View,{gap:4,children:[(0,t.jsx)("label",{htmlFor:c,children:(0,t.jsx)(S.Text,{variant:"small",color:"dimmer",multiline:!1,children:"Cover image"})}),(0,t.jsxs)(_.View,{row:!0,gap:16,align:"center",children:[(0,t.jsx)(j.default,{alt:"",width:64,height:64,imageUrl:p}),(0,t.jsxs)(_.View,{grow:!0,shrink:!0,row:!0,gap:16,children:[(0,t.jsx)(_.View,{grow:!0,shrink:!0,basis:0,children:(0,t.jsx)(y.FileUploadInput,{onSelect:e=>{e&&e.length>0&&O.uploadImage(e[0],h.ImageUploadContexts.ReplCoverImage)},acceptedFileTypes:v.ACCEPTABLE_IMAGE_UPLOAD_TYPES,dropZoneDisabled:!0,children:(0,t.jsx)(T.Tooltip,{tooltip:"Not allowed to update image",isDisabled:i.isAuthorized,children:(0,t.jsx)(b.Button,{"aria-labelledby":c,text:I?"Replace image":"Upload image",disabled:!i.isAuthorized,clsx:C.default.button,size:"small",loading:w})})})}),I?(0,t.jsx)(_.View,{grow:!0,shrink:!0,basis:0,children:(0,t.jsx)(b.Button,{text:"Reset",size:"small",disabled:!i.isAuthorized,onClick:U,clsx:C.default.button,loading:w})}):null]})]})]})};e.s(["default",0,k],801346);var A=e.i(399997),w=e.i(402841),I=e.i(462229),O=e.i(691636),U=e.i(449525),D=e.i(528710),P=e.i(925654);let M=e=>0===e.length?{message:"Title cannot be blank"}:e.length>60?{message:"Title cannot be greater than 60 characters"}:void 0,F=e=>{if(e.length>w.REPL_DESCRIPTION_MAX_LENGTH)return{message:`Description cannot be greater than ${w.REPL_DESCRIPTION_MAX_LENGTH} characters`}},E=(0,I.cssRecord)({inputLabel:[O.rcss.flex.row,O.rcss.justify.spaceBetween,O.rcss.align.end],descriptionInput:[O.rcss.minHeight(96),O.rcss.maxHeight(256),{resize:"vertical"}],inputErrorIcon:[O.rcss.color.accentNegativeStronger],inputErrorMessage:[O.rcss.flex.growAndShrink(1),O.rcss.color.accentNegativeStronger]});function z({error:e,id:r}){return e?(0,t.jsxs)(_.View,{id:r,row:!0,gap:4,align:"center",children:[(0,t.jsx)(o.default,{css:E.inputErrorIcon}),(0,t.jsx)(S.Text,{css:E.inputErrorMessage,children:e.message})]}):null}function $(e){let r=(0,R.useIdSeed)();return(0,t.jsxs)(_.View,{gap:8,children:[(0,t.jsxs)(U.ButtonGroup,{tag:"fieldset",name:r("privacy"),value:e.isPrivate.toString(),onChange:t=>{e.onChange("true"===t)},row:!0,primary:!0,stretch:!0,children:[(0,t.jsx)(U.ButtonGroupItem,{id:r("false"),value:"false",text:"Public",icon:(0,t.jsx)(n.default,{})}),(0,t.jsx)(U.ButtonGroupItem,{id:r("true"),value:"true",text:"Private",icon:(0,t.jsx)(s.default,{})})]}),(0,t.jsx)(S.Text,{variant:"small",color:"dimmest",children:(0,c.default)(e.isPrivate,e.isTeam)})]})}e.s(["EditReplForm",0,function({repl:e,onDone:n}){let{showConfirm:s,showError:o}=(0,u.default)(),[c,{loading:p}]=(0,i.useEditReplFormEditMutation)({onCompleted:()=>{s("App edited"),n()},onError:e=>{o(e.message)}}),[g,{loading:m}]=(0,i.useEditReplFormEditMutation)({onCompleted:()=>{s("Updated privacy")},onError:e=>{o(e.message)}}),f=e.org?.type!=="team"&&e.authorizations.editVisibility.isAuthorized,h=(0,d.useFormField)(e.title,M),x=(0,d.useFormField)(e.description??"",F),v=(0,r.useId)(),j=(0,r.useId)(),R=(0,r.useId)(),y=(0,r.useId)(),T=!!h.error||!!x.error,C=e.owner?.__typename==="Team",I=async()=>{if(m)return;let t=!e.isPrivate;if(e.authorizations.editVisibility.isAuthorized||!1===t)return g({variables:{input:{id:e.id,isPrivate:!e.isPrivate}},optimisticResponse:{__typename:"RootMutationType",updateRepl:{__typename:"UpdateReplPayload",repl:{...e,isPrivate:!e.isPrivate}}}});o(e.authorizations.editVisibility.message)};return(0,t.jsxs)(_.View,{gap:32,children:[(0,t.jsxs)(_.View,{tag:"form",gap:24,onSubmit:t=>{t.preventDefault(),p||null==h.validate()&&null==x.validate()&&c({variables:{input:{id:e.id,title:h.value,description:x.value}}})},children:[(0,t.jsx)(S.Header,{variant:"headerDefault",level:2,children:"Edit App"}),(0,t.jsxs)(_.View,{gap:4,children:[(0,t.jsxs)(_.View,{css:E.inputLabel,children:[(0,t.jsx)("label",{htmlFor:v,children:(0,t.jsx)(S.Text,{variant:"small",color:"dimmer",multiline:!1,children:"Name"})}),(0,t.jsx)(P.default,{maxLength:60,value:h.value,hideLabel:!0})]}),(0,t.jsx)(D.Input,{style:{cursor:e.authorizations.editMetadata.isAuthorized?"auto":"not-allowed"},disabled:!e.authorizations.editMetadata.isAuthorized,maxLength:60,value:h.value,onChange:e=>h.setValue(e.target.value),spellCheck:!1,id:v,"aria-describedby":j}),(0,t.jsx)(z,{id:j,error:h.error})]}),(0,t.jsxs)(_.View,{gap:4,children:[(0,t.jsxs)(_.View,{css:E.inputLabel,children:[(0,t.jsx)("label",{htmlFor:R,children:(0,t.jsx)(S.Text,{variant:"small",color:"dimmer",multiline:!1,children:"Description"})}),(0,t.jsx)(P.default,{maxLength:w.REPL_DESCRIPTION_MAX_LENGTH,value:x.value,hideLabel:!0})]}),(0,t.jsx)(D.MultiLineInput,{disabled:!e.authorizations.editMetadata.isAuthorized,maxLength:w.REPL_DESCRIPTION_MAX_LENGTH,value:x.value,onChange:e=>x.setValue(e.target.value),placeholder:"What does this App do?",css:E.descriptionInput,id:R,"aria-describedby":y}),(0,t.jsx)(z,{id:y,error:x.error})]}),(0,t.jsxs)(_.View,{row:!0,gap:12,justify:"end",children:[(0,t.jsx)(b.Button,{type:"button",text:"Cancel",onClick:n}),(0,t.jsx)(b.Button,{type:"submit",iconLeft:p?(0,t.jsx)(l.default,{}):(0,t.jsx)(a.default,{}),disabled:p||T||!e.authorizations.editMetadata.isAuthorized,text:"Save",colorway:"primary"})]})]}),(0,t.jsxs)(_.View,{gap:16,children:[(0,t.jsx)(A.default,{replId:e.id,authz:e.authorizations.editMetadata,initialIconUrl:e.iconUrl,originIconUrl:e.templateInfo?.iconUrl}),(0,t.jsx)(k,{replId:e.id,authz:e.authorizations.editMetadata,initialImageUrl:e.imageUrl??e.templateInfo?.imageUrl,originImageUrl:e.templateInfo?.imageUrl})]}),f?(0,t.jsx)($,{isPrivate:e.isPrivate,onChange:I,isTeam:C}):null]})},"PrivacyToggle",0,$],79433)},612963,e=>{"use strict";var t=e.i(973245),r=e.i(304277);e.i(566901);let i={},a=t.gql`
    fragment OrgReplCreator on User {
  id
  displayName
  fullName
  username
  image
}
    `,n=t.gql`
    query UserSelectorSearch($orgId: String!, $searchInput: OrgMembersInput!) {
  currentUser {
    __typename
    id
    org(orgId: $orgId) {
      __typename
      ... on Org {
        id
        members(input: $searchInput) {
          __typename
          ... on Error {
            message
          }
          ... on OrgMemberConnection {
            __typename
            items {
              member {
                id
                user {
                  id
                  ...OrgReplCreator
                }
              }
              type
            }
          }
        }
      }
    }
  }
}
    ${a}`,l=t.gql`
    query UserSelectorGetUser($id: Int!) {
  user(id: $id) {
    id
    ...OrgReplCreator
  }
}
    ${a}`;e.s(["OrgReplCreatorFragmentDoc",0,a,"UserSelectorGetUserDocument",0,l,"useUserSelectorSearchQuery",0,function(e){let t={...i,...e};return r.useQuery(n,t)}])},36763,291852,582086,e=>{"use strict";var t=e.i(973245),r=e.i(612963),i=e.i(951262);let a={},n=t.gql`
    fragment AppCardApp on Repl {
  id
  title
  iconUrl
  url
  isCurrentUserStarred
  user {
    id
    ...OrgReplCreator
  }
  deploymentMetadata {
    ... on DeploymentMetadata {
      id
      url
      timeDeployed
    }
  }
}
    ${r.OrgReplCreatorFragmentDoc}`,l=t.gql`
    mutation UpdateStarredApps($input: UpdateStarredAppsInput!) {
  updateStarredApps(input: $input) {
    ... on Org {
      __typename
      id
      currentUserStarredApps {
        ... on StarredApp {
          id
          repl {
            id
            ...AppCardApp
          }
        }
      }
      currentUserRecentOrgApps {
        id
        ...AppCardApp
      }
    }
    ... on NotFoundError {
      message
    }
    ... on UserError {
      message
    }
    ... on UnauthorizedError {
      message
    }
    ... on Error {
      message
    }
  }
}
    ${n}`;e.s(["AppCardAppFragmentDoc",0,n,"useUpdateStarredAppsMutation",0,function(e){let t={...a,...e};return i.useMutation(l,t)}],291852);let s=t.gql`
    fragment CurrentUserRecentApps on Org {
  currentUserRecentOrgApps {
    ... on Repl {
      id
      ...AppCardApp
    }
  }
}
    ${n}`;e.s(["CurrentUserRecentAppsFragmentDoc",0,s],582086);let o={},d=t.gql`
    mutation TrackOrgAppOpen($input: TrackOrgAppOpenInput!) {
  trackOrgAppOpen(input: $input) {
    ... on Org {
      id
      ...CurrentUserRecentApps
    }
  }
}
    ${s}`;var u=e.i(709485),c=e.i(151027),p=e.i(415541);e.s(["default",0,e=>{let t,r=(0,c.useCurrentUserStoredOrgContext)(),a=e?.orgId??r.orgId,n=e?.orgRole??r.orgRole,[l]=(t={...o,...void 0},i.useMutation(d,t));return{trackAppOpen:e=>{a&&(l({variables:{input:{orgId:a,replId:e}}}),(0,p.track)(u.events.ORG_APP_VIEWED,{replId:e,context:(0,c.getOrgTrackingContext)({id:a}),orgRole:n}))}}}],36763)},120375,e=>{e.v({dropdownTrigger:"DeploymentArtifactDropdown-module__dq8lNq__dropdownTrigger",itemContent:"DeploymentArtifactDropdown-module__dq8lNq__itemContent",itemRow:"DeploymentArtifactDropdown-module__dq8lNq__itemRow",menu:"DeploymentArtifactDropdown-module__dq8lNq__menu",textContainer:"DeploymentArtifactDropdown-module__dq8lNq__textContainer",thumbContainer:"DeploymentArtifactDropdown-module__dq8lNq__thumbContainer"})},83234,e=>{"use strict";var t=e.i(276385),r=e.i(389959),i=e.i(908796),a=e.i(167392),n=e.i(182409),l=e.i(66924),s=e.i(816350),o=e.i(566049),d=e.i(453891),u=e.i(36763),c=e.i(919073),p=e.i(643484),g=e.i(295231),m=e.i(8047),f=e.i(61732),h=e.i(120375);function x({artifact:e,baseUrl:r,disabled:i,onAction:a}){let n=(0,l.getArtifactKindConfigFromString)(e.type),o=e.name,d=i?void 0:(0,s.getArtifactDeploymentUrl)(e,r);return(0,t.jsx)(g.BaseMenuItem,{id:e.id,textValue:o,href:d,target:"_blank",rel:"noreferrer",onAction:a,isDisabled:i,children:(0,t.jsx)(f.View,{row:!0,gap:6,align:"center",clsx:h.default.itemRow,children:(0,t.jsxs)(f.View,{row:!0,gap:6,align:"center",shrink:!0,clsx:h.default.itemContent,children:[(0,t.jsx)(c.ShadesSurface,{align:"center",justify:"center",width:24,height:24,clsx:h.default.thumbContainer,br:4,children:(0,t.jsx)(n.Icon,{size:12,color:n.color})}),(0,t.jsxs)(f.View,{shrink:!0,clsx:h.default.textContainer,children:[(0,t.jsx)(m.Text,{variant:"small",multiline:!1,showTooltipOnTruncate:!0,children:o}),i?(0,t.jsx)(m.Text,{color:"dimmest",variant:"small",multiline:!1,children:"This deployment type has no URL"}):null]})]})})})}e.s(["DeploymentArtifactDropdown",0,function({artifacts:e,deployment:l,replId:s}){let[c,m]=(0,r.useState)(!1),{href:f}=(0,d.useDeploymentLink)(l),{trackAppOpen:v}=(0,u.default)(),{currentBuild:j}=l,{title:R,color:b}=o.buildStatuses[j.status],y=j.status===i.HostingBuildStatus.Success?"Published":R,S=j.provider!==i.HostingBuildProvider.Cron&&j.provider!==i.HostingBuildProvider.Extension;return(0,t.jsx)(g.PopupMenu,{"aria-label":"Deployment creations menu",isOpen:c,onOpenChange:m,clsx:h.default.menu,trigger:(0,t.jsx)(p.Button,{size:"xsmall",variant:"nofill",shrink:!0,text:y,iconLeft:(0,t.jsx)(n.default,{size:12,color:b}),iconRight:(0,t.jsx)(a.default,{size:12}),clsx:h.default.dropdownTrigger}),children:e.map(e=>(0,t.jsx)(x,{artifact:e,baseUrl:f,disabled:!S,onAction:S?()=>v(s):void 0},e.id))})}])},593876,e=>{e.v({overflowChip:"ArtifactTicTacs-module__SO-Q6G__overflowChip",ticTac:"ArtifactTicTacs-module__SO-Q6G__ticTac"})},345395,e=>{"use strict";var t=e.i(276385),r=e.i(66924),i=e.i(919073),a=e.i(8047),n=e.i(244945),l=e.i(61732),s=e.i(593876);function o({artifact:e,isActive:a,onActiveChange:l}){let d=(0,r.getArtifactKindConfigFromString)(e.kind);return(0,t.jsx)(n.Tooltip,{tooltip:e.name,children:(0,t.jsx)(i.ShadesSurface,{tag:"button","aria-label":e.name,"aria-pressed":a,align:"center",justify:"center",clsx:s.default.ticTac,br:8,colorShade:a?"themePrimaryInverted":void 0,border:a?"strong":void 0,onPointerEnter:()=>l?.(e.id),onClick:()=>l?.(e.id),children:(0,t.jsx)(d.Icon,{size:14})})})}e.s(["ArtifactTicTacs",0,function({artifacts:e,activeId:r,onActiveChange:n,maxVisible:d=4}){if(0===e.length)return null;let u=e.slice(0,d),c=e.length-u.length;return(0,t.jsxs)(l.View,{row:!0,gap:4,align:"center",children:[u.map(e=>(0,t.jsx)(o,{artifact:e,isActive:e.id===r,onActiveChange:n},e.id)),c>0?(0,t.jsx)(i.ShadesSurface,{align:"center",justify:"center",clsx:s.default.overflowChip,br:8,children:(0,t.jsxs)(a.Text,{variant:"small",color:"dimmer",children:["+",c]})}):null]})}])},248902,449820,e=>{"use strict";var t=e.i(276385),r=e.i(317349),i=e.i(320216),a=e.i(924325);e.s(["DeleteReplDialog",0,function({repl:e,onDeleteRequested:n,onDone:l}){let{showConfirm:s,showError:o}=(0,i.default)(),[d,u]=(0,r.useDeleteReplDialogReplDeleteMutation)({onCompleted:e=>{"Repl"===e.deleteRepl.__typename?(s("App scheduled for deletion"),n?.(),l?.()):o("Something went wrong")},onError:e=>o(e.message),variables:{id:e.id},update:(e,t)=>{t.data?.deleteRepl.id&&(e.evict({id:e.identify(t.data.deleteRepl)}),e.gc())}});return(0,t.jsx)(a.default,{name:e.title,entityType:"App",isDeleting:u.loading,delete:()=>{u.loading||d()},hideModal:()=>l?.()})}],248902);var n=e.i(80593),l=e.i(122400),s=e.i(131344),o=e.i(8047);e.s(["LeaveMultiplayerReplDialog",0,function({repl:e,onLeave:r,onCancel:a}){let{showConfirm:d,showError:u}=(0,i.default)(),[c,{loading:p}]=(0,n.useLeaveMultiplayerReplDialogRemoveMutation)({variables:{id:e.id},refetchQueries:["CurrentUserRepls"],onCompleted(){d("App removed"),r()},onError(e){u(e.message)}});return(0,t.jsx)(s.default,{title:"Leave multiplayer App",confirmLabel:"Yes, leave this App",isDestructive:!0,loading:p,confirmIcon:(0,t.jsx)(l.default,{}),onCancel:a,onConfirm:()=>{p||c()},children:(0,t.jsxs)(o.Text,{children:["Are you sure you want to leave this multiplayer App (",e.title,")? You will no longer be able to access its content."]})})}],449820)},253864,e=>{"use strict";var t=e.i(276385),r=e.i(488081),i=e.i(389959),a=e.i(908796),n=e.i(973245),l=e.i(304277);e.i(566901);let s={},o=n.gql`
    fragment ReplsDashboardMoveItemReplFolder on ReplFolder {
  id
  pathnames
  folderType
  name
  parentId
  timeCreated
}
    `,d=n.gql`
    query ReplsDashboardMoveItemModalFolder($id: String!, $teamId: Int) {
  currentUser {
    id
    replFolder(id: $id, teamId: $teamId) {
      id
      folders {
        id
        ...ReplsDashboardMoveItemReplFolder
      }
    }
  }
}
    ${o}`;var u=e.i(657929),c=e.i(302905),p=e.i(143524),g=e.i(269848),m=e.i(50814),f=e.i(967629),h=e.i(480028),x=e.i(462229),v=e.i(691636),j=e.i(643484),R=e.i(8047),b=e.i(61732);let y={__typename:"ReplFolder",id:"__ROOT_ID__",name:"(home)/",pathnames:["(home)/"],canEdit:!1,timeCreated:null},S=(0,x.cssRecord)({folderPicker:[v.rcss.height(250),v.rcss.overflow("auto"),v.rcss.borderRadius(4),v.rcss.border({color:h.tokens.outlineDimmest})]}),T=(0,f.css)({"&":{height:"40px",display:"flex",justifyContent:"space-between",alignItems:"center",padding:"0 10px"},"&:hover":{cursor:"pointer",backgroundColor:h.tokens.backgroundRoot},".small-folder-icon-container":{height:"20px",width:"20px",display:"flex",justifyContent:"center",alignItems:"center"},".small-back-folder-icon":{transform:"rotate(90deg)",width:"17px"},".small-folder-icon":{width:"20px"},".small-folder-title":{display:"flex",alignItems:"center"},".small-folder-title a":{marginLeft:"20px",borderBottom:"none",color:"inherit"},".small-folder-time":{fontSize:"12px",color:h.tokens.foregroundDimmer},"&.is-selected:hover,.is-selected":{backgroundColor:h.tokens.accentPrimaryDefault,color:h.tokens.backgroundHigher},".is-selected .small-folder-time":{color:"inherit"}}),_=({folder:e,onSelect:r,onNavigate:i,isSelected:a,isBack:n=!1})=>(0,t.jsxs)("div",{clsx:[{"is-selected":a}],onClick:()=>{r&&r(e)},css:T,children:[(0,t.jsxs)("div",{className:"small-folder-title",children:[(0,t.jsx)("div",{className:"small-folder-icon-container",children:n?(0,t.jsx)("div",{className:"small-back-folder-icon",children:(0,t.jsx)(u.default,{})}):(0,t.jsx)("div",{className:"small-folder-icon",children:(0,t.jsx)(c.default,{})})}),(0,t.jsx)("a",{onClick:t=>i?i(e,t):()=>{},children:e.name})]}),(0,t.jsx)("div",{className:"small-folder-time",children:e.timeCreated?(0,m.ago)(e.timeCreated):""})]});e.s(["default",0,e=>{var n;let o,{item:u,isRepl:c,teamId:m,hideModal:f}=e,h=/\/@([^/]*)/.exec(r.default.asPath||""),x=h?h[1]:null,v=m&&x?{__typename:"ReplFolder",id:`__TEAM__${m}__`,name:`@${x}`,pathnames:[`@${x}`],canEdit:!1,timeCreated:null}:y,[T,C]=(0,i.useState)(null),[k,A]=(0,i.useState)(v),[w,I]=(0,i.useState)([]),{data:O,loading:U}=(n={fetchPolicy:"cache-and-network",variables:{id:k.id,teamId:m},ssr:!1,notifyOnNetworkStatusChange:!0},o={...s,...n},l.useQuery(d,o)),D=e=>{e===T?C(null):C(e)},P=(e,t)=>{t.stopPropagation(),e.pathnames.length>k.pathnames.length?w.push(k):w.pop(),A(e),C(e),I(w)},M=async()=>{let t=[],r=[];c?t.push(u.id):r.push(u.id),e.onSubmit({variables:{destFolderId:T?T.id:"",replIds:t,folderIds:r,teamId:m}}),f()},F=(O?.currentUser?.replFolder?.folders||[]).filter(e=>("Unnamed"!==e.name||null!==e.parentId)&&e.folderType===a.ReplFolderTypes.Default&&(!!c||e.id!==u.id)).map(e=>({...e,pathnames:e.pathnames.slice(1)})),E=w[w.length-1]||v,z=T?T.id:"",$="name"in u?u.name:u.title;return(0,t.jsxs)(b.View,{gap:8,tag:"form",onSubmit:e=>{e.preventDefault(),M()},children:[(0,t.jsxs)(R.Text,{children:["Move ",$," to:"]}),(0,t.jsxs)(b.View,{css:S.folderPicker,children:[k.pathnames&&k.pathnames.join()!==v.pathnames.join()?(0,t.jsx)(_,{folder:{...E,name:"(up one level)"},isBack:!0,onNavigate:P,isSelected:z===E.id}):null,F?F.map(e=>(0,t.jsx)(_,{folder:e,onSelect:D,onNavigate:P,isSelected:e.id===z},`move-folder-${e.id}`)):null]}),(0,t.jsxs)(R.Text,{children:["Moving to:"," ",T?T.pathnames[T.pathnames.length-1]:k.pathnames[k.pathnames.length-1]||"(home)/"]}),(0,t.jsxs)(b.View,{row:!0,gap:8,justify:"end",children:[U?null:(0,t.jsx)(j.Button,{text:"Cancel",onClick:()=>f()}),(0,t.jsx)(j.Button,{colorway:"primary",iconLeft:U?(0,t.jsx)(g.default,{}):(0,t.jsx)(p.default,{}),disabled:U,text:c?"Move App":"Move folder",type:"submit"})]})]})}],253864)},318418,e=>{"use strict";var t=e.i(276385),r=e.i(389959),i=e.i(908796),a=e.i(973245),n=e.i(951262);let l={},s=a.gql`
    mutation TransferReplWithinOrgDialogTransfer($input: TransferReplWithinOrgInput!) {
  transferReplWithinOrg(input: $input) {
    ... on Repl {
      id
      user {
        id
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
    `;var o=e.i(269848),d=e.i(612343),u=e.i(320216),c=e.i(959787),p=e.i(643484),g=e.i(8047),m=e.i(61732);e.s(["TransferReplWithinOrgDialog",0,function({repl:e,orgId:a,hideModal:f}){let h,x=`group-search-${(0,r.useId)()}`,[v,j]=(0,r.useState)(),[R,b]=(0,r.useState)(""),{showError:y,showConfirm:S}=(0,u.default)(),[T,{loading:_}]=(h={...l,...void 0},n.useMutation(s,h)),C=async()=>{if(!v)return;let t=await T({variables:{input:{replId:e.id,newOwnerOrgGroupId:v.id}}});t.data?.transferReplWithinOrg.__typename==="Repl"?(S("Repl transferred successfully"),f()):y(t.data?.transferReplWithinOrg.message??"Transfer failed")};return(0,t.jsxs)(m.View,{gap:24,children:[(0,t.jsxs)(g.Header,{variant:"subheadDefault",level:2,children:["Transfer ownership of ",e.title]}),(0,t.jsxs)(m.View,{gap:8,children:[(0,t.jsxs)(g.Text,{children:["Select another member of your workspace to transfer to. The selected user will become the primary owner of ",e.title," and will be displayed as the app creator in your workspace's app directory."]}),(0,t.jsx)(m.View,{grow:!0,shrink:!0,children:(0,t.jsx)(c.default,{inputId:x,orgId:a,types:[i.OrgGroupType.SystemIndividual],selectedGroups:v?[v]:[],value:R,setValue:b,onSelect:e=>{j(e),b(e.name)},onClear:()=>j(void 0),placeholder:"Select a user"})})]}),(0,t.jsxs)(m.View,{row:!0,gap:12,justify:"end",children:[(0,t.jsx)(p.Button,{text:"Cancel",onClick:f}),(0,t.jsx)(p.Button,{dataCy:"transfer-repl-dialog-confirm-button",disabled:_||!v,iconLeft:_?(0,t.jsx)(o.default,{}):(0,t.jsx)(d.default,{}),onClick:C,text:"Transfer app",colorway:"primary"})]})]})}],318418)},845128,e=>{"use strict";var t=e.i(276385),r=e.i(389959),i=e.i(781258),a=e.i(269848),n=e.i(450265),l=e.i(416298),s=e.i(320216),o=e.i(429843),d=e.i(825419),u=e.i(643484),c=e.i(585544),p=e.i(19322),g=e.i(108431),m=e.i(8047),f=e.i(61732);e.s(["TransferReplToOrgDialog",0,function({repl:e,onDone:h}){let x=`org-select-${(0,r.useId)()}`,[v,j]=(0,r.useState)(""),{showError:R,showConfirm:b}=(0,s.default)(),{data:y,loading:S,error:T}=(0,i.useTransferReplToOrgDialogOrgsQuery)(),[_,{loading:C}]=(0,i.useTransferReplToOrgDialogTransferMutation)(),k=y?.currentUser?.orgs?.__typename==="CurrentUserOrganizationConnection"?y.currentUser.orgs.items.map(e=>({id:e.org.id,name:e.org.name,slug:e.org.slug,image:e.org.image??null})):[],A=k.find(e=>e.id===v),w=async()=>{if(!A)return void R("Please select a workspace");try{let t=await _({variables:{orgId:A.id,replIds:[e.id]}}),r=t.data?.transferReplToOrganization;r?.__typename==="TransferReplToOrganizationSuccess"?(b(`Successfully started transfer of "${e.title}" to ${A.name}.`),h()):r?.__typename==="UserError"||r?.__typename==="TooManyRequestsError"?R(r.message||"Failed to transfer repl"):R("Unexpected response from server")}catch(e){R("Failed to transfer repl. Please try again."),o.logger.error("Replit TransferReplToOrgDialog error:",e)}},I=()=>{h()};if(S)return(0,t.jsxs)(f.View,{gap:24,align:"center",children:[(0,t.jsxs)(m.Header,{variant:"subheadDefault",level:2,children:["Transfer ",e.title," to Organization"]}),(0,t.jsx)(a.default,{})]});if(T||y?.currentUser?.orgs?.__typename!=="CurrentUserOrganizationConnection"&&y?.currentUser?.orgs?.__typename){let r=T?.message||(y?.currentUser?.orgs?.__typename==="NotFoundError"||y?.currentUser?.orgs?.__typename==="UserError"?y.currentUser.orgs.message:"Failed to load workspaces");return(0,t.jsxs)(f.View,{gap:24,children:[(0,t.jsxs)(m.Header,{variant:"subheadDefault",level:2,children:["Transfer ",e.title," to Organization"]}),(0,t.jsx)(m.Text,{children:r}),(0,t.jsx)(f.View,{row:!0,gap:12,justify:"end",children:(0,t.jsx)(u.Button,{text:"Close",onClick:I})})]})}return 0===k.length?(0,t.jsxs)(f.View,{gap:24,children:[(0,t.jsxs)(m.Header,{variant:"subheadDefault",level:2,children:["Transfer ",e.title," to Organization"]}),(0,t.jsx)(m.Text,{children:"You don't belong to any organizations. You need to be a member of an organization to transfer repls to it."}),(0,t.jsx)(f.View,{row:!0,gap:12,justify:"end",children:(0,t.jsx)(u.Button,{text:"Close",onClick:I})})]}):(0,t.jsxs)(f.View,{gap:24,children:[(0,t.jsxs)(m.Header,{variant:"subheadDefault",level:2,children:["Transfer ",e.title," to Organization"]}),(0,t.jsxs)(f.View,{gap:8,children:[(0,t.jsxs)(m.Text,{children:['Select an organization to transfer "',e.title,'" to. This action is irreversible and the app will no longer belong to you.']}),(0,t.jsx)(g.StatusBanner,{colorway:"warning",text:"Linked account secrets will not be transferred. You'll need to re-link them in the destination workspace.",icon:(0,t.jsx)(l.default,{})}),(0,t.jsxs)(f.View,{gap:4,children:[(0,t.jsx)("label",{htmlFor:x,children:(0,t.jsx)(m.Text,{color:"dimmer",variant:"small",children:"Destination Organization"})}),(0,t.jsx)(p.Select,{id:x,"aria-label":"Select workspace",placeholder:"Choose a workspace...",selectedKey:v,onSelectionChange:e=>{null!=e&&j(e)},isDisabled:C,children:k.map(e=>(0,t.jsx)(c.ListBoxItem,{id:e.id,label:`${e.name} (@${e.slug})`,icon:(0,t.jsx)(d.Avatar,{src:e.image,size:16,username:e.name})},e.id))})]}),(0,t.jsx)(m.Text,{color:"dimmer",variant:"small",children:"The transfer occurs in the background and may take some time to complete."})]}),(0,t.jsxs)(f.View,{row:!0,gap:12,justify:"end",children:[(0,t.jsx)(u.Button,{text:"Cancel",onClick:I,disabled:C}),(0,t.jsx)(u.Button,{dataCy:"transfer-repl-to-org-dialog-confirm-button",disabled:C||!v,iconLeft:C?(0,t.jsx)(a.default,{}):(0,t.jsx)(n.default,{}),onClick:w,text:"Transfer to Workspace",colorway:"primary"})]})]})}])},519425,e=>{"use strict";var t,r,i=e.i(276385),a=e.i(389959),n=e.i(517414),l=e.i(908796),s=e.i(122400),o=e.i(534141),d=e.i(712771),u=e.i(143524),c=e.i(61935),p=e.i(828322),g=e.i(869472),m=e.i(898039),f=e.i(908628),h=e.i(491194),x=e.i(612343),v=e.i(450265),j=e.i(570438),R=e.i(151027),b=e.i(730497),y=e.i(320216),S=e.i(955410),T=e.i(934174),_=e.i(248902),C=e.i(79433),k=e.i(449820),A=e.i(253864),w=e.i(318418),I=e.i(488299),O=e.i(295231),U=e.i(528326),D=e.i(183555),P=e.i(921125),M=e.i(845128),F=((t=F||{}).CoverPage="CoverPage",t.Delete="Delete",t.Edit="Edit",t.Leave="Leave",t.TransferWithinOrg="TransferWithinOrg",t.TransferPersonalToOrg="TransferPersonalToOrg",t.MoveToFolder="MoveToFolder",t.Fork="Fork",t.Feature="Feature",t.Pin="Pin",t.Unpin="Unpin",t.MarkAsStack="MarkAsStack",t.UnmarkAsStack="UnmarkAsStack",t),E=((r=E||{}).Delete="Delete",r.Edit="Edit",r.Fork="Fork",r.Feature="Feature",r.Leave="Leave",r.TransferWithinOrg="TransferWithinOrg",r.TransferPersonalToOrg="TransferPersonalToOrg",r.MoveToFolder="MoveToFolder",r.MarkAsStack="MarkAsStack",r.UnmarkAsStack="UnmarkAsStack",r);function z({repl:e,deleteAction:t}){let{trackClick:r}=(0,S.useTrackClick)(),[F,E]=(0,a.useState)(null),$=(0,j.useCurrentUserId)(),{fork:V,isForking:L}=(0,D.useForkContext)(),{orgRole:q}=(0,R.useCurrentUserStoredOrgContext)(),{showNotice:B,showError:N}=(0,y.default)(),W=(0,R.useIsCurrentOrgEnterprise)(),H=(0,b.useFlag)({controlName:"flag-per-user-pinning"}),[G,{loading:K}]=(0,n.useReplActionsUpdateReplMutation)(),[Q,{loading:Y}]=(0,n.useReplActionsToggleReplPinMutation)(),X=K||Y,[J]=(0,n.useReplActionsMoveToFolderMutation)(),[Z,{loading:ee}]=(0,n.useAddOrgStackTemplateMutation)({onCompleted:e=>{e.addOrgStackTemplate?.success?B(e.addOrgStackTemplate.message||"Successfully pinned template"):N(e.addOrgStackTemplate?.message||"Failed to pin template")},onError:e=>{N(`Error pinning template: ${e.message}`)}}),[et,{loading:er}]=(0,n.useRemoveOrgStackTemplateMutation)({onCompleted:e=>{e.removeOrgStackTemplate?.success?B(e.removeOrgStackTemplate?.message||"Successfully removed pinned template"):N(e.removeOrgStackTemplate?.message||"Failed to remove pinned template")},onError:e=>{N(`Error removing pinned template: ${e.message}`)}}),ei=e.authorizations,ea=e.org?.__typename==="Org",en=e.owner?.id===$,el=q===l.SystemOrgGroupType.SystemAdmins,es=ei.editFolder.isAuthorized,eo=ea&&W&&el,ed=t?.type==="hidden",eu=t?.type==="visible"?t.onDeleteRequested:void 0,ec=H?e.isCurrentUserStarred:e.isStarred,ep=[{label:"Cover page",value:"CoverPage",link:(0,P.replViewLinkProps)(e),icon:(0,i.jsx)(d.default,{})},...ei.star.isAuthorized&&ec?[{label:"Unpin from top",value:"Unpin",icon:(0,i.jsx)(g.default,{})}]:[],...ei.star.isAuthorized&&!ec?[{label:"Pin to top",value:"Pin",icon:(0,i.jsx)(g.default,{})}]:[],...ei.editMetadata.isAuthorized?[{label:"Edit details",value:"Edit",icon:(0,i.jsx)(o.default,{})}]:[],...ea&&(en||el)?[{label:"Transfer Owner",value:"TransferWithinOrg",icon:(0,i.jsx)(x.default,{})}]:[],...en&&!ea?[{label:"Transfer To Workspace",value:"TransferPersonalToOrg",icon:(0,i.jsx)(v.default,{})}]:[],...es?[{label:"Move to folder",value:"MoveToFolder",icon:(0,i.jsx)(u.default,{})}]:[],...ei.fork.isAuthorized?[{label:"Remix",value:"Fork",icon:(0,i.jsx)(m.default,{})}]:[],...ea&&!e.isPrivate?[{label:e.isFeaturedRepl?"Remove from Featured Apps":"Feature on Profile",value:"Feature",icon:(0,i.jsx)(f.default,{})}]:[],...eo&&!e.isStackTemplate?[{label:"Pin to Agent input box",value:"MarkAsStack",icon:(0,i.jsx)(c.default,{})}]:[],...eo&&e.isStackTemplate?[{label:"Unpin from Agent input box",value:"UnmarkAsStack",icon:(0,i.jsx)(c.default,{})}]:[],...ei.removeSelf.isAuthorized?[{label:"Leave",value:"Leave",isDestructive:!0,icon:(0,i.jsx)(s.default,{})}]:[],...ei.deleteRepl.isAuthorized&&!ed?[{label:"Delete",value:"Delete",isDestructive:!0,icon:(0,i.jsx)(h.default,{})}]:[]];return(0,i.jsxs)(i.Fragment,{children:[(0,i.jsx)(O.PopupMenu,{trigger:(0,i.jsx)(I.IconButton,{tooltipBehavior:"hidden",size:24,alt:"App Actions",children:(0,i.jsx)(p.default,{size:16})}),onAction:t=>{switch(t){case"CoverPage":break;case"Edit":E("Edit");break;case"TransferWithinOrg":E("TransferWithinOrg");break;case"TransferPersonalToOrg":E("TransferPersonalToOrg");break;case"MoveToFolder":E("MoveToFolder");break;case"Leave":E("Leave");break;case"Delete":E("Delete");break;case"Fork":L||V();break;case"Feature":E("Feature");break;case"Pin":case"Unpin":{if(X)break;let r="Pin"===t;H?Q({variables:{input:{replId:e.id,pinned:r}},optimisticResponse:{__typename:"RootMutationType",toggleReplPin:{__typename:"Repl",id:e.id,isCurrentUserStarred:r}},refetchQueries:["CurrentUserRepls"],onCompleted:e=>{let t=e.toggleReplPin;t&&"message"in t&&N(t.message)},onError:e=>{N(e.message)}}):G({variables:{input:{id:e.id,isStarred:r}},optimisticResponse:{__typename:"RootMutationType",updateRepl:{__typename:"UpdateReplPayload",repl:{__typename:"Repl",id:e.id,isStarred:r}}},refetchQueries:["CurrentUserRepls"],onError:e=>{N(e.message)}});break}case"MarkAsStack":e.org?.id&&!ee&&(r({productArea:"design_systems",target:"pin_app_to_agent_input_menu_item"}),Z({variables:{orgId:e.org.id,replId:e.id}}));break;case"UnmarkAsStack":e.org?.id&&!er&&(r({productArea:"design_systems",target:"unpin_app_from_agent_input_menu_item"}),et({variables:{orgId:e.org.id,replId:e.id}}))}},children:ep.map(e=>(0,i.jsx)(O.MenuItem,{id:e.value,label:e.label,icon:e.icon,isDestructive:e.isDestructive,...e.link?{href:e.link.href,as:e.link.as}:{}},e.value))}),(0,i.jsx)(U.Modal,{isOpen:"Leave"===F,onRequestClose:()=>E(null),children:(0,i.jsx)(k.LeaveMultiplayerReplDialog,{repl:e,onCancel:()=>E(null),onLeave:()=>{E(null),eu?.()}})}),(0,i.jsx)(U.Modal,{isOpen:"Delete"===F,onRequestClose:()=>E(null),children:(0,i.jsx)(_.DeleteReplDialog,{repl:e,onDone:()=>E(null),onDeleteRequested:eu})}),(0,i.jsx)(U.Modal,{isOpen:"Edit"===F,onRequestClose:()=>E(null),children:(0,i.jsx)(C.EditReplForm,{repl:e,onDone:()=>E(null)})}),e.org?.id?(0,i.jsx)(U.Modal,{isOpen:"TransferWithinOrg"===F,onRequestClose:()=>E(null),children:(0,i.jsx)(w.TransferReplWithinOrgDialog,{repl:e,orgId:e.org?.id,hideModal:()=>E(null)})}):null,(0,i.jsx)(U.Modal,{isOpen:"TransferPersonalToOrg"===F,onRequestClose:()=>E(null),children:(0,i.jsx)(M.TransferReplToOrgDialog,{repl:e,onDone:()=>E(null)})}),(0,i.jsx)(U.Modal,{isOpen:"MoveToFolder"===F,onRequestClose:()=>E(null),children:(0,i.jsx)(A.default,{isRepl:!0,item:e,teamId:void 0,hideModal:()=>E(null),onSubmit:e=>{J({variables:{replIds:e.variables.replIds,folderIds:e.variables.folderIds,destFolderId:e.variables.destFolderId},refetchQueries:["CurrentUserRepls","ReplsFiltersFolderList"],onCompleted:()=>{B("App moved successfully")},onError:e=>{N(e.message)}})}})}),(0,i.jsx)(U.Modal,{isOpen:"Feature"===F,onRequestClose:()=>E(null),centered:!0,maxWidth:650,children:(0,i.jsx)(T.default,{isFeatured:e.isFeaturedRepl,repl:e,orgId:e.org?.id,onCompleted:()=>E(null)})})]})}e.s(["ReplActions",0,function({repl:e,trackingContext:t,deleteAction:r}){return(0,i.jsx)(D.ForkContextProvider,{forkParams:{trackingData:{forkSource:t}},repl:e,children:(0,i.jsx)(z,{repl:e,deleteAction:r})})}])},162912,e=>{e.v({dim:"StatusBadge-module__iziSwq__dim"})},202239,807645,e=>{"use strict";var t=e.i(276385),r=e.i(908796),i=e.i(399245),a=e.i(453891),n=e.i(36763),l=e.i(892158);e.s(["DeploymentSiteLink",0,function({deployment:e,icon:s=(0,t.jsx)(i.default,{})}){let{trackAppOpen:o}=(0,n.default)(),d=(0,a.useDeploymentLink)(e);return e.repl.config.isAgentStack?(0,t.jsx)(l.IconButtonLink,{href:d.href,alt:"Automation: no accessible url",disabled:!0,children:s}):e.currentBuild.provider===r.HostingBuildProvider.Cron?(0,t.jsx)(l.IconButtonLink,{href:d.href,alt:"Scheduled Jobs have no accessible url",disabled:!0,children:s}):(0,t.jsx)(l.IconButtonLink,{onClick:()=>{o(e.repl.id)},href:d.href,alt:"Go to site",target:"_blank",children:s})}],202239);var s=e.i(797342),o=e.i(182409),d=e.i(995691),u=e.i(379334),c=e.i(566049),p=e.i(8047),g=e.i(244945),m=e.i(61732),f=e.i(162912);e.s(["StatusBadge",0,function({deployment:e,isPrivate:a=!1,isOrg:n=!1,small:l=!0}){if(!e)if(a)return(0,t.jsx)(g.Tooltip,{tooltip:n?"Internal to your organization":"This App is private",children:(0,t.jsxs)(m.View,{clsx:f.default.dim,row:!0,gap:4,align:"center",children:[(0,t.jsx)(d.default,{size:l?12:16}),(0,t.jsx)(p.Text,{variant:l?"small":void 0,multiline:!1,children:"Private"})]})});else return(0,t.jsx)(g.Tooltip,{tooltip:"Anyone on Replit can view and remix this App",children:(0,t.jsxs)(m.View,{clsx:f.default.dim,row:!0,gap:4,align:"center",children:[(0,t.jsx)(i.default,{size:l?12:16}),(0,t.jsx)(p.Text,{variant:l?"small":void 0,multiline:!1,children:"Public"})]})});let{currentBuild:h}=e,{title:x,color:v}=c.buildStatuses[h.status],j=(0,s.default)(new Date(h.timeCreated),Date.now(),{addSuffix:!0}),R=`Published ${j} by ${h.user?.displayName??u.DELETED_USER_DISPLAY_NAME}`,b=h.status===r.HostingBuildStatus.Success?"Published":x;return(0,t.jsx)(g.Tooltip,{tooltip:R,children:(0,t.jsxs)(m.View,{row:!0,gap:4,align:"center",children:[(0,t.jsx)(o.default,{size:l?12:16,color:v}),(0,t.jsx)(p.Text,{color:"dimmer",variant:l?"small":void 0,multiline:!1,children:b})]})})}],807645)},134869,e=>{e.v({agentRunningPill:"ReplCard-module__K7MMUa__agentRunningPill",appImage:"ReplCard-module__K7MMUa__appImage",iconContainer:"ReplCard-module__K7MMUa__iconContainer",overlayedClickTargets:"ReplCard-module__K7MMUa__overlayedClickTargets",pinBadge:"ReplCard-module__K7MMUa__pinBadge","pulse-blurple":"ReplCard-module__K7MMUa__pulse-blurple",root:"ReplCard-module__K7MMUa__root",smallIconContainer:"ReplCard-module__K7MMUa__smallIconContainer",ticTacsOverlay:"ReplCard-module__K7MMUa__ticTacsOverlay",title:"ReplCard-module__K7MMUa__title"})},443588,e=>{"use strict";var t=e.i(276385),r=e.i(413974),i=e.i(389959),a=e.i(943427),n=e.i(908796);e.i(925218);var l=e.i(587467),s=e.i(641555),o=e.i(752539),d=e.i(252204),u=e.i(757053),c=e.i(416298),p=e.i(546833),g=e.i(66924),m=e.i(816350),f=e.i(83234),h=e.i(202239),x=e.i(453891),v=e.i(234504),j=e.i(730497),R=e.i(547523),b=e.i(441503),y=e.i(480912),S=e.i(50814),T=e.i(595996),_=e.i(345395),C=e.i(807645),k=e.i(480028),A=e.i(661594),w=e.i(919073),I=e.i(825419),O=e.i(488299),U=e.i(744006),D=e.i(565931),P=e.i(8047),M=e.i(244945),F=e.i(61732),E=e.i(519425),z=e.i(921125),$=e.i(134869);function V(e){let r=(0,y.useReplAgentStatus)(e.repl);return(0,t.jsx)(q,{...e,agentStatus:r})}function L(e){let r,i,a=(0,l.useObservable)(e.agentStatus);if(!a)return null;let s=a?.label,d=k.tokens.foregroundDimmest;switch(a?.status){case n.AgentStatusV2.Running:i="blurple";break;case n.AgentStatusV2.PausedWithRequest:i="primary",r=(0,t.jsx)(o.default,{color:d,size:12});break;case n.AgentStatusV2.PausedWithError:i="red",d=k.tokens.foregroundDefault,r=(0,t.jsx)(c.default,{color:d,size:12})}return(0,t.jsx)(U.Pill,{colorway:i,text:s,iconRight:r,clsx:a?.status===n.AgentStatusV2.Running?$.default.agentRunningPill:void 0})}function q({repl:e,isOrg:n=!1,showPinBadge:l=!1,onTogglePin:o,agentStatus:d,presenceUsers:u,trackingContext:c,onDeleteRequested:g,hideDelete:m,shouldShowPublishedArtifactsOnly:f=!1,showLastOpened:h=!1}){let x=(0,j.useFlag)({controlName:"flag-per-user-pinning"}),v=(0,z.replLinkProps)(e),b=(0,A.usePressedProps)(),[y,T]=(0,i.useState)(null),_=e.artifacts,C=f&&e.hostingDeployment?.__typename==="HostingDeployment"?new Set(e.hostingDeployment.currentBuild.artifacts?.map(e=>e.folderName)):null,k=(C?_.filter(e=>C.has(e.artifactId)):_).filter(e=>(0,a.isArtifactKindPreviewable)(e.kind??"web")).map(e=>({id:e.artifactId,name:e.title??e.artifactId,kind:e.kind??"web"})),w=y??k[0]??null,I=(0,s.useObservableMemo)(()=>d?.select(e=>e?.appImageUrl),[d]),O=w?_.find(e=>e.artifactId===w.id)?.latestScreenshotUri??null:null,U=(0,R.useBreakpoint)("tabletMax"),D=k.length>0?O:I||e.latestAgentScreenshotUrl||null;return(0,t.jsxs)(F.View,{tag:"li",clsx:[$.default.root,p.shades.button("halfElevated")],...b,children:[(0,t.jsx)(B,{repl:e,imageUrl:D,ticTacArtifacts:k,activeArtifact:w,maxVisibleTicTacs:U?1:4,onActiveArtifactChange:e=>{T(k.find(t=>t.id===e)??null)},isStarred:l&&e.authorizations.star.isAuthorized&&(x?e.isCurrentUserStarred:e.isStarred),onTogglePin:o}),(0,t.jsxs)(F.View,{grow:!0,shrink:!0,gap:6,p:12,children:[(0,t.jsxs)(F.View,{row:!0,gap:8,align:"start",justify:"space-between",children:[(0,t.jsx)(F.View,{grow:!0,shrink:!0,row:!0,gap:8,align:"center",children:(0,t.jsxs)(F.View,{grow:!0,shrink:!0,children:[(0,t.jsx)(r.default,{...v,clsx:$.default.title,children:(0,t.jsx)(P.Text,{multiline:!1,translate:"no",children:e.title})}),(0,t.jsx)(P.Text,{multiline:!1,variant:"small",color:"dimmest",children:function(e,t){let r=t?e.lastOpened:null,i=r??e.timeUpdated;if(!t)return(0,S.ago)(i);let a=r?"Opened":"Edited";return`${a} ${(0,S.ago)(i)}`}(e,h)})]})}),(0,t.jsx)(F.View,{clsx:$.default.overlayedClickTargets,children:(0,t.jsx)(E.ReplActions,{repl:e,trackingContext:c,deleteAction:m?{type:"hidden"}:{type:"visible",onDeleteRequested:g?()=>g(e.id):void 0}})})]}),n?(0,t.jsx)(N,{repl:e,presenceUsers:u,replLink:v}):null,(0,t.jsx)(K,{repl:e,isOrg:n,agentStatus:d})]})]})}function B({repl:e,imageUrl:r,ticTacArtifacts:i,activeArtifact:a,maxVisibleTicTacs:n,onActiveArtifactChange:l,isStarred:s,onTogglePin:o}){return(0,t.jsxs)(w.ShadesSurface,{clsx:$.default.appImage,style:r?{backgroundImage:`url(${r})`}:void 0,border:!0,children:[s?(0,t.jsx)(F.View,{clsx:$.default.pinBadge,children:(0,t.jsx)(O.IconButton,{alt:"Unpin from top",size:24,onClick:()=>o?.(e.id,!1),children:(0,t.jsx)(u.default,{size:16})})}):null,i&&i.length>0?(0,t.jsxs)(t.Fragment,{children:[!r&&a?(0,t.jsx)(H,{kind:a.kind}):null,(0,t.jsx)(F.View,{clsx:$.default.ticTacsOverlay,children:(0,t.jsx)(_.ArtifactTicTacs,{artifacts:i,activeId:a?.id,onActiveChange:l,maxVisible:n})})]}):(0,t.jsx)(F.View,{align:"center",justify:"center",clsx:{[$.default.smallIconContainer]:r,[$.default.iconContainer]:!r},children:(0,t.jsx)(T.ReplIconWithPlaceholder,{alt:e.title,size:r?24:64,iconUrl:e.iconUrl,isLoading:!e.iconUrl})})]})}function N({repl:e,presenceUsers:i,replLink:a}){let n=(0,l.useObservable)(i,[]),s=e.user?.id,o=s?n.filter(e=>e.id!==s):n;return e.user||0!==o.length?(0,t.jsxs)(F.View,{row:!0,align:"center",justify:"space-between",children:[e.user?(0,t.jsx)(r.default,{href:`/@${e.user.username}`,clsx:$.default.overlayedClickTargets,children:(0,t.jsxs)(F.View,{row:!0,align:"center",gap:4,children:[(0,t.jsx)(I.Avatar,{size:16,username:e.user.username,fullName:e.user.fullName,src:e.user.image}),(0,t.jsx)(P.Text,{variant:"small",color:"dimmer",multiline:!1,children:e.user.username})]})}):null,o.length>0?(0,t.jsx)(W,{users:o,replLink:a,replTitle:e.title}):null]}):null}function W({users:e,replLink:i,replTitle:a}){let n=e.map(e=>e.fullName||e.username),l=`${n.join(", ")} active in ${a}`;return(0,t.jsx)(r.default,{href:i.href,as:i.as,"aria-label":l,clsx:$.default.overlayedClickTargets,children:(0,t.jsx)(D.default,{activeUsers:e,size:16,visibleNumOfUsers:5,getUserLabel:e=>e.fullName||e.username})})}function H({kind:e}){let r=(0,g.getArtifactKindConfigFromString)(e);return(0,t.jsx)(F.View,{align:"center",justify:"center",clsx:$.default.iconContainer,children:(0,t.jsx)(r.Icon,{size:64,color:r.color})})}function G({repl:e,isOrg:i,showArtifactDropdown:a}){let l=e.hostingDeployment?.__typename==="HostingDeployment"?e.hostingDeployment:null,{href:s}=(0,x.useDeploymentLink)(l);if(!l)return(0,t.jsx)(F.View,{clsx:$.default.overlayedClickTargets,children:(0,t.jsx)(C.StatusBadge,{isPrivate:e.isPrivate,isOrg:i})});if(a&&l.currentBuild.status===n.HostingBuildStatus.Success){let r=l.currentBuild.artifacts??[],i=(0,m.getLinkableArtifacts)(r,s);if(i.length>1)return(0,t.jsx)(F.View,{clsx:$.default.overlayedClickTargets,row:!0,gap:4,align:"center",children:(0,t.jsx)(f.DeploymentArtifactDropdown,{artifacts:i,deployment:l,replId:e.id})})}return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)(r.default,{clsx:$.default.overlayedClickTargets,...(0,z.replLinkProps)(e,{initialPaneType:"deployments"}),children:(0,t.jsx)(C.StatusBadge,{deployment:l,isPrivate:e.isPrivate,isOrg:i})}),(0,t.jsx)(F.View,{clsx:$.default.overlayedClickTargets,children:(0,t.jsx)(h.DeploymentSiteLink,{deployment:l,icon:(0,t.jsx)(d.default,{})})})]})}function K({repl:e,isOrg:r,...i}){let a=e.hostingDeployment?.__typename==="HostingDeployment";return(0,t.jsxs)(F.View,{row:!0,gap:4,align:"center",justify:"space-between",children:[(0,t.jsx)(G,{repl:e,isOrg:r,showArtifactDropdown:a}),r&&e.authorizations.viewFileContents.isAuthorized&&!e.authorizations.editFileContents.isAuthorized?(0,t.jsx)(M.Tooltip,{clsx:$.default.overlayedClickTargets,tooltip:e.authorizations.editFileContents.code===n.ReplAuthorizationCode.InsufficientPermissions?"You don't have permission to edit this App. Request permissions from the creator or an admin.":e.authorizations.editFileContents.message,children:(0,t.jsx)(U.Pill,{colorway:"grey",text:"Read-only"})}):(0,t.jsx)(t.Fragment,{children:i.agentStatus?(0,t.jsx)(L,{agentStatus:i.agentStatus}):null})]})}e.s(["ReplCard",0,function(e){let r=(0,i.useContext)(v.AgentStatusContext),a=(0,b.useReplPresenceUsers)(e.repl.id);return r?(0,t.jsx)(V,{...e,presenceUsers:a}):(0,t.jsx)(q,{...e,presenceUsers:a})},"ReplCardView",0,q])}]);

//# debugId=fec26b46-5882-fb4f-fc6c-ab88bfe0b99e
//# sourceMappingURL=0ge36j4g-9byf.js.map
